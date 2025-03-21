import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from PIL import Image

# Initialize session state to store results
if "last_results" not in st.session_state:
    st.session_state.last_results = [
        {
            "file_name": "default_image_1.jpg",
            "city": "Lahore",  
            "predicted_class": "No Stagnant Water",
            "confidence": 0.85,
            "risk_score": 15
        },
        {
            "file_name": "default_image_2.jpg",
            "city": "Karachi",  
            "predicted_class": "Stagnant Water",
            "confidence": 0.92,
            "risk_score": 75
        }
    ]

# Teachable Machine TensorFlow.js Integration with File Upload
def teachable_machine_component():
    components.html(
        """
        <div style="font-family: sans-serif; color: var(--text-color);">Teachable Machine Image Model</div>
        <input type="file" id="file-input" accept="image/*" />
        <div id="image-container"></div>
        <div id="label-container" style="margin-top: 20px; font-size: 16px; color: var(--text-color);"></div>
        <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest/dist/teachablemachine-image.min.js"></script>
        <script type="text/javascript">
            // Model URLs
            const modelURL = "https://storage.googleapis.com/tm-model/jtmut1SnG/model.json";
            const metadataURL = "https://storage.googleapis.com/tm-model/jtmut1SnG/metadata.json";

            let model, maxPredictions;

            // Load the model and metadata
            async function init() {
                try {
                    console.log("Loading model...");
                    model = await tmImage.load(modelURL, metadataURL);
                    maxPredictions = model.getTotalClasses();
                    console.log("Model loaded successfully!");
                    console.log("Model classes:", maxPredictions);

                    // Set up file input listener
                    const fileInput = document.getElementById("file-input");
                    fileInput.addEventListener("change", handleFileUpload, false);
                } catch (error) {
                    console.error("Error loading model:", error);
                }
            }

            // Handle file upload
            async function handleFileUpload(event) {
                const file = event.target.files[0];
                if (!file) return;

                console.log("File uploaded:", file.name);

                // Display the uploaded image
                const imageContainer = document.getElementById("image-container");
                imageContainer.innerHTML = "";
                const img = document.createElement("img");
                img.src = URL.createObjectURL(file);
                img.width = 200;
                img.height = 200;
                imageContainer.appendChild(img);

                // Make predictions
                console.log("Making predictions...");
                await predict(img);
            }

            // Make predictions on the uploaded image
            async function predict(image) {
                try {
                    console.log("Predicting...");
                    const prediction = await model.predict(image);
                    console.log("Predictions:", prediction);

                    const labelContainer = document.getElementById("label-container");
                    labelContainer.innerHTML = ""; // Clear previous results

                    for (let i = 0; i < maxPredictions; i++) {
                        const className = prediction[i].className;
                        const probability = prediction[i].probability.toFixed(2);

                        // Create a result div
                        const resultDiv = document.createElement("div");
                        resultDiv.style.marginBottom = "10px";

                        // Add class name and probability
                        const classText = document.createElement("span");
                        classText.innerText = `${className}: `;
                        classText.style.fontWeight = "bold";
                        classText.style.color = "var(--text-color)";

                        const probabilityText = document.createElement("span");
                        probabilityText.innerText = `${probability}`;
                        probabilityText.style.color = probability > 0.5 ? "red" : "green";

                        resultDiv.appendChild(classText);
                        resultDiv.appendChild(probabilityText);

                        // Highlight high-risk predictions
                        if (className === "Stagnant Water" && probability > 0.5) {
                            resultDiv.style.backgroundColor = "var(--background-color)";
                            resultDiv.style.color = "var(--text-color)";
                            resultDiv.style.padding = "5px";
                            resultDiv.style.borderRadius = "5px";
                            resultDiv.style.border = "1px solid red";
                        } else {
                            resultDiv.style.backgroundColor = "var(--background-color)";
                            resultDiv.style.color = "var(--text-color)";
                            resultDiv.style.padding = "5px";
                            resultDiv.style.borderRadius = "5px";
                            resultDiv.style.border = "1px solid green";
                        }

                        labelContainer.appendChild(resultDiv);
                    }
                    console.log("Predictions completed!");
                } catch (error) {
                    console.error("Error making predictions:", error);
                }
            }

            // Initialize the model
            init();
        </script>
        <style>
            :root {
                --text-color: black;
                --background-color: white;
            }
            @media (prefers-color-scheme: dark) {
                :root {
                    --text-color: white;
                    --background-color: #1e1e1e;
                }
            }
        </style>
        """,
        height=400,
    )

# Calculate risk score
def calculate_risk_score(predictions, threshold=0.5):
    """Calculate a dengue risk score based on predictions."""
    # Count the number of stagnant water spots (placeholder)
    stagnant_spots = np.sum(predictions > threshold)
    
    # Calculate risk score (example formula)
    risk_score = stagnant_spots * 10  # Adjust based on your requirements
    return risk_score

# Streamlit App
def main():
    st.set_page_config(page_title="Satellite Image Analysis for Dengue Risk", layout="wide")
    st.title("Satellite Image Analysis for Dengue Risk")
    st.write("Upload satellite images to detect stagnant water spots.")

    # City selection
    st.subheader("Select City")
    city = st.selectbox(
        "Choose a city",
        ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Multan"],  # Major cities
        index=0  # Default to Lahore
    )

    # Add Teachable Machine Component
    st.subheader("Teachable Machine Model")
    teachable_machine_component()
  
    # Display last results or default results if no new files are uploaded
    st.subheader("Sample Results")
    for result in st.session_state.last_results:
        st.write(f"📄 **File Name**: {result['file_name']}")
        st.write(f"📍 **City**: {result['city']}")  # Updated to use city
        st.write(f"🎉 Predicted Class: **{result['predicted_class']}** with {result['confidence']:.2f} confidence!")
        st.write(f"🦟 Dengue Risk Score: **{result['risk_score']}**")
        if result["predicted_class"] == "Stagnant Water":
            st.error("⚠️ Stagnant water detected! This is a potential dengue breeding site. Please take action.")
        st.write("---")

if __name__ == "__main__":
    main()
