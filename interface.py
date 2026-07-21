import streamlit as st
import requests

st.title("Hello, dear Customer!")
st.write("Please leave your feedback here!")

with st.form("Leave feedback"):
    text = st.text_input("Feedback:")
    submit = st.form_submit_button("Send Feedback")

if submit:
    data = {"sentence": text}
    response = requests.post("http://backend:8000/text_post", json = data)
    st.write(response.json()["prediction"][0])
