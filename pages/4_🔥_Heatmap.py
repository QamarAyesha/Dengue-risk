import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title("Dengue Risk Heatmap for Lahore")

st.markdown(
    """
A comprehensive visualization of dengue risk levels, indicating areas with varying degrees of risk. The map illustrates the influence of specific factors, including weather conditions, stagnant water coverage, and historical dengue cases, on the overall risk assessment.
    """
)

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
col1, col2 = st.columns([4, 1])

with col1:
    # Create map
    m = leafmap.Map(center=[31.5204, 74.3587], zoom=12)
    m.add_heatmap(
        data,
        latitude="Latitude",
        longitude="Longitude",
        value=selected_factor,
        name="Heatmap",
        radius=20,
    )
    m.to_streamlit(height=700)

with col2:
    # Color key explanation using gradient bar
    st.markdown(
        """
        **Color Key Explanation:**
        <div style="background: linear-gradient(to bottom, #0000FF, #00FF00, #FFFF00, #FFA500, #FF0000); height: 300px; width: 30px; border-radius: 8px; margin-top: 20px;">
        </div>
        <div style="display: flex; flex-direction: column; justify-content: space-between; height: 300px;">
            <span style="color: #0000FF;">Very Low Risk</span>
            <span style="color: #00FF00;">Minimal Risk</span>
            <span style="color: #FFFF00;">Low Risk</span>
            <span style="color: #FFA500;">Moderate Risk</span>
            <span style="color: #FF0000;">High Risk</span>
        </div>
        """,
        unsafe_allow_html=True
    )



