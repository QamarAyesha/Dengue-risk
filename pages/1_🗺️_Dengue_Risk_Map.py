import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title("Dengue Risk Heatmap")

# Custom CSS to add a translucent blue background to the markdown
st.markdown("""
    <style>
        .translucent-blue-box {
            background-color: rgba(70, 130, 180, 0.5); /* Translucent blue with opacity */
            padding: 20px;
            border-radius: 10px;
            min-height: 150px;  /* You can adjust this value as needed */
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Apply the class to the markdown text
st.markdown("""
    <div class="translucent-blue-box">
        <p>A comprehensive visualization of dengue risk levels, indicating areas with varying degrees of risk. The map illustrates the influence of specific factors, including weather conditions, stagnant water coverage, and historical dengue cases, on the overall risk assessment.</p>
    </div>
""", unsafe_allow_html=True)

# Load data
data = pd.read_csv('https://raw.githubusercontent.com/QamarAyesha/test-data/refs/heads/main/lahore_dengue_data.csv')

# Dropdown for factor selection
factor_mapping = {
    'Overall Risk': 'Total_Risk_Score',
    'Weather': 'Weather_Risk_Score',
    'Stagnant water': 'Water_Coverage_Risk_Score',
    'Past Cases': 'Past_Cases_Risk_Score'
}
factor_label = st.selectbox("Select Risk Factor to Display", list(factor_mapping.keys()), index=0)
factor = factor_mapping[factor_label]


# Create layout
col1, col2 = st.columns([6, 1])

with col1:
    # Create map
    m = leafmap.Map(center=[31.5204, 74.3587], zoom=12)
    m.add_heatmap(
        data,
        latitude="Latitude",
        longitude="Longitude",
        value= factor,
        name="Heatmap",
        radius=20,
    )
    m.to_streamlit(height=700)

with col2:

    # Color key explanation using gradient bar
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; justify-content: space-between; align-items: center; height: 320px;">
            <span style="font-family: Arial, sans-serif; font-size: 10px;">Low</span>
            <div style="background: linear-gradient(to bottom, #0000FF, #00FF00, #FFFF00, #FFA500, #FF0000); height: 300px; width: 20px; border-radius: 0px;"></div>
            <span style="font-family: Arial, sans-serif; font-size: 10px;">High</span>
        </div>
        """,
        unsafe_allow_html=True
    )





