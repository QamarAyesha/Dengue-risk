import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(page_title='Fumigation Progress', layout='wide')

st.title('Fumigation Progress')

# Load Data (Sample Data)
data = pd.DataFrame({
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Faisalabad', 'Multan'],
    'Progress (%)': [85, 70, 60, 75, 90],
    'Latitude': [31.5497, 24.8607, 33.6844, 31.4504, 30.1575],
    'Longitude': [74.3436, 67.0011, 73.0479, 73.1350, 71.5249],
    'Estimated Completion (Days)': [5, 12, 15, 8, 3]
})

# Layout
col1, col2 = st.columns([1, 2])

# City Selector and Details
with col1:
    selected_city = st.selectbox('Select a city to view progress', data['City'])
    city_data = data[data['City'] == selected_city]

    # Display City Progress with improved formatting
    st.markdown(f"### {selected_city}")
    st.metric(label='Fumigation Progress', value=f"{city_data['Progress (%)'].values[0]}%")
    st.write(f"**Estimated Completion:** {city_data['Estimated Completion (Days)'].values[0]} days")

# Map Visualization
with col2:
    st.write("### City Progress Overview")
    fig = px.scatter_mapbox(
        data, lat='Latitude', lon='Longitude', size='Progress (%)',
        color='Progress (%)', hover_name='City', zoom=5,
        mapbox_style='carto-positron', color_continuous_scale='Blues'
    )
    st.plotly_chart(fig, use_container_width=True)

# Progress Timeline with Clearer Visualization
st.write("### Estimated Fumigation Progress Over Time")
timeline_data = pd.DataFrame({
    'Day': range(1, 16),
    'Progress (%)': [i * (city_data['Progress (%)'].values[0] / 15) for i in range(1, 16)]
})
fig_timeline = px.line(
    timeline_data, x='Day', y='Progress (%)',
    title=f'Progress Timeline for {selected_city}',
    markers=True, line_shape='linear'
)
fig_timeline.update_layout(yaxis=dict(tickformat=".0%"))
st.plotly_chart(fig_timeline, use_container_width=True)

# Feedback Form
st.write("### Provide Feedback")
feedback = st.text_area('Do you have any concerns or suggestions about the fumigation process?')
if st.button('Submit Feedback'):
    st.success('Thank you for your feedback!')

st.write("Stay informed and help keep your city safe from dengue.")


