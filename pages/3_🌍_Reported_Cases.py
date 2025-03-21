import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state to store reported cases data
if "reported_cases" not in st.session_state:
    st.session_state.reported_cases = pd.DataFrame({
        "Location": ["Gulberg, Lahore", "Johar Town, Lahore", "Defence, Lahore"],
        "Year": [2023, 2023, 2023],
        "January": [10, 5, 8],
        "February": [15, 10, 12],
        "March": [80, 50, 30],
        "April": [60, 40, 20],  # Default to 0 for months without data
        "May": [0, 5, 6],
        "June": [0, 0, 0],
        "July": [0, 0, 0],
        "August": [30, 15, 22],
        "September": [120, 80, 75],
        "October": [10, 8, 20],
        "November": [2, 0, 0],
        "December": [0, 1, 3]
    })

# Streamlit page
def main():
    st.title("📅 Reported Dengue Cases")
    st.write("View and manage reported dengue cases data location-wise, month-wise, and year-wise.")

    # Add filters for location and year
    st.subheader("Filters")
    locations = st.session_state.reported_cases["Location"].unique().tolist()
    selected_location = st.selectbox("Select Location", ["All"] + locations)
    years = st.session_state.reported_cases["Year"].unique().tolist()
    selected_year = st.selectbox("Select Year", ["All"] + years)

    # Filter data based on user selection
    filtered_data = st.session_state.reported_cases.copy()
    if selected_location != "All":
        filtered_data = filtered_data[filtered_data["Location"] == selected_location]
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
            id_vars=["Location", "Year"],
            value_vars=[
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ],
            var_name="Month",
            value_name="Number of Cases"
        )
        melted_data["Year-Month"] = melted_data["Month"] + " " + melted_data["Year"].astype(str)

        # Plot the data
        fig, ax = plt.subplots()
        for location in melted_data["Location"].unique():
            location_data = melted_data[melted_data["Location"] == location]
            ax.plot(location_data["Year-Month"], location_data["Number of Cases"], marker="o", label=location)
        ax.set_xlabel("Year-Month")
        ax.set_ylabel("Number of Cases")
        ax.set_title("Reported Dengue Cases Over Time")
        plt.xticks(rotation=45)
        ax.legend()
        st.pyplot(fig)
    else:
        st.info("No data available for visualization.")

    # Add new data
    st.subheader("Add New Data")
    with st.form("add_data_form"):
        location = st.selectbox(
            "Location",
            ["Gulberg, Lahore", "Johar Town, Lahore", "Defence, Lahore", "Other"]
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
                # Check if the location and year already exist in the data
                existing_entry = st.session_state.reported_cases[
                    (st.session_state.reported_cases["Location"] == location) &
                    (st.session_state.reported_cases["Year"] == year)
                ]
                if not existing_entry.empty:
                    # Update the existing entry
                    st.session_state.reported_cases.loc[existing_entry.index, month] = cases
                else:
                    # Add a new entry
                    new_entry = {
                        "Location": location,
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
