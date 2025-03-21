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
    # Preventive Measures section
    st.header("Preventive Measures")
    st.markdown("""
        <ul>
            <li>Eliminate stagnant water around your home.</li>
            <li>Use mosquito repellents and wear protective clothing.</li>
            <li>Install window and door screens to prevent mosquitoes from entering.</li>
            <li>Participate in community clean-up campaigns.</li>
            <li>Encourage fumigation and larvicide treatments in your neighborhood.</li>
        </ul>
    """, unsafe_allow_html=True)
    
    # Symptom checker
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

# Myth Buster Section with Blue Background
with col2:
    # Custom CSS for Myth Busters background
    st.markdown(""" 
        <style>
            .myth-buster-box {
                background-color: rgba(70, 130, 180, 0.7); /* Translucent blue with opacity */
                padding: 20px;
                border-radius: 10px;
                min-height: 200px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }
        </style>
    """, unsafe_allow_html=True)

    # Myth Busters title
    st.markdown(
        """
        <h3 style='font-size:18px;'>Dengue Myth Busters</h3>
        <p>Discover the truth behind common misconceptions about dengue.</p>
    """,
        unsafe_allow_html=True
    )

    # Wrapping the Myth Busters content inside the blue box
    st.markdown(""" 
        <div class="myth-buster-box">
            <div class="expander">
                <details>
                    <summary>Myth: Dengue only spreads in dirty areas.</summary>
                    Reality: Dengue mosquitoes can breed in clean water as well, such as in containers or flower pots.
                </details>
                <details>
                    <summary>Myth: All mosquitoes transmit dengue.</summary>
                    Reality: Only female Aedes aegypti mosquitoes are responsible for transmitting the dengue virus.
                </details>
                <details>
                    <summary>Myth: Dengue is contagious from person to person.</summary>
                    Reality: Dengue cannot spread directly from one person to another; it is only transmitted through mosquito bites.
                </details>
                <details>
                    <summary>Myth: Mosquitoes only bite during the night.</summary>
                    Reality: Aedes mosquitoes are most active during early morning and late afternoon.
                </details>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.write("Stay informed, stay safe!")



