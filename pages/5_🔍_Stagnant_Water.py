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

                    let riskScore = 0;
                    for (let i = 0; i < maxPredictions; i++) {
                        const className = prediction[i].className;
                        const probability = parseFloat(prediction[i].probability.toFixed(2));
                        
                        if (className === "Stagnant Water") {
                            riskScore = probability; // Risk score is the probability itself (always <1)
                        }
                        
                        const resultDiv = document.createElement("div");
                        resultDiv.style.marginBottom = "10px";

                        const classText = document.createElement("span");
                        classText.innerText = `${className}: `;
                        classText.style.fontWeight = "bold";
                        classText.style.color = "var(--text-color)";

                        const probabilityText = document.createElement("span");
                        probabilityText.innerText = `${probability}`;
                        probabilityText.style.color = probability > 0.5 ? "red" : "green";

                        resultDiv.appendChild(classText);
                        resultDiv.appendChild(probabilityText);
                        labelContainer.appendChild(resultDiv);
                    }

                    // Display risk score
                    const riskDiv = document.createElement("div");
                    riskDiv.innerText = `🦟 Dengue Risk Score: ${riskScore.toFixed(2)}`;
                    riskDiv.style.fontWeight = "bold";
                    riskDiv.style.marginTop = "10px";
                    labelContainer.appendChild(riskDiv);
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
        index=0  # Default to Lahore
    )

    # Add Teachable Machine Component
    st.subheader("Teachable Machine Model")
    teachable_machine_component()

if __name__ == "__main__":
    main()
