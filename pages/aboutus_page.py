import streamlit as st

def show_aboutus_page():    
    background_color = "rgb(78, 108, 80)"

    # Convert RGB to hexadecimal
    def rgb_to_hex(rgb):
        rgb_values = rgb.replace("rgb(", "").replace(")", "").split(",")
        r, g, b = map(int, rgb_values)
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    hex_background_color = rgb_to_hex(background_color)
    #ssidebar_color = "#4E6C50"

    # Apply background color to the page body
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {background_color};
        }}
        </style>
        """,
        unsafe_allow_html=True)
    st.markdown('''
        # About us \n 
        I am Mukhtyar Khan, a data scientist with a passion for using technology to solve real-world problems. 
        I created this crop recommendation app to help farmers make better decisions about what crops to grow.

        The app uses machine learning to analyze weather data, soil conditions, and other factors to recommend the 
        best crops for a given region. I believe that everyone should have access to the information they need to grow 
        healthy and sustainable crops. That's why I'm making my app available to farmers of all sizes, regardless of their budget or technical expertise.

        I am constantly working to improve my app, and I welcome feedback from my users. You can connect with me on 
        social media or visit my website to learn more about my work. \n
                            
        My Social Media Accounts
        - <a href="https://github.com/Mukhtyarkhan" style="color: blue;" target="_blank">Git-Hub</a>
        - <a href="https://www.linkedin.com/in/mukhtyar-khan" style="color: blue;" target="_blank">LinkedIn</a>
        - <a href="https://web.facebook.com/profile.php?id=100039125557634" style="color: blue;" target="_blank">Instagram</a>
                        
        My Website
        - <a href="https://www.datascienceportfol.io/MukhtyarKhan" style="color: blue;" target="_blank">My portfolio</a>
        \n
    ''', unsafe_allow_html=True)