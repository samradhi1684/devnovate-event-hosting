import firebase_admin
from firebase_admin import credentials, auth, firestore
from fastapi import Depends, HTTPException
import uuid

# Load Firebase credentials and initialize Firebase Admin SDK
cred = credentials.Certificate("backend/service-account.json")  # Ensure the correct path
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

def verify_token(id_token: str):
    """Verifies Firebase ID token and returns user info."""
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token  # Returns user details like UID, email, etc.
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

def get_current_user(id_token: str = Depends(verify_token)):
    """Dependency function to get the authenticated user."""
    return id_token  # Contains user details

def create_event(title: str, description: str, date: str):
    """Creates an event in Firestore."""
    event_id = str(uuid.uuid4())  # Generate a unique event ID
    event_ref = db.collection("events").document(event_id)

    event_ref.set({
        "title": title,
        "description": description,
        "date": date,
        "registered_users": []  # Empty list for storing registered user UIDs
    })

    return {"message": "Event created successfully", "event_id": event_id}

def get_events():
    """Fetches all events from Firestore."""
    events = db.collection("events").stream()
    return [
        {
            "id": event.id,
            "title": event.to_dict().get("title", "No Title"),
            "description": event.to_dict().get("description", "No description available"),  # Ensure description exists
            "date": event.to_dict().get("date", "Unknown Date"),
            "location": event.to_dict().get("location", "Unknown Location"),
        }
        for event in events
    ]


def register_user_for_event(event_id: str, user: dict):
    """Registers a user for an event."""
    try:
        print(f"🔍 Attempting to register User: {user['uid']} for Event: {event_id}")  # ✅ Debugging

        event_ref = db.collection("events").document(event_id)
        event_data = event_ref.get()

        if not event_data.exists:
            print("❌ Event not found in Firestore.")
            raise HTTPException(status_code=404, detail="Event not found")

        event_info = event_data.to_dict()
        registered_users = event_info.get("registered_users", [])

        if user["uid"] in registered_users:
            return {"message": "Already registered"}

        registered_users.append(user["uid"])
        event_ref.update({"registered_users": registered_users})
        return {"message": "Registration successful!"}
    except Exception as e:
        print(f"❌ Registration error: {str(e)}")  # ✅ Debugging
        raise HTTPException(status_code=500, detail=str(e))


