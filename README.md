# 🚁 Aerial Object Classification and Detection

## 📌 Overview
This project focuses on detecting and classifying aerial objects such as birds 🐦 and drones 🚁 using Deep Learning techniques. It combines image classification, transfer learning, and object detection to build a complete end-to-end system.

## 🎯 Problem Statement
The objective of this project is to classify aerial images into Bird or Drone and also detect their exact location in the image using bounding boxes. The system also provides confidence scores for predictions. This has real-world applications in surveillance systems, airspace monitoring, and security detection.

## 🧠 Models Used
This project uses three different models:
- CNN (Baseline Model): A custom Convolutional Neural Network used for basic image classification and understanding baseline performance.
- MobileNetV2 (Transfer Learning): A pre-trained model fine-tuned on the dataset to achieve better accuracy and faster training.
- YOLOv8 (Object Detection): A real-time object detection model that detects objects using bounding boxes and provides class labels with confidence scores.

## 📂 Project Structure
Aerial_Object_Classification/
│
├── models/
│   ├── mobilenet_model.h5
│   └── yolov8_model.pt
│
├── notebooks/
│   ├── CNN_Model.ipynb
│   ├── MobileNet_Model.ipynb
│   └── YOLO_Model.ipynb
│
├── streamlit_app/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore

## ⚙️ Installation
Clone the repository and install dependencies:
git clone https://github.com/yashijain22/Aerial-Object-Classification-Detection.git  
cd Aerial-Object-Classification-Detection  
pip install -r requirements.txt  

## ▶️ Run the Application
Navigate to the Streamlit app folder and run:
cd streamlit_app  
streamlit run app.py  

## 📊 Model Evaluation
For classification models, evaluation is done using Accuracy, Precision, Recall, and F1 Score.  
For object detection, evaluation is based on confidence scores and bounding box accuracy.  

Model comparison:
- CNN provides baseline performance  
- MobileNetV2 improves classification accuracy  
- YOLOv8 performs best for detection and localization  

## 📸 Output
The system detects birds and drones in images, displays bounding boxes around them, and shows confidence scores for each detected object.

## ⚠️ Note
The CNN model is not included in the repository due to file size limitations. It can be trained using the provided notebook.

## 🛠️ Technologies Used
Python, TensorFlow/Keras, Ultralytics YOLOv8, OpenCV, Streamlit

## 🚀 Future Enhancements
Real-time video detection, multi-class object detection, and cloud deployment can be added in the future.

## 👩‍💻 Author
Yashi Jain
