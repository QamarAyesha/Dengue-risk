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
This application utilizes AI and geospatial technologies to predict and prevent dengue outbreaks, offering actionable insights to safeguard vulnerable communities.
""")

# Page title and introduction
st.title("🌍 AI-Driven Dengue Prevention System")
st.markdown("""
### How might we predict and prevent outbreaks of infectious diseases in vulnerable communities?
This app leverages **AI-driven predictive analytics** and **geospatial technologies** to identify, forecast, and mitigate the risks of infectious disease outbreaks, such as dengue, malaria, and chikungunya, in vulnerable regions.
""")

# Define pages with their thumbnails and descriptions
pages = [
    {
        "title": "Dengue Risk Map",
        "path": "/Dengue_Risk_Map",
        "thumbnail": "images/maps_12785933(1).png",  # Local image path
        "description": "Analyze dengue risk with a heatmap."
    },
    {
        "title": "Fumigation Progress",
        "path": "/Fumigation_Progress",
        "thumbnail": "images/business_15843486.png",  # Local image path
        "description": "Displays progress of fumigation by government staff."
    },
    {
        "title": "Reported Cases",
        "path": "/Reported_Cases",
        "thumbnail": "images/megaphone_6808568.png",  # Local image path
        "description": "Visualize historically reported cases."
    },
    {
        "title": "Environmental Factors",
        "path": "/Environmental_Factors",
        "thumbnail": "images/environmental_factors.png",  # Local image path
        "description": "Analyze weather and environmental risks."
    },
    {
        "title": "Stagnant Water",
        "path": "/Stagnant_Water",
        "thumbnail": "images/stagnant_water.png",  # Local image path
        "description": "Satellite-based analysis of stagnant water and associated risk."
    },
    {
        "title": "Guidelines",
        "path": "/Guidelines",
        "thumbnail": "images/guidelines.png",  # Local image path
        "description": "Prevention and Awareness."
    }
]

# Cards with Page Thumbnails in Multi-Column Layout
st.header("Explore the App")

# Add custom CSS for card styling
st.markdown("""
<style>
.card-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;  /* Space between cards */
    justify-content: space-between;
}
.card {
    border: 1px solid #e1e4e8;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: transform 0.2s, box-shadow 0.2s;
    flex: 1 1 calc(33.333% - 20px);  /* Three cards per row with spacing */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;  /* Center content horizontally */
    min-height: 300px;  /* Ensure all cards have the same height */
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

# Create a container for the cards
st.markdown('<div class="card-container">', unsafe_allow_html=True)

# Loop through pages and create cards
for page in pages:
    st.markdown(f"""
    <a href="{page['path']}" target="_self" style="text-decoration: none; color: inherit;">
        <div class="card">
            <img src="{page['thumbnail']}" alt="{page['title']}">
            <h3>{page['title']}</h3>
            <p>{page['description']}</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Close the container
st.markdown('</div>', unsafe_allow_html=True)

# Custom CSS for key feature boxes
st.markdown("""
<style>
.key-feature-box {
    background-color: rgba(70, 130, 180, 0.5); /* darker blue with some opacity */
    padding: 20px;
    border-radius: 10px;
    min-height: 200px;  /* Ensures each box has the same height */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

ul {
    margin: 0;
    padding-left: 20px;
}

li {
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Key Features section
st.header("Key Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="key-feature-box">
            <strong>Real-Time Risk Mapping</strong>  
            <ul>
                <li>Visualize disease risk zones using satellite and drone imagery.</li>
                <li>Identify stagnant water sources and mosquito breeding grounds.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="key-feature-box">
            <strong>Predictive Analytics</strong>  
            <ul>
                <li>Forecast outbreaks using environmental data (rainfall, temperature, humidity).</li>
                <li>AI models trained on historical outbreak data.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="key-feature-box">
            <strong>Community Alerts</strong>  
            <ul>
                <li>Send real-time alerts via SMS and WhatsApp.</li>
                <li>Engage communities in reporting and prevention efforts.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Call-to-action section
st.header("Get Started")
st.markdown("""
Explore the tools and features of this app to understand how AI and geospatial technologies can help prevent infectious disease outbreaks.  
👇 **Select a page from the sidebar** or click on the cards above to get started!
""")

# Footer
st.markdown("---")
st.markdown("""
**Disclaimer**: This app is a prototype designed for educational and demonstration purposes.  
**Contact**: For inquiries, please email [support@example.com](mailto:support@example.com).
""")
