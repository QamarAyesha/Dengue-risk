function teachable_machine_component() {
    components.html(
        `
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
                    console.log("Raw predictions:", prediction);

                    // Log detailed predictions
                    for (let i = 0; i < prediction.length; i++) {
                        console.log(`Class: ${prediction[i].className}, Probability: ${prediction[i].probability}`);
                    }

                    const labelContainer = document.getElementById("label-container");
                    labelContainer.innerHTML = ""; // Clear previous results

                    let hasStagnantWater = false;
                    let maxConfidence = 0;
                    let predictedClass = "";

                    for (let i = 0; i < maxPredictions; i++) {
                        const className = prediction[i].className;
                        const probability = prediction[i].probability.toFixed(2);

                        // Track the class with the highest confidence
                        if (probability > maxConfidence) {
                            maxConfidence = probability;
                            predictedClass = className;
                        }

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
                            hasStagnantWater = true;
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

                    // Send results back to Streamlit
                    if (window.Streamlit) {
                        window.Streamlit.setComponentValue({
                            predicted_class: predictedClass,
                            confidence: maxConfidence,
                            has_stagnant_water: hasStagnantWater
                        });
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
        `,
        height=500,
    );
}
