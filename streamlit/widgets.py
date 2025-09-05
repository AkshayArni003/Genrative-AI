import streamlit as st
import pandas as pd

st.title("Text Input")

name = st.text_input("Enter your Name")
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is: {age}")

options = ["Python", "Javascript", "Java"]
st.selectbox("Select your fav language", options)
if name:
    st.write(f"Hello {name}")

df = pd.DataFrame({
    "Name": ["Akshay", "Keerthana", "Arni"],
    "Age": [30, 29, 31],
    "City": ["Banglore", "Mandya", "Kerla"]
})
df.to_csv("sample.csv")
uploaded_file=st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)