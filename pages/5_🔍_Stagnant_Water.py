import streamlit as st
import numpy as np
from PIL import Image

# Initialize session state to store results
if "last_results" not in st.session_state:
    st.session_state.last_results = [
        {
            "file_name": "default_image_1.jpg",
            "city": "Lahore",  # Updated to use city instead of location
            "predicted_class": "No Stagnant Water",
            "confidence": 0.85,
            "risk_score": 15
        },
        {
            "file_name": "default_image_2.jpg",
            "city": "Karachi",  # Updated to use city instead of location
            "predicted_class": "Stagnant Water",
            "confidence": 0.92,
            "risk_score": 75
        }
    ]

# Placeholder for model loading
def load_model(model_path):
    st.warning("Model loading is currently disabled. This is a placeholder.")
    return None

# Placeholder for preprocessing
def preprocess_image(image):
    st.warning("Preprocessing is currently disabled. This is a placeholder.")
    return np.zeros((1, 224, 224, 3))  # Return a dummy array

# Placeholder for prediction
def predict(model, image):
    st.warning("Prediction is currently disabled. This is a placeholder.")
    return np.random.rand(1, 2)  # Return random predictions for 2 classes

# Streamlit page
def main():
    st.set_page_config(page_title="Satellite Image Analysis for Dengue Risk", layout="wide")
    st.title("🌍 Satellite Image Analysis for Dengue Risk")
    st.write("Upload or select satellite images to detect stagnant water spots.")

    # Placeholder for model path
    model_path = "model/model.json"  # Replace with the path to your model later
    model = load_model(model_path)

    # City selection
    st.subheader("Select City")
    city = st.selectbox(
        "Choose a city",
        ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Multan"],  # Major cities
        index=0  # Default to Lahore
    )

    # File uploader for multiple satellite images
    uploaded_files = st.file_uploader(
        "Upload satellite images...", 
        type=["jpg", "jpeg", "png"], 
        accept_multiple_files=True
    )

    # Process uploaded files
    if uploaded_files:
        results = []
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            st.image(image, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)

            # Preprocess and predict (placeholder)
            processed_image = preprocess_image(image)
            predictions = predict(model, processed_image)

            # Display the result (placeholder)
            class_names = ["No Stagnant Water", "Stagnant Water"]  # Replace with your class names
            predicted_class = class_names[np.argmax(predictions)]
            confidence = np.max(predictions)
            risk_score = calculate_risk_score(predictions)

            # Store results
            results.append({
                "file_name": uploaded_file.name,
                "city": city,  # Updated to use city
                "predicted_class": predicted_class,
                "confidence": confidence,
                "risk_score": risk_score
            })

            # Display results for the current file
            st.write(f"📍 **City**: {city}")
            st.write(f"🎉 Predicted Class (placeholder): **{predicted_class}** with {confidence:.2f} confidence!")
            st.write(f"🦟 Dengue Risk Score (placeholder): **{risk_score}**")
            if predicted_class == "Stagnant Water":
                st.error("⚠️ Stagnant water detected! This is a potential dengue breeding site. Please take action.")
            st.write("---")

        # Save results to session state
        st.session_state.last_results = results

    # Display last results or default results if no new files are uploaded
    st.subheader("Last Results")
    for result in st.session_state.last_results:
        st.write(f"📄 **File Name**: {result['file_name']}")
        st.write(f"📍 **City**: {result['city']}")  # Updated to use city
        st.write(f"🎉 Predicted Class (placeholder): **{result['predicted_class']}** with {result['confidence']:.2f} confidence!")
        st.write(f"🦟 Dengue Risk Score (placeholder): **{result['risk_score']}**")
        if result["predicted_class"] == "Stagnant Water":
            st.error("⚠️ Stagnant water detected! This is a potential dengue breeding site. Please take action.")
        st.write("---")

# Placeholder for risk score calculation
def calculate_risk_score(predictions, threshold=0.5):
    """Calculate a dengue risk score based on predictions."""
    # Count the number of stagnant water spots (placeholder)
    stagnant_spots = np.sum(predictions > threshold)
    
    # Calculate risk score (example formula)
    risk_score = stagnant_spots * 10  # Adjust based on your requirements
    return risk_score

if __name__ == "__main__":
    main()
