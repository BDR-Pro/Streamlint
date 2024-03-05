# Import convention
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
clicked=st.button('Hit me')
try:
    if clicked:
        st.write('Button clicked')
except:
    pass
#st.data_editor('Edit data', data)
st.checkbox('Check me out')
res=st.radio('Pick one:', ['nose','ear'])
st.write(res)
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.data_editor(df)
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
uploaded=st.file_uploader('File uploader')
try:
    st.image(uploaded)
except:
    pass
st.latex(r"x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}")
# File path to your image
file_path = 'monero.jpg'
file_name = 'monero.jpg'  # The name you want the downloaded file to have

# Read the file in binary mode
with open(file_path, "rb") as file:
    btn = st.download_button(
            label="Click to Download the image",
            data=file,  # Pass file content, not file name
            file_name=file_name,
            mime="image/jpeg"  # MIME type
        )
    
audio_file = open('download.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')

video_file = open('code_animation.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes, format='video/mp4', start_time=5)
color=st.color_picker('Pick a color')
try:
    st.write(color)
    st.write('Color picked')
except:
    pass

with st.form(key='my_form', clear_on_submit=True):
    st.write('Inside the form')
    article=st.text_input('Enter some text')
    number=st.number_input('Enter a number')
    st.checkbox('Check me out')
    sumbited=st.form_submit_button('Submit')

try:
    if sumbited:
        st.write(article)
        st.write(number)
        st.write('Form submitted')
except:
    pass