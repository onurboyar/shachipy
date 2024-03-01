import streamlit as st
import pandas as pd

st.write('Hello, Streamlit!')

st.title('My First Streamlit App')

if st.button('Say hello'):
    st.write('Hello, World!')

st.write('This is a simple text display.')



data = pd.DataFrame({'Column A': [1, 2, 3], 'Column B': [4, 5, 6]})
st.write(data)

age = st.slider('How old are you?', 0, 130, 25)
st.write("You're ", age, 'years old')

if st.button('Click me'):
    st.write('Button clicked!')


col1, col2 = st.columns(2)

with col1:
    st.header('Column 1')
    st.write('Hello, Column 1!')

with col2:
    st.header('Column 2')
    st.write('Hello, Column 2!')