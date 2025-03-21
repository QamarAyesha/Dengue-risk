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
st.sidebar.image(logo, use_column_width=True)

# Page title and introduction
st.title("🌍 AI-Driven Dengue Prevention System")
st.markdown("""
### How might we predict and prevent outbreaks of infectious diseases in vulnerable communities?
This app leverages **AI-driven predictive analytics** and **geospatial technologies** to identify, forecast, and mitigate the risks of infectious disease outbreaks, such as dengue, malaria, and chikungunya, in vulnerable regions.
""")

# Linked images for navigation
st.header("Explore the App")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <a href="/Risk_Mapping" target="_self">
        <img src="https://via.placeholder.com/150x100.png?text=Risk+Mapping" width="100%">
    </a>
    """, unsafe_allow_html=True)
    st.markdown("**🌐 Risk Mapping**")

with col2:
    st.markdown("""
    <a href="/Predictive_Analytics" target="_self">
        <img src="https://via.placeholder.com/150x100.png?text=Predictive+Analytics" width="100%">
    </a>
    """, unsafe_allow_html=True)
    st.markdown("**📊 Predictive Analytics**")

with col3:
    st.markdown("""
    <a href="/Community_Alerts" target="_self">
        <img src="https://via.placeholder.com/150x100.png?text=Community+Alerts" width="100%">
    </a>
    """, unsafe_allow_html=True)
    st.markdown("**🚨 Community Alerts**")

with col4:
    st.markdown("""
    <a href="/Government_Dashboard" target="_self">
        <img src="https://via.placeholder.com/150x100.png?text=Government+Dashboard" width="100%">
    </a>
    """, unsafe_allow_html=True)
    st.markdown("**📈 Government Dashboard**")

# Key features section
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
👇 **Select a page from the sidebar** or click on the images above to get started!
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
