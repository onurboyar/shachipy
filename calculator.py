import streamlit as st
st.title('Simple Calculator')

# Inputs
num1 = st.number_input('Enter first number', format='%f')
num2 = st.number_input('Enter second number', format='%f')

# Operations
operation = st.selectbox('Choose an operation:', ['Add', 'Subtract', 'Multiply', 'Divide'])

# Calculate
if st.button('Calculate'):
    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    st.success(f'Result: {result}')