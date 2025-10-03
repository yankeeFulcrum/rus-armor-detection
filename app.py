import streamlit as st
from ultralytics import YOLO
from PIL import Image

model = YOLO("rus-armor-detectionv0.0.1-alpha.pt")

st.title("Russian Armor Detection")

uploaded_file = st.file_uploader("Upload an image", type=["jpg","png","jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded", use_container_width=True)

    if st.button("Run Detection"):
        results = model.predict(source=image, save=False, show=False)
        res_plotted = results[0].plot()   # numpy array with boxes drawn
        st.image(res_plotted, caption="Detection Results", use_container_width=True)

