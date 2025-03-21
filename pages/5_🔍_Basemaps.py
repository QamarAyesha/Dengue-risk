import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd

# Load the Teachable Machine TensorFlow.js model
def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model

# Preprocess the image for the model
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to match model input size
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Streamlit app
def main():
    st.title("Teachable Machine + Streamlit Integration")
    st.write("Upload an image for classification")

    # Load the model
    model_path = "path_to_your_model"  # Replace with the path to your model.json
    model = load_model(model_path)

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Preprocess and predict
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        st.write("Predictions:", predictions)

        # Display the result
        class_names = ["Class 1", "Class 2", "Class 3"]  # Replace with your class names
        predicted_class = class_names[np.argmax(predictions)]
        confidence = np.max(predictions)
        st.write(f"🎉 Predicted Class: **{predicted_class}** with {confidence:.2f} confidence!")

        # Show confidence scores as a bar chart
        st.write("Confidence Scores:")
        fig, ax = plt.subplots()
        ax.bar(class_names, predictions[0])
        ax.set_ylabel("Confidence")
        ax.set_xlabel("Class")
        st.pyplot(fig)

        # Show a custom message based on the prediction
        if predicted_class == "Class 1":
            st.success("This is Class 1! Here's what you should do: [Action for Class 1]")
        elif predicted_class == "Class 2":
            st.warning("This is Class 2! Here's what you should do: [Action for Class 2]")
        else:
            st.error("This is Class 3! Here's what you should do: [Action for Class 3]")

        # Add a reset button
        if st.button("Reset"):
            st.experimental_rerun()

if __name__ == "__main__":
    main()
