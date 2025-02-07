import streamlit as st
import os
from models import APIKeyModel
from asyncio import run
import requests

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None
if "page" not in st.session_state:
    st.session_state.page = "login"

def handle_login(page, username, password):
    """Validate credentials and navigate if successful."""
    valid_username = "user"
    valid_password = "password"

    if username == valid_username and password == valid_password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.page = page
    else:
        st.error("Invalid username or password!")

def login_page():
    """Render the login page."""
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    st.button("Login", on_click=handle_login, args=('key_entry', username, password))

def key_page():
    """Render the key entry page."""
    st.title("Key Entry Page")
    st.write(f"Welcome, {st.session_state.username}!")
    prompt = st.text_input("Enter your prompt...")
    prompt_dict = {}
    prompt_dict["prompt"] = prompt
    
    ENDPOINT = "http://fastapi:8000/ask-question"
    # ENDPOINT = "http://127.0.0.1:8000/ask-question" Commented for Docker compose
        
    if st.button("Submit"):
        response = requests.post(ENDPOINT, json=prompt_dict)
        response.raise_for_status()
        data = response.json()
        result = data.get('response')
        st.write(result)

if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "key_entry":
    key_page()