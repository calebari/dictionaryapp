import streamlit as st
import PyDictionary

st.title("Caleb's super duper dictionary app")
dc = PyDictionary.PyDictionary()
a = input('enter a word')
w1 = dc.meaning(a)
print(w1)
