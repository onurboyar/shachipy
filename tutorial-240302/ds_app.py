import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the app
st.title('Data Science App with Streamlit')

# Generate sample data
@st.cache_data # Use caching to generate the data only once
def generate_data(n_rows, n_cols):
    """Generates a DataFrame with random data"""
    dates = pd.date_range(start="2021-01-01", periods=n_rows, freq="D")
    data = np.random.randn(n_rows, n_cols)
    columns = [f"Column_{i}" for i in range(1, n_cols + 1)]
    return pd.DataFrame(data, index=dates, columns=columns)

# User input for the size of the dataset
n_rows = st.sidebar.slider("Number of rows", min_value=10, max_value=1000, value=100, step=10)
n_cols = st.sidebar.slider("Number of columns", min_value=1, max_value=20, value=5, step=1)

# Generate and display the dataframe
df = generate_data(n_rows, n_cols)
st.write("### Generated Data", df)

# Show column statistics
if st.sidebar.checkbox('Show Column Statistics'):
    st.write("### Column Statistics", df.describe())

# Visualization
if st.sidebar.checkbox('Show Histogram'):
    column_to_plot = st.sidebar.selectbox('Select Column to Visualize', df.columns)
    fig, ax = plt.subplots()
    df[column_to_plot].hist(bins=20, ax=ax)
    ax.set_title(f'Histogram of {column_to_plot}')
    st.pyplot(fig)

st.write("This app demonstrates Streamlit's capability for data science tasks using generated data.")
