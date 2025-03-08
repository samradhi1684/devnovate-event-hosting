import streamlit as st
import requests

# Backend URL
BACKEND_URL = "http://127.0.0.1:8080"

def fetch_events():
    """Fetch events from FastAPI."""
    response = requests.get(f"{BACKEND_URL}/events/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("❌ Failed to load events.")
        return []

def register_for_event(event_id):
    """Registers the user for an event."""
    if "firebase_token" not in st.session_state:
        st.error("❌ Please log in first!")
        return

    headers = {"Authorization": f"Bearer {st.session_state['firebase_token']}"}
    response = requests.post(f"{BACKEND_URL}/register_event/{event_id}", headers=headers)

    if response.status_code == 200:
        st.success("✅ Successfully registered for the event!")
    else:
        st.error("❌ Registration failed. Try again.")

def events_page():
    """Display event list with registration buttons."""
    st.title("📅 Events")
    st.write("Welcome! View and register for upcoming events below.")

    events = fetch_events()
    if not events:
        st.info("No events available.")
        return

    for i, event in enumerate(events):
        st.subheader(event.get("title", "No Title"))
    st.write(f"📅 Date: {event.get('date', 'Unknown Date')}")
    st.write(f"📍 Location: {event.get('location', 'No Location Provided')}")

    # Handle missing description safely
    st.write(f"📖 {event.get('description', 'No description available.')}")

    # Ensure unique button key using index
    if st.button(f"Register for {event.get('title', 'this event')}", key=f"register_{i}"):
        register_for_event(event.get("id", ""))

if __name__ == "__main__":
    events_page()
