import streamlit as st
from auth import login, logout, display_user_info, register  # Ensure register is imported
from pages.home import home
from pages.events import events_page

# Set page title
st.set_page_config(page_title="Event Hosting Platform", page_icon="📅", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")

# Display user info if logged in
display_user_info()

if "user" not in st.session_state:
    # Show navigation for unauthenticated users
    page = st.sidebar.radio("Go to", ["Sign In", "Sign Up"])  # Changed "Login" → "Sign In"
    
    if page == "Sign In":
        login()
    elif page == "Sign Up":
        register()  
else:
    # Show app pages after login
    page = st.sidebar.radio("Go to", ["Home", "Events"])
    
    if page == "Home":
        home()
    elif page == "Events":
        events_page()

    # Logout button
    if st.sidebar.button("Logout"):
        logout()
