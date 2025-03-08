from fastapi import FastAPI, Depends
from backend.firebase import get_current_user, create_event, get_events, register_user_for_event  # Import Firestore functions

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Event Hosting Platform!"}

# 🔒 Protected route (only accessible with valid Firebase token)
@app.get("/protected-route")
def protected_route(user: dict = Depends(get_current_user)):
    return {"message": "You have accessed a protected route!", "user": user}

# 📅 Create an event (Protected)
@app.post("/create_event/")
def add_event(title: str, description: str, date: str, user: dict = Depends(get_current_user)):
    response = create_event(title, description, date)
    return {"message": "Event Created Successfully!", "event": response}

# 📅 Fetch all events (Public)
@app.get("/events/")
def list_events():
    return get_events()  # ✅ Fixed incorrect return syntax

@app.post("/register_event/{event_id}")
def register_event(event_id: str, user: dict = Depends(get_current_user)):
    return register_user_for_event(event_id, user)
