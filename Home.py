import streamlit as st
import leafmap.foliumap as leafmap

# Set page configuration
st.set_page_config(
    page_title="AI-Driven Dengue Prevention System",
    layout="wide",
    page_icon="🦟"
)

# Customize the sidebar
st.sidebar.title("About")
st.sidebar.info("""
**AI-Driven Dengue Prevention System**  
This app aims to predict and prevent dengue outbreaks in vulnerable communities using AI and geospatial technologies.
""")
logo = "https://i.imgur.com/UbOXYAU.png"  # Replace with your logo URL
st.sidebar.image(logo, use_container_width=True)

# Page title and introduction
st.title("🦟 AI-Driven Dengue Prevention System")
st.markdown("""
### How might we predict and prevent dengue outbreaks in vulnerable communities?
This app leverages **AI-driven predictive analytics** and **geospatial technologies** to identify, forecast, and mitigate the risks of dengue outbreaks in vulnerable regions.
""")

# Section 1: Buttons with Icons
st.header("1. Buttons with Icons")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🌐 Risk Mapping"):
        st.switch_page("/pages/Risk_Mapping.py")  # Replace with your page path
    st.markdown("Visualize disease risk zones using satellite and drone imagery.")

with col2:
    if st.button("📊 Predictive Analytics"):
        st.switch_page("/pages/Predictive_Analytics.py")  # Replace with your page path
    st.markdown("Forecast outbreaks using environmental data and AI models.")

with col3:
    if st.button("🚨 Community Alerts"):
        st.switch_page("/pages/Community_Alerts.py")  # Replace with your page path
    st.markdown("Send real-time alerts via SMS and WhatsApp.")

with col4:
    if st.button("📈 Government Dashboard"):
        st.switch_page("/pages/Government_Dashboard.py")  # Replace with your page path
    st.markdown("View dengue risk maps and fumigation efforts.")

# Section 2: Markdown Links with Emojis
st.header("2. Markdown Links with Emojis")
st.markdown("""
- [🌐 Risk Mapping](/Risk_Mapping)  
  Visualize disease risk zones using satellite and drone imagery.  
- [📊 Predictive Analytics](/Predictive_Analytics)  
  Forecast outbreaks using environmental data and AI models.  
- [🚨 Community Alerts](/Community_Alerts)  
  Send real-time alerts via SMS and WhatsApp.  
- [📈 Government Dashboard](/Government_Dashboard)  
  View dengue risk maps and fumigation efforts.  
""")

# Section 3: Cards with Expanders
st.header("3. Cards with Expanders")
with st.expander("🌐 Risk Mapping"):
    st.markdown("""
    Visualize disease risk zones using satellite and drone imagery.  
    [Go to Risk Mapping](/Risk_Mapping)  
    """)
with st.expander("📊 Predictive Analytics"):
    st.markdown("""
    Forecast outbreaks using environmental data and AI models.  
    [Go to Predictive Analytics](/Predictive_Analytics)  
    """)
with st.expander("🚨 Community Alerts"):
    st.markdown("""
    Send real-time alerts via SMS and WhatsApp.  
    [Go to Community Alerts](/Community_Alerts)  
    """)
with st.expander("📈 Government Dashboard"):
    st.markdown("""
    View dengue risk maps and fumigation efforts.  
    [Go to Government Dashboard](/Government_Dashboard)  
    """)

# Section 4: Columns with Text Links
st.header("4. Columns with Text Links")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    **🌐 Risk Mapping**  
    [Explore Risk Mapping](/Risk_Mapping)  
    """)
with col2:
    st.markdown("""
    **📊 Predictive Analytics**  
    [Explore Predictive Analytics](/Predictive_Analytics)  
    """)
with col3:
    st.markdown("""
    **🚨 Community Alerts**  
    [Explore Community Alerts](/Community_Alerts)  
    """)
with col4:
    st.markdown("""
    **📈 Government Dashboard**  
    [Explore Government Dashboard](/Government_Dashboard)  
    """)

# Section 5: Custom HTML and CSS (Advanced)
st.header("5. Custom HTML and CSS (Advanced)")
st.markdown("""
<style>
.card {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    width: 100%;
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
}
.card:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
</style>
<div class="card">
    <a href="/Risk_Mapping" target="_self" style="text-decoration: none; color: inherit;">
        <h3>🌐 Risk Mapping</h3>
        <p>Visualize disease risk zones using satellite and drone imagery.</p>
    </a>
</div>
<div class="card">
    <a href="/Predictive_Analytics" target="_self" style="text-decoration: none; color: inherit;">
        <h3>📊 Predictive Analytics</h3>
        <p>Forecast outbreaks using environmental data and AI models.</p>
    </a>
</div>
<div class="card">
    <a href="/Community_Alerts" target="_self" style="text-decoration: none; color: inherit;">
        <h3>🚨 Community Alerts</h3>
        <p>Send real-time alerts via SMS and WhatsApp.</p>
    </a>
</div>
<div class="card">
    <a href="/Government_Dashboard" target="_self" style="text-decoration: none; color: inherit;">
        <h3>📈 Government Dashboard</h3>
        <p>View dengue risk maps and fumigation efforts.</p>
    </a>
</div>
""", unsafe_allow_html=True)

# Add a map for visualization
st.header("Dengue Risk Map")
m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)

# Footer
st.markdown("---")
st.markdown("""
**Disclaimer**: This app is a prototype designed for educational and demonstration purposes.  
**Contact**: For inquiries, please email [support@example.com](mailto:support@example.com).
""")
