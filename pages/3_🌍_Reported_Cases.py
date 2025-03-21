import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state to store reported cases data
if "reported_cases" not in st.session_state:
    st.session_state.reported_cases = pd.DataFrame({
        "Location": ["Gulberg, Lahore", "Johar Town, Lahore", "Defence, Lahore"],
        "Year": [2023, 2023, 2023],
        "Month": ["January", "February", "March"],
        "Number of Cases": [10, 15, 20]
    })

# Streamlit page
def main():
    st.title("📅 Reported Dengue Cases")
    st.write("View and manage reported dengue cases data location-wise, month-wise, and year-wise.")

    # Display reported cases data
    st.subheader("Reported Cases Data")
    st.dataframe(st.session_state.reported_cases, use_container_width=True)

    # Visualize data
    st.subheader("Visualization")
    if not st.session_state.reported_cases.empty:
        # Group data by Year and Month for visualization
        grouped_data = st.session_state.reported_cases.groupby(["Year", "Month"])["Number of Cases"].sum().reset_index()
        grouped_data["Year-Month"] = grouped_data["Month"] + " " + grouped_data["Year"].astype(str)

        # Plot the data
        fig, ax = plt.subplots()
        grouped_data.plot(x="Year-Month", y="Number of Cases", kind="line", ax=ax, marker="o", color="skyblue")
        ax.set_xlabel("Year-Month")
        ax.set_ylabel("Number of Cases")
        ax.set_title("Reported Dengue Cases Over Time")
        plt.xticks(rotation=45)
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
                new_data = pd.DataFrame({
                    "Location": [location],
                    "Year": [year],
                    "Month": [month],
                    "Number of Cases": [cases]
                })
                st.session_state.reported_cases = pd.concat(
                    [st.session_state.reported_cases, new_data], ignore_index=True
                )
                st.success("Data added successfully!")
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
