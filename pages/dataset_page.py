import streamlit as st
import pandas as pd
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def show_dataset_page():
    background_color = "rgb(78, 108, 80)"

    # Convert RGB to hexadecimal
    def rgb_to_hex(rgb):
        rgb_values = rgb.replace("rgb(", "").replace(")", "").split(",")
        r, g, b = map(int, rgb_values)
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    hex_background_color = rgb_to_hex(background_color)

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
            st.stop()

        try:
            # Authenticate with Google Sheets API using your credentials JSON file
            scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name('my_json_key.json', scope)
            client = gspread.authorize(creds)

            # Open the Google Sheet by title
            sheet_name = "user_upolded_dataset"
            sheet = client.open(sheet_name).sheet1

            # Append the uploaded data to the Google Sheet
            df_to_upload = df_uploaded.fillna("")  # Replace NaN values with empty strings
            values = df_to_upload.values.tolist()
            sheet.insert_rows(values, 2)  # Insert the data at the second row (modify as needed)

            st.success("Thank you for uploading your dataset. This data has been saved to Google Sheets.")
        except Exception as e:
            st.error(f"Error: {e}")

    # Add a checkbox widget to ask the user if they want to provide feedback
    feedback_checkbox = st.checkbox("Do you have any feedback?")

    # If the checkbox is checked, add a text area widget for the user to enter their feedback
    if feedback_checkbox:
        feedback = st.text_area("Please enter your feedback here:")
        submit_button = st.button("Submit Feedback")

        # If the user enters some feedback and clicks the submit button, save it to a Google Sheet
        if feedback and submit_button:
            try:
                # Authenticate with Google Sheets API using your credentials JSON file (if not already authenticated)
                scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
                creds = ServiceAccountCredentials.from_json_keyfile_name('my_json_key.json', scope)
                client = gspread.authorize(creds)

                # Open the Google Sheet for feedback by title
                feedback_sheet_name = "user_feedback"
                feedback_sheet = client.open(feedback_sheet_name).sheet1

                # Append the feedback to the Google Sheet
                feedback_data = [[feedback]]
                feedback_sheet.insert_rows(feedback_data, 2)  # Insert the feedback at the second row (modify as needed)

                st.success("Thank you for your feedback!")
            except Exception as e:
                st.error(f"Error: {e}")

