import streamlit as st

st.set_page_config(layout="wide")
st.title("Dengue Prevention and Awareness")

st.markdown(
    """
    Learn how to protect yourself and your community from dengue. Explore preventive measures, identify symptoms, and uncover the facts.
    """
)

# Symptom Checker
st.header("🩺 Symptom Checker")
symptoms = ["Fever", "Headache", "Muscle Pain", "Fatigue", "Nausea", "Skin Rash"]
selected_symptoms = st.multiselect("Select your symptoms", symptoms)

if selected_symptoms:
    st.write("Based on your symptoms, it is recommended to:")
    if "Fever" in selected_symptoms and "Muscle Pain" in selected_symptoms:
        st.write("- Stay hydrated and monitor your temperature.")
        st.write("- Consult a healthcare provider if the fever persists.")
    else:
        st.write("- Rest, drink fluids, and monitor symptoms.")
        st.write("- Seek medical advice if symptoms worsen.")

# Preventive Tips
st.header("🛡️ Preventive Measures")
tips_category = st.radio("Choose a category to get tips:", ["At Home", "Outdoors", "Community Action"])

if tips_category == "At Home":
    st.write("- Empty standing water from containers.")
    st.write("- Keep windows and doors closed or use screens.")
elif tips_category == "Outdoors":
    st.write("- Wear long-sleeved clothing.")
    st.write("- Apply mosquito repellent.")
elif tips_category == "Community Action":
    st.write("- Organize cleanup drives to remove mosquito breeding sites.")
    st.write("- Encourage proper waste management.")

# Myth Buster
st.header("❗ Myth Buster")
myths = {
    "Dengue only spreads in dirty water": "Mosquitoes can breed in clean, stagnant water.",
    "Only rural areas are at risk": "Urban areas with poor drainage are also prone to dengue outbreaks.",
    "Dengue is contagious between people": "Dengue spreads through mosquito bites, not person-to-person contact."
}

selected_myth = st.selectbox("Select a myth to uncover the fact:", list(myths.keys()))
st.write(f"**Fact:** {myths[selected_myth]}")

st.write("Stay informed and stay safe!")
