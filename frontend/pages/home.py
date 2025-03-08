import streamlit as st

def home():
    st.title("🎉 Welcome to MeetSync")
    st.write("An event hosting platform that lets you easily create, discover, and manage events in real time.")

    # Upcoming Events Section
    st.subheader("📅 Upcoming Events")
    events = [
        {"name": "Tech Meetup", "date": "March 20, 2025", "location": "Ahmedabad"},
        {"name": "Startup Pitch Night", "date": "April 5, 2025", "location": "Vadodara"},
        {"name": "AI Workshop", "date": "April 15, 2025", "location": "Gandhinagar"},
    ]

    for event in events:
        with st.container():
            st.write(f"### {event['name']}")
            st.write(f"📅 **{event['date']}** | 📍 **{event['location']}**")
            st.button(f"🔍 View Details", key=event["name"])

if __name__ == "__main__":
    home()
