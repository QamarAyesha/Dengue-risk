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

# City Selector
selected_city = st.selectbox('Select a city to view progress:', data['City'])

# Display City Progress
city_data = data[data['City'] == selected_city]
st.metric(label='Fumigation Progress', value=f"{city_data['Progress (%)'].values[0]}%")
st.write(f"Estimated Completion: {city_data['Estimated Completion (Days)'].values[0]} days")

# Map Visualization
st.write("### City Progress Overview")
fig = px.scatter_mapbox(
    data, lat='Latitude', lon='Longitude', size='Progress (%)',
    color='Progress (%)', hover_name='City', zoom=5,
    mapbox_style='carto-positron', color_continuous_scale='Blues'
)
st.plotly_chart(fig, use_container_width=True)

# Progress Timeline with Fixed Scaling
st.write("### Estimated Fumigation Progress Over Time")

# Get the estimated completion days for the selected city
estimated_completion_days = city_data['Estimated Completion (Days)'].values[0]
initial_progress = city_data['Progress (%)'].values[0] / 100  # Normalize to [0, 1]

timeline_data = pd.DataFrame({
    'Day': range(1, estimated_completion_days + 1),
    'Progress (%)': [initial_progress * (day / estimated_completion_days) for day in range(1, estimated_completion_days + 1)]
})


# Plotting the timeline with fixed progress
fig_timeline = px.line(
    timeline_data, x='Day', y='Progress (%)',
    title=f'Progress Timeline for {selected_city}',
    markers=True, line_shape='spline'  # Smooth curve
)

# Format the Y-axis to show percentage format
fig_timeline.update_layout(
    yaxis=dict(
        tickformat=".0%",  # Show as percentages
        range=[0, 1]  # Set Y-axis range to [0, 1] for percentages
    )
)



fig_timeline.add_annotation(
    x=estimated_completion_days, y=initial_progress,
    text="Completion", showarrow=True, arrowhead=1
)

# Display the timeline plot
st.plotly_chart(fig_timeline, use_container_width=True)

# Feedback Form
st.write("### Provide Feedback")
feedback = st.text_area('Do you have any concerns or suggestions about the fumigation process?')
if st.button('Submit Feedback'):
    st.success('Thank you for your feedback!')

st.write("Stay informed and help keep your city safe from dengue.")


