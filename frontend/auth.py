import streamlit as st
import pyrebase
import urllib.parse

# Firebase Configuration
firebase_config = {
    "apiKey": "AIzaSyDs5QY1NYTWzv1IO2EdvNzBpoLshjRIJII",
    "authDomain": "devnovate-event-hosting.firebaseapp.com",
    "projectId": "devnovate-event-hosting",
    "storageBucket": "devnovate-event-hosting.appspot.com",
    "messagingSenderId": "167966907642",
    "appId": "1:167966907642:web:eede517c70943ca0cbfd43",
    "measurementId": "G-MF2TK4YDL8",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def login():
    """ User Login Form """
    st.title("🔐 Login to MeetSync")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state["user"] = user
            st.session_state["firebase_token"] = user['idToken']  # Store token securely
            st.success(f"✅ Logged in as {email}")
        except Exception as e:
            st.error("❌ Login failed. Check credentials.")

    # Google Sign-In
    google_url = f"https://accounts.google.com/o/oauth2/auth?client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost:8501/&response_type=token&scope=email profile"
    
    if st.button("Sign in with Google"):
        st.experimental_set_query_params(redirect=urllib.parse.quote(google_url))
        st.markdown(f"[Click here to sign in with Google]({google_url})", unsafe_allow_html=True)

    # Handle Redirected Token
    params = st.query_params
    if "id_token" in params:
        token = params["id_token"][0]
        try:
            user_info = auth.get_account_info(token)
            st.session_state["user"] = user_info
            st.session_state["firebase_token"] = token  # Store token securely
            st.success("✅ Google Sign-In Successful!")
        except Exception as e:
            st.error("❌ Google Authentication failed.")

def register():
    """ User Registration Form """
    st.title("📝 Register for Event Hosting Platform")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password != confirm_password:
            st.error("❌ Passwords do not match!")
            return

        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("✅ Registration successful! You can now log in.")
        except Exception as e:
            st.error("❌ Registration failed. Email might already be in use.")

def logout():
    """ Logout Function """
    st.session_state.pop("user", None)
    st.session_state.pop("firebase_token", None)  # Clear token on logout
    st.success("🔓 Logged out successfully!")

def display_user_info():
    """ Display logged-in user details """
    if "user" in st.session_state:
        st.sidebar.write(f"👤 Logged in as: {st.session_state['user']['email']}")
        if "firebase_token" in st.session_state:
            st.sidebar.text("✅ Authenticated")  # Show successful authentication
        st.sidebar.button("Logout", on_click=logout)
    else:
        st.sidebar.write("🔓 Not logged in")
