import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

# Page Config
st.set_page_config(page_title="Dengue Risk Heatmap", layout="wide")

# Custom CSS for Blue-Themed UI
st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
    }
    .st-emotion-cache-1inwz65 h1, .st-emotion-cache-1inwz65 h2 {
        color: #003366 !important;
    }
    .st-emotion-cache-16txtl3 {
        background-color: #f0f5ff !important;
        border-radius: 10px;
        padding: 20px;
    }
    .stSelectbox label {
        color: #003366 !important;
    }
    .st-emotion-cache-19rxjzo {
        background-color: #e6f0ff;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Dengue Risk Heatmap")

st.markdown(
    """
A comprehensive visualization of dengue risk levels, indicating areas with varying degrees of risk. The map illustrates the influence of specific factors, including weather conditions, stagnant water coverage, and historical dengue cases, on the overall risk assessment.
    """
)

# Load Data
data = pd.read_csv('https://raw.githubusercontent.com/QamarAyesha/test-data/refs/heads/main/lahore_dengue_data.csv')

# Dropdown for Risk Factor Selection
factor_mapping = {
    'Overall Risk': 'Total_Risk_Score',
    'Weather': 'Weather_Risk_Score',
    'Stagnant water': 'Water_Coverage_Risk_Score',
    'Past Cases': 'Past_Cases_Risk_Score'
}
factor_label = st.selectbox("Select Risk Factor to Display:", list(factor_mapping.keys()), index=0)
factor = factor_mapping[factor_label]

# Layout: Map and Color Key
col1, col2 = st.columns([6, 1])

with col1:
    # Display Heatmap
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

with col2:
    # Display Color Key Explanation
    st.markdown(
        """
        <h4 style='text-align: center; color: #003366;'>Risk Level Key</h4>
        <div style="display: flex; flex-direction: column; justify-content: space-between; align-items: center; height: 320px;">
            <span style="font-family: Arial, sans-serif; font-size: 12px; color: #003366;">Low</span>
            <div style="background: linear-gradient(to bottom, #0000FF, #00FF00, #FFFF00, #FFA500, #FF0000); height: 300px; width: 20px; border-radius: 0px;"></div>
            <span style="font-family: Arial, sans-serif; font-size: 12px; color: #003366;">High</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("Stay informed and take preventive measures to reduce dengue risk.")




