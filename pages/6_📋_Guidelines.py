import streamlit as st

st.set_page_config(layout="wide")

st.title("Guidelines")

# Introduction
st.markdown(
    """
    Learn how to protect yourself and your community from dengue fever. Explore helpful tips, check symptoms, and uncover common misconceptions about dengue.
    """
)

# Create layout
col1, col2 = st.columns([2, 1])

# Preventive Tips Section
with col1:
    st.header("Preventive Measures")
    st.write("Follow these essential measures to reduce the risk of dengue:")
    tips = [
        "Eliminate stagnant water around your home.",
        "Use mosquito repellents and wear protective clothing.",
        "Install window and door screens to prevent mosquitoes from entering.",
        "Participate in community clean-up campaigns.",
        "Encourage fumigation and larvicide treatments in your neighborhood."
    ]
    for tip in tips:
        st.write(f"✔️ {tip}")

# symptom checkker
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

# Myth Buster Section with Accordion UI
with col2:
    st.markdown(
        """
        <h3 style='font-size:18px;'>🧠 Dengue Myth Busters</h3>
        <p>Discover the truth behind common misconceptions about dengue.</p>
        """,
        unsafe_allow_html=True
    )

    with st.expander("Myth: Dengue only spreads in dirty areas."):
        st.write("Reality: Dengue mosquitoes can breed in clean water as well, such as in containers or flower pots.")

    with st.expander("Myth: All mosquitoes transmit dengue."):
        st.write("Reality: Only female Aedes aegypti mosquitoes are responsible for transmitting the dengue virus.")

    with st.expander("Myth: Dengue is contagious from person to person."):
        st.write("Reality: Dengue cannot spread directly from one person to another; it is only transmitted through mosquito bites.")

    with st.expander("Myth: Mosquitoes only bite during the night."):
        st.write("Reality: Aedes mosquitoes are most active during early morning and late afternoon.")


# Footer
st.write("Stay informed, stay safe!")

