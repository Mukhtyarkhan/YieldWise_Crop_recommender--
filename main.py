
import streamlit as st
from streamlit_option_menu import option_menu
from pages import home_page, services_page, dataset_page, aboutus_page
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras
import pickle
import os
import gspread

# Set Streamlit to have a responsive layout
st.set_page_config(
    page_title="Your App Title",
    layout="wide",
    #initial_sidebar_state="expanded",
    initial_sidebar_state="collapsed"  # Use "wide" for responsiveness
)

# Create a menu for page selection
selected = option_menu(
    menu_title=None,
    options=['Home', 'Services', 'Dataset', 'About us'],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles = {
            "container": {"padding": "0!important", "background-color": "rgb(180, 139, 86)",'top':'0'},  # Set the menu bar background color
            "icon": {"color": "blue", "font-size": "25px"},
            "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "green",  # Change hover color to green
                        },
            "nav-link-selected": {"background-color": "green"},  # Set the selected button background color to green
                        }
)

# Display the selected page
if selected == "Home":
    home_page.show_home_page()
elif selected == "Services":
    services_page.show_services_page()
elif selected == "Dataset":
    dataset_page.show_dataset_page()
elif selected == "About us":
    aboutus_page.show_aboutus_page()
