# Q7
import streamlit as st
import csv
import pandas as pd
import numpy as np

st.title("DataInsight Corp. - Feedback Hub")
st.header("Customer Feedback Dashboard")
tab1, tab2 = st.tabs(["Submit New FeedBack", "View & Analyze Feedback"])

with tab1:
     with st.form(key="feedback_form"):

        st.header("Enter Feedback details")
        st.text_input("Customer Name")
        st.selectbox("Product", ["WebApp Pro", "DataSuite Plus", "Analytics Dashboard"])
        st.number_input("Rating", min_value=1, max_value=5)
        submitted = st.form_submit_button("Submit feedback")
        if submitted:
            st.success("Thank you! Feedback submitted successfully.")

with tab2:
    st.header("View & Analyze Feedback")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Upload Data")
        user_file = st.file_uploader("Upload Feedback CSV File")

        if user_file is not None:

            df_user = pd.read_csv(user_file)
            st.dataframe(df_user)
        
        elif user_file is None:
            st.write("No file uploaded. Displaying sample data:")

            products = ["WebApp Pro", "DataSuite Plus", "Analytics Dashboard", "WebApp Pro", "DataSuite Plus", "Analytics Dashboard", "WebApp Pro", "DataSuite Plus", "Analytics Dashboard", "WebApp Pro"]
            names = ["Alice Smith", "Bob Johnson", "Carol Davis", "David Wilson", "Emma Brown", "Frank Miller", "Amy Chen", "Kevin Lee", "Robert Taylor", "Michelle Clark"]

            ratings = np.random.randint(1, 5, size=10)
            df_sample = pd.DataFrame({"Customer_Names": names, "Products": products, "Rating": ratings})
            st.dataframe(df_sample)


    with col2:
        st.header("Data Analysis")
        threshold = st.slider("Select Rating Threshold", 1, 5)

        if user_file is not None:
            st.write(f"Total feedback entires: {df_user.size}")
            st.write(f"Average Rating: {df_user.mean()}")
            st.write(f"Ratings >= {threshold}: {df_user['Ratings'].where(df_user['Ratings'] >= threshold).sum()}")
        
        if user_file is None:
            st.write("Please upload csv file to see your feedback statistics")
