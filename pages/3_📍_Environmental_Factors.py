import streamlit as st
import numpy as np
import pandas as pd

# Initialize session state to store results
if "last_predictions" not in st.session_state:
    st.session_state.last_predictions = []

# Placeholder for model loading
def load_model(model_path):
    st.info("The model is being loaded. Please wait...")
    # Simulate a delay for loading
    st.spinner("Loading model...")
    return None

# Placeholder for prediction
def predict_risk(model, input_data):
    st.info("Predicting risk based on environmental data...")
    # Simulate a delay for prediction
    st.spinner("Analyzing data...")
    # Return random risk level (0 = Low, 1 = Medium, 2 = High)
    return np.random.randint(0, 3)

# Streamlit page
def main():
    st.title("📊 Predictive Analytics Using Environmental Data")
    st.write("Use rainfall, temperature, humidity, and vegetation data to predict mosquito breeding conditions and dengue risk for specific areas in Lahore.")

    # Explanation of the model
    st.markdown("""
    ### How the Model Works
    This predictive model uses **environmental data** to assess the risk of dengue outbreaks in specific areas of Lahore. The model analyzes the following factors:
    - **Rainfall**: Stagnant water from rainfall is a breeding ground for mosquitoes.
    - **Temperature**: Higher temperatures accelerate mosquito breeding cycles.
    - **Humidity**: High humidity levels create favorable conditions for mosquito survival.
    - **Vegetation Index (NDVI)**: Dense vegetation can provide breeding sites for mosquitoes.

    Based on these inputs, the model predicts the **risk level** (Low, Medium, or High) and suggests **intervention strategies**.
    """)

    # Placeholder for model path
    model_path = "model/environmental_model.h5"  # Replace with the path to your model later
    model = load_model(model_path)

    # Location selection (Lahore neighborhoods)
    st.subheader("Select Location in Lahore")
    location = st.selectbox(
        "Choose a neighborhood in Lahore",
        [
            "Gulberg", "Defence", "Model Town", "Johar Town", "Faisal Town",
            "Cantt", "Iqbal Town", "Garden Town", "Wapda Town", "DHA"
        ],  # Add more neighborhoods as needed
        index=0,  # Default to Gulberg
        help="Select the neighborhood in Lahore for which you want to predict dengue risk."
    )

    # Input fields for environmental data
    st.subheader("Enter Environmental Data")
    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=50.0,
        help="Enter the amount of rainfall in millimeters. Higher rainfall increases the risk of stagnant water."
    )
    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        value=25.0,
        help="Enter the average temperature in Celsius. Higher temperatures accelerate mosquito breeding."
    )
    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        help="Enter the relative humidity percentage. High humidity favors mosquito survival."
    )
    vegetation = st.number_input(
        "Vegetation Index (NDVI)",
        min_value=-1.0,
        max_value=1.0,
        value=0.5,
        help="Enter the Normalized Difference Vegetation Index (NDVI). Dense vegetation can provide breeding sites."
    )

    # Predict button
    if st.button("Predict Risk", help="Click to predict the dengue risk based on the entered data."):
        # Prepare input data
        input_data = np.array([[rainfall, temperature, humidity, vegetation]])

        # Predict risk level (placeholder)
        risk_level = predict_risk(model, input_data)

        # Map risk level to text
        risk_levels = ["Low", "Medium", "High"]
        risk_text = risk_levels[risk_level]

        # Suggested intervention strategies
        interventions = {
            "Low": "No immediate action required. Monitor conditions regularly.",
            "Medium": "Increase surveillance and public awareness. Remove stagnant water sources.",
            "High": "Implement emergency measures. Conduct fogging and distribute mosquito nets."
        }
        intervention = interventions[risk_text]

        # Store results in session state
        result = {
            "location": location,
            "rainfall": rainfall,
            "temperature": temperature,
            "humidity": humidity,
            "vegetation": vegetation,
            "risk_level": risk_text,
            "intervention": intervention
        }
        st.session_state.last_predictions.append(result)

    # Display last predictions
    st.subheader("Dynamic Risk Dashboard")
    if st.session_state.last_predictions:
        st.write("### Latest Predictions")
        for i, result in enumerate(st.session_state.last_predictions[::-1]):  # Show latest first
            st.write(f"#### Prediction {i + 1}")
            st.write(f"- **Location**: {result['location']}, Lahore")
            st.write(f"- **Rainfall**: {result['rainfall']} mm")
            st.write(f"- **Temperature**: {result['temperature']} °C")
            st.write(f"- **Humidity**: {result['humidity']}%")
            st.write(f"- **Vegetation Index**: {result['vegetation']}")
            st.write(f"- **Risk Level**: **{result['risk_level']}**")
            st.write(f"- **Intervention Strategy**: {result['intervention']}")
            st.write("---")
    else:
        st.info("No predictions yet. Enter environmental data and click 'Predict Risk' to see results.")

if __name__ == "__main__":
    main()
