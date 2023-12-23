import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/WIN_20231202_21_52_35_Pro.jpg")

with col2:
    st.title("Ashish Pal")
    content="""
    My name is Ashish Pal.
    I am pursuing my B.Tech in specialisation of Artificial Intelligence and Machine Learning.
    I am building the apps by learning from the course.
    I am learning the Python Basics from the course.
    I am always eager to learn about the new technology.
    Now, I am interested to learn about the Web3 from the Rise In platform.
    I will learn the python , Java ,and it's data structure and algorithm.
    """
    #st.write(content)
    st.info(content)

content1 = """
Below you can find some of the apps I have  built in python. Feel free to contact me!
"""
st.write(content1)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
