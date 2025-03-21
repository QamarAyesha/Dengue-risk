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

# Cards in Multi-Column Layout
st.header("Explore the App")
col1, col2, col3, col4 = st.columns(4)

# Card 1: Risk Mapping
with col1:
    st.markdown("""
    <div style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);">
        <h3>🌐 Risk Mapping</h3>
        <p>Visualize disease risk zones using satellite and drone imagery.</p>
        <a href="/Risk_Mapping" target="_self" style="text-decoration: none;">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                Explore
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Card 2: Predictive Analytics
with col2:
    st.markdown("""
    <div style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);">
        <h3>📊 Predictive Analytics</h3>
        <p>Forecast outbreaks using environmental data and AI models.</p>
        <a href="/Predictive_Analytics" target="_self" style="text-decoration: none;">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                Explore
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Card 3: Community Alerts
with col3:
    st.markdown("""
    <div style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);">
        <h3>🚨 Community Alerts</h3>
        <p>Send real-time alerts via SMS and WhatsApp.</p>
        <a href="/Community_Alerts" target="_self" style="text-decoration: none;">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                Explore
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Card 4: Government Dashboard
with col4:
    st.markdown("""
    <div style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);">
        <h3>📈 Government Dashboard</h3>
        <p>View dengue risk maps and fumigation efforts.</p>
        <a href="/Government_Dashboard" target="_self" style="text-decoration: none;">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                Explore
            </button>
        </a>
    </div>
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
