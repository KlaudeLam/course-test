import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to the DS Class")
st.subheader("Welcome to the DS Class")
st.write("Hello world")
st.write("### hihi")
st.caption("This is a caption")

# Include beyond text
st.code("x=6767")
st.latex(r'''a+a = e^-1''')

st.image("image.png", )

# Interactive
st.checkbox("yes")
st.button("click")
st.radio("choose",["a","b"])
st.multiselect("Pick",["a","b"])
st.slider("slide",0,100)

# Advanced input
st.number_input("choose a no.",0,10)
st.text_input("email")
st.date_input("bday")

st.sidebar.file_uploader("Gib cat meme")

# Display CSV
df = pd.read_csv("bnpl_dataset.csv")
st.dataframe(df.head(5))