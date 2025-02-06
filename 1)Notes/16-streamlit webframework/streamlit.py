# Stramlit is open source app framework for machine learning and data science projects. 

import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title("Hello Streamlit")

# Display a simple text
st.write("this is simmple text")

# creating a dataframe
df = pd.DataFrame({
    'first coloumn':[1,2,3,4],
    'second column':[10,20,30,40]
})

# Display the dataframe
st.write("Here is the dataframe")
st.write(df)

# Create a line chart 
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)