import streamlit as st
import streamlit.components.v1 as components

# Teachable Machine TensorFlow.js Integration
def teachable_machine_component():
    components.html(
        """
        <div>Teachable Machine Image Model</div>
        <button type="button" onclick="init()">Start</button>
        <div id="webcam-container"></div>
        <div id="label-container"></div>
        <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest/dist/teachablemachine-image.min.js"></script>
        <script type="text/javascript">
            const URL = "https://teachablemachine.withgoogle.com/models/jtmut1SnG/";

            let model, webcam, labelContainer, maxPredictions;

            async function init() {
                const modelURL = URL + "model.json";
                const metadataURL = URL + "metadata.json";

                model = await tmImage.load(modelURL, metadataURL);
                maxPredictions = model.getTotalClasses();

                const flip = true;
                webcam = new tmImage.Webcam(200, 200, flip);
                await webcam.setup();
                await webcam.play();
                window.requestAnimationFrame(loop);

                document.getElementById("webcam-container").appendChild(webcam.canvas);
                labelContainer = document.getElementById("label-container");
                for (let i = 0; i < maxPredictions; i++) {
                    labelContainer.appendChild(document.createElement("div"));
                }
            }

            async function loop() {
                webcam.update();
                await predict();
                window.requestAnimationFrame(loop);
            }

            async function predict() {
                const prediction = await model.predict(webcam.canvas);
                for (let i = 0; i < maxPredictions; i++) {
                    const classPrediction =
                        prediction[i].className + ": " + prediction[i].probability.toFixed(2);
                    labelContainer.childNodes[i].innerHTML = classPrediction;
                }
            }
        </script>
        """,
        height=500,
    )

# Streamlit App
def main():
    st.set_page_config(page_title="Satellite Image Analysis for Dengue Risk", layout="wide")
    st.title("Satellite Image Analysis for Dengue Risk")
    st.write("Upload or select satellite images to detect stagnant water spots.")

    # Add Teachable Machine Component
    st.subheader("Teachable Machine Model")
    teachable_machine_component()

if __name__ == "__main__":
    main()
