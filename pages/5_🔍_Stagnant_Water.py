import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from PIL import Image

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
                await predict(img, file.name);
            }

            // Make predictions on the uploaded image
            async function predict(image, fileName) {
                try {
                    console.log("Predicting...");
                    const prediction = await model.predict(image);
                    console.log("Predictions:", prediction);

                    const labelContainer = document.getElementById("label-container");
                    labelContainer.innerHTML = ""; // Clear previous results

                    let riskScore = 0;
                    let predictedClass = "Unknown";
                    let confidence = 0;

                    for (let i = 0; i < maxPredictions; i++) {
                        const className = prediction[i].className;
                        const probability = parseFloat(prediction[i].probability.toFixed(2));

                        if (probability > confidence) {
                            predictedClass = className;
                            confidence = probability;
                        }
                        
                        if (className === "Stagnant Water") {
                            riskScore = probability; // Risk score is the probability itself (always <1)
                        }
                    }

                    // Display full result
                    labelContainer.innerHTML += `<div style='margin-top: 10px; padding: 10px; border: 1px solid #ccc; border-radius: 5px;'>
                        📄 <b>File Name:</b> ${fileName} <br>
                        📍 <b>City:</b> ${document.getElementById("city-selector").value} <br>
                        🎉 <b>Predicted Class:</b> ${predictedClass} with ${confidence.toFixed(2)} confidence! <br>
                        🦟 <b>Dengue Risk Score:</b> ${riskScore.toFixed(2)}
                    </div>`;
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
        height=600,
    )

# Streamlit App
def main():
    st.set_page_config(page_title="Satellite Image Analysis for Dengue Risk", layout="wide")
    st.title("Satellite Image Analysis for Dengue Risk")
    st.write("Upload satellite images to detect stagnant water spots and assess dengue risk.")

    # City selection
    st.subheader("Select City")
    city = st.selectbox(
        "Choose a city",
        ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Multan"],  # Major cities
        index=0,  # Default to Lahore
        key="city-selector"
    )

    # Add Teachable Machine Component
    st.subheader("Teachable Machine Model")
    teachable_machine_component()

if __name__ == "__main__":
    main()
