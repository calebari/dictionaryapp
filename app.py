import streamlit as st
import PyDictionary

st.title("Caleb's super duper dictionary app")
dc = PyDictionary.PyDictionary()

st.sidebar.title('enter your word here')
a=st.sidebar.text_input('',30)

w1 = dc.meaning(a)
print(w1)
