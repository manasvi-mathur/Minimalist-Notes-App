# Modern Minimalist Notes App

A clean, full-stack Note-Taking application built with **Django**, **jQuery**, and **Bootstrap**. This project features smooth animations, real-time search, and a complete RESTful API.

![Notes App Preview](https://img.shields.io/badge/Tech-Django%20|%20jQuery%20|%20Bootstrap%20|%20SQLite-blue)

## ✨ Key Features
- **Modern UI**: Smooth fade-in animations and subtle hover effects.
- **AJAX Driven**: Create, Read, Update, and Delete notes without refreshing the page.
- **Search**: Instant filtering to find your notes quickly.
- **RESTful API**: Clean endpoints for managing data as JSON.
- **Clean Aesthetic**: A minimalist "Azure & Slate" design.

## 🛠️ Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript (jQuery)
- **Styling**: Bootstrap 5 + Custom Animations
- **Database**: SQLite (No local setup required)

## 📡 API Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/notes/` | Fetch all notes |
| `POST` | `/api/add/` | Create a new note |
| `POST` | `/api/update/<id>/` | Edit an existing note |
| `DELETE` | `/api/delete/<id>/` | Remove a note |

## 🚀 Getting Started
1. **Clone the repo**:
   ```bash
   git clone https://github.com/AtharvaMaik/DjangoNotes.git
   cd DjangoNotes
   ```
2. **Install Dependencies**:
   ```bash
   pip install django
   ```
3. **Setup Database**:
   ```bash
   python manage.py migrate
   ```
4. **Run the App**:
   ```bash
   python manage.py runserver
   ```
5. **Open Browser**:
   Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📄 License
Created for educational purposes. Feel free to use and modify!
