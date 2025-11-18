import streamlit as st

st.title("Streamlit Widgets Example")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0, 100, 25)

options = ['Python', 'JavaScript', 'C++']
choice = st.selectbox("Select your favorite programming language:", options)

if name:
    st.write(f"Hello, {name}!")

st.write(f"You are {age} years old.")
st.write(f"Your favorite programming language is {choice}.")