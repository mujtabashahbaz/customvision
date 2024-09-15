import streamlit as st
import requests
from PIL import Image
import io

# Azure Custom Vision API details
API_KEY = 'f1941114bac543859fba9ea1749f1979'
ENDPOINT = 'https://southcentralus.api.cognitive.microsoft.com/'
PREDICTION_URL = ENDPOINT + 'customvision/v3.0/Prediction/YOUR_PROJECT_ID/classify/iterations/YOUR_ITERATION_NAME/image'

def get_prediction(image_bytes):
    headers = {
        'Prediction-Key': API_KEY,
        'Content-Type': 'application/octet-stream'
    }
    response = requests.post(PREDICTION_URL, headers=headers, data=image_bytes)
    return response.json()

st.title('Azure Custom Vision Image Classification')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Convert image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='JPEG')
    image_bytes = image_bytes.getvalue()

    # Get prediction
    result = get_prediction(image_bytes)
    st.write(result)
