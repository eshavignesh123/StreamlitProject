import streamlit as st
import random
clicked = st.button("Click")

if clicked:
    num = random.randint(1,10)
    st.write(num)




