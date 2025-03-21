import streamlit as st
import streamlit.components.v1 as components
import json  # Import the json module

# Define class labels
class_labels = {
    0: "No Stagnant Water",
    1: "Stagnant Water - Low Risk",
    2: "Stagnant Water - High Risk"
}

# Teachable Machine TensorFlow.js Integration with File Upload
def teachable_machine_component(class_labels):
    # Convert class_labels to JSON string
    class_labels_json = json.dumps(class_labels)
    
    # Use a multi-line string for the HTML/JavaScript code
    html_code = f"""
    <div style="font-family: sans-serif; color: var(--text-color);">Teachable Machine Image Model</div>
    <input type="file" id="file-input" accept="image/*" />
    <div id="image-container"></div>
    <div id="label-container" style="margin-top: 20px; font-size: 16px; color: var(--text-color);"></div>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
    <script type="text/javascript">
        // Teachable Machine model URL
        const modelURL = "https://teachablemachine.withgoogle.com/models/jtmut1SnG/model.json";

        // Class labels
        const classLabels = {class_labels_json};

        let model;

        // Load the model
        async function init() {{
            try {{
                console.log("Loading model...");
                console.log("Model URL:", modelURL);

                // Load the model using tf.loadLayersModel
                model = await tf.loadLayersModel(modelURL);
                console.log("Model loaded successfully!");

                // Set up file input listener
                const fileInput = document.getElementById("file-input");
                fileInput.addEventListener("change", handleFileUpload, false);
            }} catch (error) {{
                console.error("Error loading model:", error);
                const labelContainer = document.getElementById("label-container");
                labelContainer.innerHTML = `<div style="color: red;">Error loading model: ${{error.message}}</div>`;
            }}
        }}

        // Handle file upload
        async function handleFileUpload(event) {{
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

            // Wait for the image to load before making predictions
            img.onload = async () => {{
                console.log("Image loaded, making predictions...");

                // Preprocess the image
                const tensor = tf.browser.fromPixels(img)
                    .resizeNearestNeighbor([224, 224]) // Resize to 224x224
                    .toFloat() // Convert to float
                    .div(tf.scalar(255)) // Normalize to [0, 1]
                    .expandDims(); // Add batch dimension

                // Make predictions
                await predict(tensor);
            }};
        }}

        // Make predictions on the uploaded image
        async function predict(tensor) {{
            try {{
                console.log("Predicting...");
                const prediction = await model.predict(tensor);
                console.log("Raw predictions:", prediction);

                // Log the probabilities for each class
                const probabilities = await prediction.data();
                console.log("Probabilities:", probabilities);

                // Get the predicted class
                const predictedClass = tf.argMax(prediction, 1).dataSync()[0];
                const confidence = tf.max(prediction).dataSync()[0];

                // Get the class label
                const className = classLabels[predictedClass] || "Unknown Class";

                // Log the results
                console.log(`Predicted Class: ${{className}}, Confidence: ${{confidence}}`);

                // Determine if stagnant water is detected
                const hasStagnantWater = predictedClass === 1 || predictedClass === 2;

                // Display the results
                const labelContainer = document.getElementById("label-container");
                labelContainer.innerHTML = `
                    <div style="margin-bottom: 10px;">
                        <span style="font-weight: bold; color: var(--text-color);">Predicted Class:</span>
                        <span style="color: ${{hasStagnantWater ? "red" : "green"}};">${{className}}</span>
                    </div>
                    <div style="margin-bottom: 10px;">
                        <span style="font-weight: bold; color: var(--text-color);">Confidence:</span>
                        <span style="color: ${{hasStagnantWater ? "red" : "green"}};">${{confidence.toFixed(2)}}</span>
                    </div>
                `;

                // Send results back to Streamlit
                if (typeof Streamlit !== "undefined" && Streamlit.setComponentValue) {{
                    Streamlit.setComponentValue({{
                        predicted_class: className,
                        confidence: confidence,
                        has_stagnant_water: hasStagnantWater
                    }});
                }} else {{
                    console.error("Streamlit API not available.");
                }}

                console.log("Predictions completed!");
            }} catch (error) {{
                console.error("Error making predictions:", error);
                const labelContainer = document.getElementById("label-container");
                labelContainer.innerHTML = `<div style="color: red;">Error making predictions: ${{error.message}}</div>`;
            }}
        }}

        // Initialize the model
        init();
    </script>
    <style>
        :root {{
            --text-color: black;
            --background-color: white;
        }}
        @media (prefers-color-scheme: dark) {{
            :root {{
                --text-color: white;
                --background-color: #1e1e1e;
            }}
        }}
    </style>
    """

    # Render the HTML/JavaScript code
    components.html(html_code, height=500)

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
    result = teachable_machine_component(class_labels)

    # Display predictions dynamically
    if result:
        st.subheader("Prediction Results")
        st.write(f"🎉 Predicted Class: **{result['predicted_class']}** with {result['confidence']:.2f} confidence!")
        if result["has_stagnant_water"]:
            st.error("⚠️ Stagnant water detected! This is a potential dengue breeding site. Please take action.")
        else:
            st.success("✅ No stagnant water detected. Low dengue risk.")

if __name__ == "__main__":
    main()
