import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/QamarAyesha/test-data/refs/heads/main/lahore_dengue_data.csv')

# Dropdown for risk factor selection with Overall Risk as default
risk_options = {
    'Overall Risk': 'Total_Risk_Score',
    'Weather Risk': 'Weather_Risk_Score',
    'Water Coverage Risk': 'Water_Coverage_Risk_Score',
    'Past Cases Risk': 'Past_Cases_Risk_Score'
}
selected_risk = st.sidebar.selectbox("Select Risk Factor for Heatmap", list(risk_options.keys()), index=0)

# Initialize Leafmap
m = leafmap.Map(center=[31.5204, 74.3587], zoom=12)
m.add_basemap('CartoDB.Positron')

# Add heatmap layer
m.add_heatmap(
    data=df,
    latitude="Latitude",
    longitude="Longitude",
    value=risk_options[selected_risk],
    name=f"{selected_risk} Heatmap",
    radius=25,
)

# Add legend with colors representing risk levels
legend_dict = {
    "Low Risk": "#00FF00",
    "Moderate Risk": "#FFFF00",
    "High Risk": "#FFA500",
    "Severe Risk": "#FF0000",
}
m.add_legend(title="Risk Level", legend_dict=legend_dict)

st.title("Dengue Risk Heatmap")
st.write("Visualizing dengue risk factors across Lahore.")

m.to_streamlit(height=600)  # Display map in Streamlit
