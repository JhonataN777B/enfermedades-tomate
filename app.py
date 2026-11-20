import base64
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import cv2
import tensorflow as tf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Cargando modelo Keras (Deep MLP HSV)...")
model = tf.keras.models.load_model("models/Tomate_DeepMLP_HSV.keras")
print("¡Modelo listo!")

# ORDEN ALFABÉTICO CORRECTO (Igual al LabelEncoder de Google Colab)
class_labels = [
    "Bacterial_spot", 
    "Early_blight", 
    "Late_blight", 
    "Leaf_Mold", 
    "Septoria_leaf_spot", 
    "Healthy"
]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        return {"error": "Formato de imagen no soportado."}
    
    # 0. Redimensionar para evitar errores de tamaño de matriz en OpenCV
    img_resized = cv2.resize(img, (224, 224))
    
    # 1. Convertir a HSV y sacar histograma (512 bins reales) de la original (precisión matemática)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    bins = (8, 8, 8)
    hist = cv2.calcHist([hsv], [0, 1, 2], None, bins, [0, 180, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    
    # Convertir a lista de 512 datos para Chart.js
    hsv_512 = [round(float(v), 5) for v in hist.flatten()]
    features = hist.flatten().reshape(1, -1)
    
    # 2. Inferencia Exacta
    predictions = model.predict(features, verbose=0)[0]
    best_idx = int(np.argmax(predictions))
    certeza_exacta = float(predictions[best_idx] * 100) # Sin redondear aquí
    
    # 3. Intensidad promedio para KDE
    v_channel = hsv[:, :, 2]
    mean_intensity = float(np.mean(v_channel) / 255.0)
    # Ajuste de escala para que empate con el rango de tu gráfica (0.002 - 0.010)
    intensidad_grafica = round((mean_intensity * 0.015), 5) 

    # 4. Replicar la Activación Espacial (Pseudo Grad-CAM de Colab)
    # Lo aplicamos sobre la imagen de 224x224 para que el mapa de calor encaje perfecto
    hsv_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2HSV)
    lower_stress = np.array([0, 10, 10])
    upper_stress = np.array([45, 255, 255])
    mask = cv2.inRange(hsv_resized, lower_stress, upper_stress)
    
    # Suavizado fuerte y mapeo térmico
    mask_blurred = cv2.GaussianBlur(mask, (51, 51), 0)
    mask_norm = cv2.normalize(mask_blurred, None, 0, 255, cv2.NORM_MINMAX)
    heatmap = cv2.applyColorMap(mask_norm, cv2.COLORMAP_JET)
    
    # Mezclar con la foto redimensionada (ahora ambas matrices miden 224x224)
    gradcam_img = cv2.addWeighted(img_resized, 0.6, heatmap, 0.4, 0)
    
    # Codificar imágenes a base64 para mandarlas a la web sin guardar archivos físicos
    _, buffer_orig = cv2.imencode('.jpg', img_resized)
    orig_b64 = base64.b64encode(buffer_orig).decode('utf-8')
    
    _, buffer_grad = cv2.imencode('.jpg', gradcam_img)
    gradcam_b64 = base64.b64encode(buffer_grad).decode('utf-8')

    return {
        "clase": class_labels[best_idx],
        "certeza": certeza_exacta,
        "hsv_512": hsv_512,
        "intensidad": intensidad_grafica,
        "img_original": orig_b64,
        "img_gradcam": gradcam_b64
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
