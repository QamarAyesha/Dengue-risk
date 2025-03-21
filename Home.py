# Cards in Multi-Column Layout
st.header("Explore the App")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 20px; text-align: center;">
        <h3>🌐 Risk Mapping</h3>
        <p>Visualize disease risk zones using satellite and drone imagery.</p>
        <a href="/Risk_Mapping" target="_self" style="text-decoration: none;">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                Explore
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 20px; text-align: center;">
        <h3>📊 Predictive Analytics</h3>
        <p>Forecast outbreaks using environmental data and AI models.</p>
        <a href="/Predictive_Analytics" target="_self" style="text-decoration: none;">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                Explore
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 20px; text-align: center;">
        <h3>🚨 Community Alerts</h3>
        <p>Send real-time alerts via SMS and WhatsApp.</p>
        <a href="/Community_Alerts" target="_self" style="text-decoration: none;">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                Explore
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 20px; text-align: center;">
        <h3>📈 Government Dashboard</h3>
        <p>View dengue risk maps and fumigation efforts.</p>
        <a href="/Government_Dashboard" target="_self" style="text-decoration: none;">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                Explore
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
