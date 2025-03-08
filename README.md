# devnovate-event-hosting

# 🎉 Devnovate Event Hosting Platform  

MeetSync : A web application for hosting and registering for events, built with **Streamlit (Frontend)** and **FastAPI (Backend)**, integrated with **Firebase** for authentication and Firestore as the database.  

---

## 🚀 Features  
- 🔥 User authentication with Firebase  
- 📅 Event creation & registration  
- 🔍 Fetch events dynamically from Firestore  
- ✅ Secure API with FastAPI  

---

## 🛠 Tech Stack  
- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **Database:** Firebase Firestore  
- **Auth:** Firebase Authentication  

---

run FastAPI server using : 
cd backend
uvicorn backend.main:app --host 127.0.0.1 --port 8080 --reload

run streamlit app using :
cd frontend
streamlit run app.py

This project aims to provide a seamless platform where users can log in, view upcoming events, and stay updated on the latest happenings. We plan to enhance the platform by adding features such as one-click registration, smart team formation, and easy event setup, making the process more efficient. Additionally, we will introduce resume-based registrations, allowing users to quickly sign up using their professional profiles. The goal is to create a highly user-friendly interface that simplifies the experience and ensures easy navigation for all users.