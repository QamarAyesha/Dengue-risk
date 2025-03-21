import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import folium
from folium.plugins import HeatMap

st.set_page_config(layout="wide")

st.title("Dengue Risk Heatmap")

# Load your dataset 
df = pd.read_csv('https://raw.githubusercontent.com/QamarAyesha/test-data/refs/heads/main/lahore_dengue_data.csv')

# Dropdown to select factors
factors = ['weather', 'historic_trend', 'water_coverage']
selected_factor = st.selectbox('Select Factor for Heatmap:', factors)

# Map initialization
m = leafmap.Map(center=[31.5204, 74.3587], zoom=11)

# Normalize data for heatmap
if selected_factor in df.columns:
    heat_data = df[['latitude', 'longitude', selected_factor]].dropna().values.tolist()
    HeatMap(heat_data, radius=20, blur=15, max_zoom=1).add_to(m)

# Add a legend to the map
def add_legend(map_object, title, colors, labels):
    legend_html = '<div style="position: fixed; bottom: 50px; left: 50px; background-color: white; z-index:9999; padding: 10px; border-radius: 5px;">'
    legend_html += f'<h4>{title}</h4>'
    for color, label in zip(colors, labels):
        legend_html += f'<div><span style="background-color:{color};width:20px;height:20px;display:inline-block;margin-right:10px;"></span>{label}</div>'
    legend_html += '</div>'
    map_object.get_root().html.add_child(folium.Element(legend_html))

# Example color key for risk levels
colors = ['#00FF00', '#FFFF00', '#FFA500', '#FF0000']
labels = ['Low Risk', 'Moderate Risk', 'High Risk', 'Severe Risk']
add_legend(m, 'Dengue Risk Levels', colors, labels)

# Render map to Streamlit
m.to_streamlit(height=700)
