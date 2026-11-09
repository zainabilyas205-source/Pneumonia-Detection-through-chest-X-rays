from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import time

app = Flask(__name__)

model = YOLO("best.pt")

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True) 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image")
        if file:
            ts = str(int(time.time()))
            filename = ts + "_" + file.filename
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Prediction
            results = model(filepath)

            predicted_filename = "pred_" + filename
            predicted_path = os.path.join(app.config["RESULT_FOLDER"], predicted_filename)
            results[0].save(filename=predicted_path)

            # --- BREAKTHROUGH LOGIC ---
            prediction = "NO - Normal"
            confidence = 0
            
            
            detection_count = len(results[0]) 

            if detection_count > 0:
                prediction = "YES - Pneumonia Detected"
                
                try:
                    
                    if hasattr(results[0], 'boxes') and len(results[0].boxes) > 0:
                        conf_val = results[0].boxes.conf[0].item()
                        confidence = round(float(conf_val) * 100, 2)
                    else:
                        confidence = "Detected"
                except:
                    confidence = "Detected"

            # Terminal debugging 
            print(f"--- DETECTED OBJECTS: {detection_count} ---")
            print(f"--- FINAL TEXT: {prediction} ---")

            return render_template(
                "index.html",
                original=filepath,
                predicted=predicted_path,
                prediction=prediction,
                confidence=confidence
            )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)