import numpy as np
import os
import base64
from io import BytesIO
from PIL import Image
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input   # ✅ FIXED

app = Flask(__name__)

model = load_model("vgg-16-nail-disease.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/nailhome')
def nailhome():
    return render_template('nailhome.html')

@app.route('/nailpred')
def nailpred():
    return render_template('nailpred.html')

@app.route('/nailresult', methods=["POST"])
def nailresult():

    upload_folder = "uploads"
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    filepath = None

    # -------- Case 1: Normal Upload --------
    if 'image' in request.files and request.files['image'].filename != "":
        f = request.files['image']
        filepath = os.path.join(upload_folder, f.filename)
        f.save(filepath)

    # -------- Case 2: Live Camera Capture --------
    elif request.form.get("captured_image"):
        image_data = request.form.get("captured_image")
        image_data = image_data.split(",")[1]
        image_bytes = base64.b64decode(image_data)

        img = Image.open(BytesIO(image_bytes))
        filepath = os.path.join(upload_folder, "captured.png")
        img.save(filepath)

    else:
        return "No image provided"

    # -------- Preprocessing --------
    img = image.load_img(filepath, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    img_data = preprocess_input(x)

    prediction_probs = model.predict(img_data)
    prediction = np.argmax(prediction_probs)
    confidence = round(np.max(prediction_probs) * 100, 2)

    classes = [
        'Darier_s disease', 'Muehrck_e_s lines', 'alopecia areata',
        'beau_s lines', 'bluish nail', 'clubbing', 'eczema',
        'half and half nails (Lindsay_s nails)', 'koilonychia',
        'leukonychia', 'onycholysis', 'pale nail',
        'red lunula', 'splinter hemorrage', 'terry_s nail',
        'white nail', 'yellow nails'
    ]

    result = classes[prediction]

    return render_template("nailpred.html",
                           prediction=result,
                           confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
