import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("My First Streamlit App")

## Display a simple Text
st.write("Hello, welcome to my first Streamlit application!")

## Display a DataFrame
df = pd.DataFrame({
    'Column A': [1, 2, 3, 4],
    'Column B': [10, 20, 30, 40]
})

## Display the DataFrame in the app
st.write("Here is a sample DataFrame:")
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),columns=['a', 'b', 'c']
)
st.line_chart(chart_data)