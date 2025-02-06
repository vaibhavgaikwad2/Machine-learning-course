# It is useful to create beautiful webapp

import streamlit as st

st.title("streamlit text input")
name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}")

age = st.slider("Select your age",0,100,18)
st.write(f"your age is {age}")


options = ["Python","Java","C++","Javascript"]
choice = st.selectbox("Choose your favorite language",options)
st.write(f"You select {choice}.")