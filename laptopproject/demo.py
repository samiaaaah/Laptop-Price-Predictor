
import streamlit as st
import pickle
import numpy as np

# import model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df1.pkl','rb'))

# title
css = """
<style>
    .title {
        font-size: 44px;
        font-weight: bold;
        color: #ffffff;
        margin-top: 20px;
        text-shadow:
            -3px 2px 0px black,
            3px 2px 0px black,
            2px -4px 0px black,
            2px 3px 0px black;
    }
</style>
"""

# Display the styled title using markdown
st.markdown(css, unsafe_allow_html=True)
st.markdown("<div class='title'>Laptop Price Predictor</div>", unsafe_allow_html=True)

# ==============================================================================
# brand
company = st.selectbox('Brand', df['Company'].unique())

# type of lap
type = st.selectbox("Type", df['TypeName'].unique())

# Ram
ram = st.selectbox("RAM(in GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])

# weight
weight = st.number_input('Weight of the laptop')

# Touchsreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# ips
ips = st.selectbox('IPS', ['No', 'Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',
                          ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600',
                           '2560x1440', '2304x1440'])

# cpu

cpu = st.selectbox('CPU', df['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

gpu = st.selectbox('GPU', df['Gpu brand'].unique())

os = st.selectbox('OS', df['os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res ** 2)) **1.0/screen_size
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

    query = query.reshape(1, 12)

    result = f"<div class='title'>The predicted price of this configuration is \n{str(int(np.exp(pipe.predict(query)[0])))}</div>"
    # st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))
    st.markdown(result, unsafe_allow_html=True)


def set_background_image(image_url):
    # Apply custom CSS to set the background image
    page_bg_img = '''
    <style>
    .stApp {
        background-position: top;
        background-image: url(%s);
        background-size: cover;
    }

    @media (max-width: 768px) {
        /* Adjust background size for mobile devices */
        .stApp {
            background-position: top;
            background-size: contain;
            background-repeat: no-repeat;
        }
    }
    </style>
    ''' % image_url
    st.markdown(page_bg_img, unsafe_allow_html=True)


def main():
    # Set the background image URL
    background_image_url = "https://images.pexels.com/photos/218863/pexels-photo-218863.jpeg?auto=compress&cs=tinysrgb&w=1600"

    # Set the background image
    set_background_image(background_image_url)

    custom_css = """
       <style>
       body {
           background-color: #4699d4;
           color: #ffffff;
           font-family: Arial, sans-serif;
       }
       select {
           background-color: #000000 !important; /* Black background for select box */
           color: #ffffff !important; /* White text within select box */
       }
       label {
           color: #ffffff !important; /* White color for select box label */
       }
       </style>
       """
    st.markdown(custom_css, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

css2 = """
<style>
    .write {
        font-size: 20px;
        font-weight: bold;
        color: #ffffff;
        margin-top: 20px;
        text-shadow:
            -3px 2px 0px black,
            3px 2px 0px black,
            2px -4px 0px black,
            2px 3px 0px black;
    }
</style>
"""
st.markdown(css2, unsafe_allow_html=True)
st.write("<div class='write'>made by SAMIYA MAHVEEN</div>", unsafe_allow_html=True)