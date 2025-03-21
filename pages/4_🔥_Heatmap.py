import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title("Dengue Risk Heatmap for Lahore")

st.markdown(
    """
This map visualizes dengue risk levels across Lahore, highlighting areas with varying degrees of risk.
You can explore the impact of specific factors—such as weather conditions, stagnant water coverage, or historical dengue cases—on the overall risk assessment.
The default view displays the comprehensive risk score, which combines multiple factors to provide a holistic understanding of dengue risk in the region."
    """
)

# Load data
data = pd.read_csv('dengue_data.csv')

# Dropdown for factor selection
factor_options = [
    'Overall Risk': 'Total_Risk_Score',
    'Weather': 'Weather_Risk_Score',
    'Stagnant water': 'Water_Coverage_Risk_Score',
    'Past Cases': 'Past_Cases_Risk_Score'
]
factor = st.selectbox("Select Risk Factor to Display", factor_options, index=0)

# Create map
m = leafmap.Map(center=[31.5204, 74.3587], zoom=12)
m.add_heatmap(
    data,
    latitude="Latitude",
    longitude="Longitude",
    value=factor,
    name="Heatmap",
    radius=20,
)
m.to_streamlit(height=700)

# Color key explanation
st.markdown(
    """
    <div style="background-color: #1e1e1e; padding: 10px; border-radius: 10px; color: #ffffff;">
    <h4>Color Key Explanation</h4>
    <ul>
      <li><span style="color: #ff0000;">Red</span>: High Risk</li>
      <li><span style="color: #ffa500;">Orange</span>: Moderate Risk</li>
      <li><span style="color: #ffff00;">Yellow</span>: Low Risk</li>
      <li><span style="color: #00ff00;">Green</span>: Minimal Risk</li>
    </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("Data Source: Dengue Surveillance Data")

