import glob
import random
from importlib import resources as importlib_resources
from os import environ
from os.path import join

import requests
import streamlit as st
from PIL import Image


def a_random_image_of_a_muffin_or_a_chihuahua() -> str:
    with importlib_resources.path('data', 'muffin') as path_to_muffin_images:
        with importlib_resources.path('data', 'chihuahua') as path_to_chihuahua_images:
            return random.choice(
                glob.glob(join(path_to_muffin_images, '*.jpg')) +
                glob.glob(join(path_to_chihuahua_images, '*.jpg'))
            )


def display_an_image(an_image: bytes) -> None:
    st.header("🐶 chihuahua 👇" if "chihuahua" in img_path else "🍪 muffin 👇")
    st.image(an_image, use_column_width=True)
    st.subheader("Predictions 👇")


def display_prediction(rank_starting_from_zero, labels_and_probas):
    st.write(
        f"{rank_starting_from_zero + 1}. ",
        "🏆" if "Chihuahua" in labels_and_probas[1] else "",
        predictions[1],
        float("{:.2f}".format(labels_and_probas[2]))
    )


def predict_class_over_http_for(an_image_path: str) -> dict:
    INFERENCE_HOST = environ.get('INFERENCE_HOST', 'localhost')
    return requests.post(f"http://{INFERENCE_HOST}:8000/predict",
                         files={"file": open(an_image_path, "rb")}).json().get("filename")


st.set_page_config(layout="centered")
st.title('Muffin 🍪 or chihuahua 🐶')
cols = st.beta_columns(3)

for each_col in cols:
    with each_col:
        img_path = a_random_image_of_a_muffin_or_a_chihuahua()
        an_image = Image.open(img_path)
        display_an_image(an_image)
        for i, predictions in enumerate(predict_class_over_http_for(img_path)):
            display_prediction(i, predictions)

_, button_column, _ = st.beta_columns(3)
with button_column:
    st.button("👉 Shuffle & predict 👈")
