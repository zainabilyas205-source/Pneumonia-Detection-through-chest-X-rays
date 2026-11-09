Pneumonia Detection Through Chest X-rays

An academic AI and computer-vision project that explores the analysis of chest X-ray images using a trained Ultralytics YOLO model. The Flask web application lets users upload an X-ray and view the model output with highlighted detection regions.
⚠️ Important medical disclaimer: This is an educational research prototype, not a clinically validated medical device. Its output is not a diagnosis and must not be used to make medical decisions. Chest X-rays should be interpreted by qualified healthcare professionals.

📌 Project Overview
Pneumonia is a lung infection that can appear in chest X-ray images. This project applies computer vision to identify image regions that the trained model has learned to associate with pneumonia.

The project workflow includes:
1. 📂 Preparing and organizing a chest X-ray image dataset.
2. 🧠 Training an Ultralytics YOLO model.
3. 📊 Evaluating the trained model on validation/test data.
4. 💾 Saving the trained weights as best.pt.
5. 🌐 Loading the model in a Flask application.
6. 📤 Uploading an X-ray image through a browser.
7. 🖼️ Displaying the original image, annotated model output, detection count, and available confidence score.
✨ Main Features
- Upload chest X-ray images through a web interface.
- Run inference using trained YOLO weights.
- Display the original and annotated images side by side.
- Show the number of detected regions.
- Show the first detected region's confidence score when available.
- Supports standard YOLO bounding-box results and YOLO oriented bounding-box (OBB) results.
- Basic upload validation and a 10 MB upload limit.
- Responsive interface for desktop and mobile screens.
🛠️ Technology Stack
- Python — application and inference logic
- Ultralytics YOLO — object detection model
- Flask — web application framework
- HTML5 / CSS3 — user interface
- Google Colab — model training environment (if used for your training run)
- Visual Studio Code — local development environment
📁 Repository Structure
pneumonia-detection-ai/
├── app.py
├── best.pt                 # Add your trained model locally; not committed to Git
├── requirements.txt
├── .gitignore
├── README.md
├── LICENSE
├── templates/
│   └── index.html
└── static/
    ├── uploads/
    │   └── .gitkeep
    └── results/
        └── .gitkeep
🧠 Model and Dataset Information
The project history includes chest X-ray classification experiments and a later YOLOv8 oriented-bounding-box (OBB) training workflow. The latest OBB training setup used an Ultralytics YOLOv8n-OBB model and a dataset organized into train, valid, and test folders.

Previously recorded OBB training configuration:
- Model family: YOLOv8n-OBB
- Image size: 640
- Epochs: 50
- Batch size: 8
- Training device: NVIDIA Tesla T4 (Google Colab)
- Training images: 2,182
- Validation images: 279
- Best weights output: best.pt
These are project-history details, not a claim that the model is clinically validated. Confirm the exact run and metrics from your own training results before using them in a formal report.
📚 Dataset Citation
Add the exact dataset name, creator/organization, source URL, version, access date, and license here. Follow the dataset provider's terms. Do not upload private, identifiable, or restricted medical images to this public repository.
⚙️ Setup and Installation
1️⃣ Clone the Repository
git clone https://github.com/YOUR-USERNAME/pneumonia-detection-ai.git
cd pneumonia-detection-ai
2️⃣ Create and Activate a Virtual Environment
Windows Command Prompt:
python -m venv venv
venv\Scripts\activate
macOS / Linux:
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt
4️⃣ Add the Trained Model
Copy your trained best.pt file into the repository's root directory, at the same level as app.py.

The model file is intentionally excluded from Git because model weights can be large. If you want to distribute it, use a suitable model-hosting service or Git LFS, and check the dataset/model license before sharing.
5️⃣ Run the Flask Application
python app.py
Open this address in your browser:
http://127.0.0.1:5000/
Upload a supported chest X-ray image (.jpg, .jpeg, .png, .bmp, or .webp) and select Analyze Image.
🔄 How the Application Works
1. Flask receives the uploaded image.
2. The filename is sanitized and a unique filename is generated.
3. The image is saved in static/uploads/.
4. Ultralytics loads the image and performs prediction with best.pt.
5. The model output is saved in static/results/.
6. The application checks the model's detection output (standard boxes or OBB).
7. The webpage displays the original image, annotated output, detection count, and confidence when available.
📊 Model Evaluation
Use the metrics produced by the actual training/evaluation run. Common object-detection metrics include:
- Precision: proportion of predicted detections that are correct.
- Recall: proportion of relevant objects that the model detects.
- mAP@0.5: mean average precision at an intersection-over-union threshold of 0.5.
- mAP@0.5:0.95: mean average precision across multiple IoU thresholds.
- Confusion matrix: summary of correct and incorrect class predictions, where applicable.
Insert your verified plots, confusion matrix, and test-set metrics in the project report. Do not estimate or invent scores.
⚠️ Limitations
- Performance depends on the quality, diversity, labeling, and representativeness of the training dataset.
- Results may not generalize to images from different hospitals, devices, populations, or acquisition settings.
- A detection result is not equivalent to a confirmed clinical diagnosis.
- The web app is a demonstration and does not include clinical workflow integration, authentication, audit logging, or regulatory validation.
- The displayed confidence is a model score, not the probability that a patient has pneumonia.
🚀 Future Improvements
- Evaluate on a larger, independent, appropriately licensed test dataset.
- Improve data quality and assess class imbalance and possible dataset bias.
- Add model versioning and reproducible experiment tracking.
- Add automated tests, structured logging, and safer production deployment.
- Improve accessibility and interface usability.
- Conduct validation with qualified medical and research professionals before considering any clinical use.
🖼️ Screenshots
Add your own screenshots to a screenshots/ folder and embed them here, for example:
![Application home page](screenshots/home-page.png)
![Prediction result](screenshots/prediction-result.png)
Suggested screenshots:
1. Application home page.
2. Image upload screen.
3. Original X-ray and annotated prediction result.
4. Training results / metrics from your actual experiment.
🔐 Responsible Use and Privacy
Only use images you are authorized to process. Avoid uploading identifiable patient information. Do not publish patient data, private medical images, or credentials in this repository. This project is intended for learning and research demonstration only.
👩‍💻 Author
Your Name
Software Engineering Project
Add your GitHub profile and LinkedIn profile links here.
📄 License
This repository's source code is provided under the MIT License in LICENSE. This does not automatically grant rights to the dataset or trained model weights. Check their separate licenses and terms.
