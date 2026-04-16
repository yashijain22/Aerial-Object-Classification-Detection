import streamlit as st
from PIL import Image
from ultralytics import YOLO

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Aerial Object Detection", layout="centered")

st.title("🚁 Aerial Object Detection System")
st.write("Upload an image to detect birds and drones")

# -------------------------------
# Load YOLO Model
# -------------------------------
@st.cache_resource
def load_model():
    model = YOLO("../models/yolov8_model.pt")
    return model

yolo_model = load_model()

# -------------------------------
# Upload Image
# -------------------------------
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.subheader("🎯 Object Detection")

    results = yolo_model.predict(image)

    result_img = results[0].plot()

    st.image(result_img, caption="Detected Objects", use_column_width=True)