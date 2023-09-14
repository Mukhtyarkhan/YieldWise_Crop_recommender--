import pandas as pd
import streamlit as st 
from streamlit_option_menu import option_menu
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras
import pickle
import os

def show_services_page():
    background_color = "rgb(78, 108, 80)"

    # Convert RGB to hexadecimal
    def rgb_to_hex(rgb):
        rgb_values = rgb.replace("rgb(", "").replace(")", "").split(",")
        r, g, b = map(int, rgb_values)
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    hex_background_color = rgb_to_hex(background_color)
    sidebar_color = "#4E6C50"

    # Apply background color to the page body
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {background_color};
        }}
        text_color
       
        </style>
        """,
        unsafe_allow_html=True
    )
    # Load the saved deep learning model
    loaded_model=r"models/model_filename.h5"
    loaded_model=keras.models.load_model(loaded_model)

    # Load the saved MinMaxScaler
    scaler_filename = r'scaler/scaler.pkl'
    with open(scaler_filename, 'rb') as scaler_file:
       scaler = pickle.load(scaler_file)

    # Define the function to get the crop recommendation using the loaded model
    def recommendation(N, P, K, temperature, humidity, ph, rainfall):
        # Scale the user input data using the loaded scaler
        user_input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        scaled_user_input = scaler.transform(user_input_data)
        
        # Make predictions with the loaded model
        prediction = loaded_model.predict(scaled_user_input)
        crop_id = np.argmax(prediction)
        return crop_id

    # Create a Streamlit app
    st.title('Crop Recommendation System')

    # Language selection option
    language_options = ["English", "Urdu","Sindhi"]
    language = st.selectbox("Select Language", language_options,)

    if language == "English":
        N_label = 'Enter nitrogens quantity'
        P_label = 'Enter Phosphorus quantity'
        K_label = 'Enter Potassiums quantity'
        temperature_label = 'Enter Temperature quantity '
        humidity_label = 'Enter Humidity quantity'
        ph_label = 'Enter pH quantity'
        rainfall_label = 'Enter Rainfall quantity'
        submit_button_label = 'Submit'
        
        crop_names = {
            0: "rice",
            1: "maize",
            2: "jute",
            3: "cotton",
            4: "coconut",
            5: "papaya",
            6: "orange",
            7: "apple",
            8: "muskmelon",
            9: "watermelon",
            10: "grapes",
            11: "mango",
            12: "banana",
            13: "pomegranate",
            14: "lentil",
            15: "blackgram",
            16: "mungbean",
            17: "mothbeans",
            18: "pigeonpeas",
            19: "kidneybeans",
            20: "chickpea",
            21: "coffee",
            22: "peas",
            23: "cowpeas",
            24: "groundnuts",
            25: "beans",
            26: "Soyabeans",
            27: "wheat",
            28: 'tobacco'
        }
        
    elif language == "Urdu":
        N_label = 'نائٹروجن کی مقدار درج کریں'
        P_label = 'فاسفورس کی مقدار درج کریں'
        K_label = 'پوٹاشیم کی مقدار درج کریں'
        temperature_label = 'درجہ حرارت کی مقدار درج کریں'
        humidity_label = 'نمی کی مقدار درج کریں'
        ph_label = 'پی ایچ کی مقدار درج کریں'
        rainfall_label = 'بارش کی مقدار درج کریں'
        submit_button_label = 'جمع کروائیں'


        
        crop_names_urdu={
                0:"چاول", 
                1:"مکئ", 
                2:"پٹ سن", 
                3:"کپاس", 
                4:"ناریل", 
                5:"پپیتا", 
                6:"سنترہ", 
                7:"سیب", 
                8:"خربوزہ", 
                9:"تربوز", 
                10:"انگور", 
                11:"آم", 
                12:"کیلا", 
                13:"انار", 
                14:"دال مسور", 
                15:"کالی دال", 
                16:"مونگ کی دال", 
                17:"موتھ کی دال", 
                18:"ارہر کی دال", 
                19:"لوبیا کی دال", 
                20:"چنا کی دال",
                21: "کافی",
                22: "مٹر",
                23: "لوبیا",
                24: "مونگ پھلی",
                25: "فلیاں",
                26: "سویابین",
                27: "گندم",
                28: 'تمباکو'
            }
        crop_names = crop_names_urdu
    elif language == "Sindhi":
        N_label = 'نائيٽروجن جي مقدار داخل ڪريو'
        P_label = 'فاسفورس جو مقدار داخل ڪريو'
        K_label = 'پوٽاشيم جو مقدار داخل ڪريو'
        temperature_label = 'درجه حرارت جي مقدار داخل ڪريو'
        humidity_label = 'نمي جي مقدار داخل ڪريو'
        ph_label = 'pH مقدار داخل ڪريو'
        rainfall_label = 'برسات جي مقدار داخل ڪريو'
        submit_button_label = 'جمع ڪريو'

        crop_names_sindhi={
            0: "چانور",
             1: "مڪئي",
             2: "جٽ",
             3: "ڪپڙو",
             4: "ناريل",
             5: 'پپيا',
             6: "نارنگي",
             7: "انب",
             8: 'مشڪلون',
             9: "تربوز",
             10: "انگور",
             11: 'آم',
             12: "ڪيلا",
             13: "انار",
             14: "دال",
             15: "ڪارو گرام",
             16: 'منگبين',
             17: "مٿبين",
             18: 'ڪبوتر',
             19: 'ڪڊني بينز',
             20: "چڪڙ",
             21: "ڪافي",
             22: "مٽر",
             23: "گواه",
             24: "مونگون",
             25: "ڀاڄيون",
             26: "سويابين",
             27: "گڻ",
             28: 'تمباکو',
         }
        crop_names=crop_names_sindhi
        

    # Input fields for the crop recommendation
    N = st.number_input(N_label)
    P = st.number_input(P_label)
    K = st.number_input(K_label)
    temperature = st.number_input(temperature_label)
    humidity = st.number_input(humidity_label)
    ph = st.number_input(ph_label)
    rainfall = st.number_input(rainfall_label)
    # Define the function to save the user input data and crop recommendation to a CSV file
    def save_user_input(N, P, K, temperature, humidity, ph, rainfall, crop):
        # Create a DataFrame with the user input data and crop recommendation
        df = pd.DataFrame({
            'N': [N],
            'P': [P],
            'K': [K],
            'temperature': [temperature],
            'humidity': [humidity],
            'ph': [ph],
            'rainfall': [rainfall],
            'crop': [crop]
        })
        
        # Append the DataFrame to the CSV file
        df.to_csv(r'data/user_input_data.csv', mode='a', header=False, index=False)

    # Call the save_user_input function when the user clicks the Submit button
    if st.button(submit_button_label):
        crop_id = recommendation(N, P, K, temperature, humidity, ph, rainfall)
        
        if crop_id in crop_names:
            crop_name = crop_names[crop_id]
            
            # Save the user input data and crop recommendation to a CSV file
            save_user_input(N, P, K, temperature, humidity, ph, rainfall, crop_name)

            if language == "English":
                st.write('The best crop to be cultivated is {}'.format(crop_name))
            elif language == "Urdu":
                st.write('اس ماحول کے لئے کاشت کرنے کے لئے بہترین فصل {}'.format(crop_name))
            elif language=="Sindhi":
                st.write('پوکڻ لاءِ بهترين فصل آهي{}'.format(crop_name))
                
        else:
            if language == "English":
                st.write('Sorry, we are not able to recommend a proper crop for this environment')
            elif language == "Urdu":
                st.write('معذرت، اس ماحول کے لئے ایک مناسب فصل کی تجویز نہیں دے سکتے')
            elif language=="Sindhi":
                st.write('معاف ڪجو، اسان هن ماحول لاءِ مناسب فصل جي سفارش ڪرڻ جي قابل نه آهيون')