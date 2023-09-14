import streamlit as st

def show_home_page():
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
        </style>
        """,
        unsafe_allow_html=True)



    st.title("Welcome to YieldWise - Your Personalized Crop Advisor")
    #st.image('Images\\image.jpg')
    st.image(r'Images/image.jpg', caption='Image Caption', use_column_width=True,width=500)

    st.markdown("Are you a farmer in Pakistan seeking the perfect crop for your land? Look no further! YieldWise is here to revolutionize your farming experience.")
    st.header("*Why YieldWise?*")
    st.markdown("- Precision Agriculture at Your Fingertips: YieldWise harnesses the power of data-driven insights to provide you with tailored crop recommendations. We consider your location, soil type, and historical weather patterns to suggest the best crops for your farm. No more guesswork!")
    st.markdown("- Maximize Your Yield: Our cutting-edge machine learning model is designed to help you achieve maximum yield with minimum risk. Say goodbye to crop failures and hello to bountiful harvests.")
    st.markdown("- Farm Smarter, Not Harder: Farming shouldn't be a game of chance. With YieldWise, you'll make informed decisions about what to plant and when. Let us handle the complexity while you focus on what you do best – nurturing your crops.")
    st.header("What YieldWise Offers:")
    st.markdown("🌱 Personalized Recommendations: Tell us where you farm, what type of soil you have, and leave the rest to us. We'll recommend crops that thrive in your specific conditions.")
    st.header("Why Wait? Farming Success Awaits!")
    st.markdown("Ready to reap the benefits of data-driven farming? Start your journey with [**SmartCrop**](#services_page) today and watch your fields flourish. Join the future of agriculture, one crop at a time.", unsafe_allow_html=True)
    st.markdown("<a id='services_page'></a>", unsafe_allow_html=True)
    #st.markdown("Ready to reap the benefits of data-driven farming? Start your journey with <a href='javascript:void(0);'>**SmartCrop**</a> today and watch your fields flourish. Join the future of agriculture, one crop at a time.", unsafe_allow_html=True)
    st.markdown('[How to use YieldWise](https://youtu.be/T5al0HmR4to?si=otJKYZHZBEkPc_Wo)')