import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize session state to store reported cases data
if "reported_cases" not in st.session_state:
    st.session_state.reported_cases = pd.DataFrame({
        "City": ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Multan"],
        "Year": [2023, 2023, 2023, 2023, 2023],
        "January": [10, 5, 8, 12, 15],
        "February": [15, 10, 12, 18, 20],
        "March": [80, 50, 30, 40, 60],
        "April": [60, 40, 20, 30, 50],
        "May": [0, 5, 6, 8, 10],
        "June": [0, 0, 0, 0, 0],
        "July": [0, 0, 0, 0, 0],
        "August": [30, 15, 22, 25, 35],
        "September": [120, 80, 75, 90, 100],
        "October": [10, 8, 20, 15, 25],
        "November": [2, 0, 0, 5, 8],
        "December": [0, 1, 3, 2, 4]
    })

# Streamlit page
def main():
    st.set_page_config(page_title="Reported Dengue Cases", layout="wide")
    st.title("Reported Dengue Cases")
    st.write("View and manage reported dengue cases data city-wise, month-wise, and year-wise.")

    # Add filters for city and year
    st.subheader("Filters")
    cities = st.session_state.reported_cases["City"].unique().tolist()
    selected_city = st.selectbox("Select City", ["All"] + cities)
    years = st.session_state.reported_cases["Year"].unique().tolist()
    selected_year = st.selectbox("Select Year", ["All"] + years)

    # Filter data based on user selection
    filtered_data = st.session_state.reported_cases.copy()
    if selected_city != "All":
        filtered_data = filtered_data[filtered_data["City"] == selected_city]
    if selected_year != "All":
        filtered_data = filtered_data[filtered_data["Year"] == selected_year]

    # Display filtered data
    st.subheader("Reported Cases Data")
    st.dataframe(filtered_data, use_container_width=True)

    # Visualize data
    st.subheader("Visualization")
    if not filtered_data.empty:
        # Melt the data for visualization
        melted_data = filtered_data.melt(
            id_vars=["City", "Year"],
            value_vars=[
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ],
            var_name="Month",
            value_name="Number of Cases"
        )
        melted_data["Year-Month"] = melted_data["Month"] + " " + melted_data["Year"].astype(str)

        # Plot the data using Plotly
        fig = px.line(
            melted_data,
            x="Year-Month",
            y="Number of Cases",
            color="City",
            markers=True,
            title="Reported Dengue Cases Over Time"
        )
        fig.update_layout(
            xaxis_title="Year-Month",
            yaxis_title="Number of Cases",
            legend_title="City",
            xaxis_tickangle=-45,
            template="plotly_white"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for visualization.")

    # Add new data
    st.subheader("Add New Data")
    with st.form("add_data_form"):
        city = st.selectbox(
            "City",
            ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Multan", "Other"]
        )
        year = st.number_input("Year", min_value=2000, max_value=2100, value=2023)
        month = st.selectbox(
            "Month",
            [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ]
        )
        cases = st.number_input("Number of Cases", min_value=0, value=0)
        submit_button = st.form_submit_button("Add Data")

        if submit_button:
            if year and month and cases >= 0:
                # Check if the city and year already exist in the data
                existing_entry = st.session_state.reported_cases[
                    (st.session_state.reported_cases["City"] == city) &
                    (st.session_state.reported_cases["Year"] == year)
                ]
                if not existing_entry.empty:
                    # Update the existing entry
                    st.session_state.reported_cases.loc[existing_entry.index, month] = cases
                else:
                    # Add a new entry
                    new_entry = {
                        "City": city,
                        "Year": year,
                        "January": 0,
                        "February": 0,
                        "March": 0,
                        "April": 0,
                        "May": 0,
                        "June": 0,
                        "July": 0,
                        "August": 0,
                        "September": 0,
                        "October": 0,
                        "November": 0,
                        "December": 0
                    }
                    new_entry[month] = cases
                    st.session_state.reported_cases = pd.concat(
                        [st.session_state.reported_cases, pd.DataFrame([new_entry])], ignore_index=True
                    )
                st.success("Data added/updated successfully!")
            else:
                st.error("Please fill in all fields correctly.")

    # Edit existing data
    st.subheader("Edit Data")
    edited_df = st.data_editor(
        st.session_state.reported_cases,
        use_container_width=True,
        num_rows="dynamic"
    )
    if not edited_df.equals(st.session_state.reported_cases):
        st.session_state.reported_cases = edited_df
        st.success("Data updated successfully!")

if __name__ == "__main__":
    main()
