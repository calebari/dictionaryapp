import streamlit as st
import PyDictionary

st.title("Caleb's super duper dictionary app")
dc = PyDictionary.PyDictionary()

st.sidebar.title('enter your word here')
a=st.sidebar.text_input('',)

if st.button('Generate Definition'):
    generated_text = dc.meaning(a)
    st.write(generated_text)
