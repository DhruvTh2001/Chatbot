# Chatbot Backend with FastAPI & SQLite

This is the backend of a chatbot application built using **FastAPI**, **SQLite**, and **JWT Authentication** with role-based access control.

## 🔧 Features

- ✅ User authentication with JWT (Login / Register)
- 🔐 Role-based access control (Admin, Editor, Viewer)
- 💬 Endpoints for chatbot interaction
- 🛢️ SQLite database using proper schema and best practices
- 🔄 Swagger UI for API testing and documentation

## 📁 Project Structure

chatbot_database/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── auth.py # JWT authentication & user routes
│ ├── db.py # Database connection and helper functions
│ ├── models.py # Database schema using SQLite
│ ├── roles.py # Role-based access decorators
│ └── chatbot.py # Chatbot interaction logic
│
├── requirements.txt # List of dependencies
└── README.md

bash
Copy
Edit

## ▶️ How to Run

```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn app.main:app --reload
