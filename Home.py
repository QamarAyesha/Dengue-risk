import streamlit as st
import leafmap.foliumap as leafmap

# Set page configuration
st.set_page_config(
    page_title="AI-Driven Dengue Prevention System",
    layout="wide",
    page_icon="🌍"
)

# Customize the sidebar
st.sidebar.title("About")
st.sidebar.info("""
**UN SDG 3 — Good Health and Well-being**  
This app aims to predict and prevent outbreaks of infectious diseases in vulnerable communities using AI and geospatial technologies.
""")
logo = "https://i.imgur.com/UbOXYAU.png"  # Replace with your logo URL
st.sidebar.image(logo, use_container_width=True)

# Page title and introduction
st.title("🌍 AI-Driven Dengue Prevention System")
st.markdown("""
### How might we predict and prevent outbreaks of infectious diseases in vulnerable communities?
This app leverages **AI-driven predictive analytics** and **geospatial technologies** to identify, forecast, and mitigate the risks of infectious disease outbreaks, such as dengue, malaria, and chikungunya, in vulnerable regions.
""")

# Define pages with their thumbnails and descriptions
pages = [
    {
        "title": "Interactive Map",
        "path": "/Interactive_Map",
        "thumbnail": "https://via.placeholder.com/300x150.png?text=Interactive+Map",
        "description": "Explore an interactive map with real-time data."
    },
    {
        "title": "Fumigation Progress",
        "path": "/Fumigation Progress",
        "thumbnail": "https://via.placeholder.com/300x150.png?text=Split+Map",
        "description": "Displays progress of fumigation by government staff"
    },
    {
        "title": "Marker Cluster",
        "path": "/Marker_Cluster",
        "thumbnail": "https://via.placeholder.com/300x150.png?text=Marker+Cluster",
        "description": "Visualize clustered markers on a map."
    },
    {
        "title": "Heatmap",
        "path": "/Heatmap",
        "thumbnail": "https://via.placeholder.com/300x150.png?text=Heatmap",
        "description": "Analyze data density with a heatmap."
    },
    {
        "title": "Basemaps",
        "path": "/Basemaps",
        "thumbnail": "https://via.placeholder.com/300x150.png?text=Basemaps",
        "description": "Switch between different basemaps."
    },
    {
        "title": "Web Map Service",
        "path": "/Web_Map_Service",
        "thumbnail": "https://via.placeholder.com/300x150.png?text=Web+Map+Service",
        "description": "Integrate WMS layers into the map."
    }
]

# Cards with Page Thumbnails in Multi-Column Layout
st.header("Explore the App")
cols = st.columns(4)  # Adjust the number of columns as needed

# Add custom CSS for card styling
st.markdown("""
<style>
.card {
    border: 1px solid #e1e4e8;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: transform 0.2s, box-shadow 0.2s;
    height: 100%;  /* Ensure all cards have the same height */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
.card img {
    width: 100%;
    border-radius: 5px;
    margin-bottom: 15px;
}
.card h3 {
    font-size: 1.25rem;
    margin: 10px 0;
}
.card p {
    font-size: 0.9rem;
    color: #555;
    margin: 0;
}
</style>
""", unsafe_allow_html=True)

# Loop through pages and create cards
for i, page in enumerate(pages):
    with cols[i % 4]:  # Distribute cards across 4 columns
        st.markdown(f"""
        <a href="{page['path']}" target="_self" style="text-decoration: none; color: inherit;">
            <div class="card">
                <img src="{page['thumbnail']}" alt="{page['title']}">
                <h3>{page['title']}</h3>
                <p>{page['description']}</p>
            </div>
        </a>
        """, unsafe_allow_html=True)

# Key features section (unchanged)
st.header("Key Features")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    **🌐 Real-Time Risk Mapping**  
    - Visualize disease risk zones using satellite and drone imagery.  
    - Identify stagnant water sources and mosquito breeding grounds.  
    """)
with col2:
    st.markdown("""
    **📊 Predictive Analytics**  
    - Forecast outbreaks using environmental data (rainfall, temperature, humidity).  
    - AI models trained on historical outbreak data.  
    """)
with col3:
    st.markdown("""
    **🚨 Community Alerts**  
    - Send real-time alerts via SMS and WhatsApp.  
    - Engage communities in reporting and prevention efforts.  
    """)

# Call-to-action section
st.header("Get Started")
st.markdown("""
Explore the tools and features of this app to understand how AI and geospatial technologies can help prevent infectious disease outbreaks.  
👇 **Select a page from the sidebar** or click on the cards above to get started!
""")

# Add a map for visualization
st.header("Global Disease Risk Map")
m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)

# Footer
st.markdown("---")
st.markdown("""
**Disclaimer**: This app is a prototype designed for educational and demonstration purposes.  
**Contact**: For inquiries, please email [support@example.com](mailto:support@example.com).
""")
