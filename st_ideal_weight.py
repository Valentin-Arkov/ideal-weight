import streamlit as st

height = st.number_input("Please enter your height in cm: ")

weight = height - 100

st.text(f"Your predicted weight is {weight} kg.")

