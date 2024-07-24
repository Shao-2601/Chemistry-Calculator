import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.header('The Carolina Chemists\' Calculator v1.0')
st.subheader('by Shao')
st.write('Please select your desired calculation: ')

button_1 = st.button('Acid-Base')
button_2 = st.button('Dilutions')

if button_2:
    switch_page('Dilutions')

if button_1:
    switch_page('Acid-Base')


