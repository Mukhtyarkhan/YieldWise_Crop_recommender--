import streamlit as st
import pandas as pd
import os

def show_dataset_page():
    background_color = "rgb(78, 108, 80)"

    # Convert RGB to hexadecimal
    def rgb_to_hex(rgb):
        rgb_values = rgb.replace("rgb(", "").replace(")", "").split(",")
        r, g, b = map(int, rgb_values)
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    hex_background_color = rgb_to_hex(background_color)
    #sidebar_color = "#4E6C50"

    # Apply background color to the page body
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {background_color};
        }}
            #Services {{
        color: white;
    }}
        </style>
        """,
        unsafe_allow_html=True)
    df=pd.read_csv(r"data/Crop_recommendation.csv")
    st.title("Dataset")
    st.write(df)
     # Add a file uploader widget
    uploaded_file = st.file_uploader("If you have a related dataset, you can upload it here")

    # If a file is uploaded
    if uploaded_file is not None:
        # Check the file extension
        file_extension = os.path.splitext(uploaded_file.name)[1]

        if file_extension == '.csv':
            df_uploaded = pd.read_csv(uploaded_file)
        elif file_extension == '.xlsx':
            df_uploaded = pd.read_excel(uploaded_file)
        elif file_extension == '.json':
            df_uploaded = pd.read_json(uploaded_file)
        else:
            st.error("Invalid file type. Please upload a CSV, XLSX, or JSON file.")
            return

        try:
            # Ensure 'data' directory exists
            if not os.path.exists('data'):
                os.makedirs('data')

            # Save the uploaded file to a new file in your directory
            save_path = r"data/User_uploaded_datasets/user_uploaded_dataset.csv"
            df_uploaded.to_csv(save_path, index=False)

            st.success("Thank you for uploading your dataset. This will help improve our model.")
        except Exception as e:
            st.error(f"Error: {e}")

    # Add a checkbox widget to ask the user if they want to provide feedback
    feedback_checkbox = st.checkbox("Do you have any feedback?")

    # If the checkbox is checked, add a text area widget for the user to enter their feedback
    if feedback_checkbox:
        feedback = st.text_area("Please enter your feedback here:")
        submit_button = st.button("Submit Feedback")

        # If the user enters some feedback and clicks the submit button, save it to a file
        if feedback and submit_button:
            with open("feedback.txt", "a") as f:
                f.write(feedback)
