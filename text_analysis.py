import streamlit as st

st.title('Text Analysis App')

# Text input
user_input = st.text_area("Enter your text here:")

# Analysis
if st.button('Analyze'):
    char_count = len(user_input)
    word_count = len(user_input.split())
    
    st.write(f"Character Count: {char_count}")
    st.write(f"Word Count: {word_count}")

st.write("This app counts the number of words and characters in your text.")