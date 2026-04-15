## ✅ Requirement Compliance

This project satisfies all Lab requirements for a full-stack web application:

| Requirement | How it is Satisfied |
| :--- | :--- |
| **Complete Web App** | Features both a Django backend and a responsive jQuery frontend. |
| **Structured HTML** | Standard HTML5 tags used in `index.html` for clean structure. |
| **CSS & Bootstrap** | Custom CSS animations + Bootstrap 5 utility classes for styling. |
| **JS & jQuery** | `index.js` logic handles all user events and UI state. |
| **Dynamic AJAX** | All data operations (Add, Edit, Delete) are performed via background AJAX. |
| **Python & Django** | Server-side logic, routing, and response handling built with Django. |
| **Database Integration** | Uses **SQLite** via Django ORM (as requested for minimal setup). |
| **RESTful API** | Implements standard REST endpoints returning JSON data. |
| **Frontend/API Interaction**| The frontend consumes the REST API via asynchronous AJAX calls. |

---

## 🚀 Technologies Used

### Frontend (Client-Side)
- **HTML5**: Provides the semantic structure of the web pages.
- **CSS3**: Custom styling for smooth fade-in animations, hover effects, and a modern Slate & Azure color palette.
- **Bootstrap 5**: A responsive CSS framework used for the grid system, buttons, cards, and the **Edit Modal** component.
- **JavaScript & jQuery**: used for DOM manipulation and handling user interactions (clicks, searches).
- **AJAX**: Performed via jQuery to make asynchronous HTTP requests to the backend without reloading the page.

### Backend (Server-Side)
- **Django Framework**: A high-level Python web framework used for routing, server-side logic, and database management.
- **Django ORM**: Used to interact with the database using Python objects instead of raw SQL queries.
- **SQLite**: A lightweight, file-based SQL database used for storing and retrieving notes.

---

## 📑 Project Structure

```text
mini_notes/
├── manage.py            # Django project entry point
├── db.sqlite3           # SQLite Database file
├── notes_project/       # Project Configuration
│   ├── settings.py      # Database and App settings
│   ├── urls.py          # Main URL routing
│   ├── wsgi.py          # Web Server Gateway Interface
│   └── asgi.py          # Asynchronous Server Gateway Interface
└── myapp/               # Application Logic
    ├── models.py        # Database Schema (Note model)
    ├── views.py         # Request handling and API logic
    ├── urls.py          # App-specific URL patterns
    └── templates/       # Frontend files
        └── index.html   # Main single-page interface
```

---

## 📡 RESTful API Endpoints

The frontend interacts with the backend entirely through these JSON-based endpoints:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/api/notes/` | Retrieves a list of all notes, ordered by newest first. |
| **POST** | `/api/add/` | Creates a new note. Expects JSON: `{"content": "..."}`. |
| **POST** | `/api/update/<id>/` | Updates an existing note by ID. Expects JSON: `{"content": "..."}`. |
| **DELETE** | `/api/delete/<id>/` | Permanently deletes a note by its ID. |

---

## 🛠️ Dynamic Interactions (AJAX)

The application utilizes **Asynchronous JavaScript and XML (AJAX)** for a "Single-Page Application" (SPA) feel.

### Why AJAX?
Instead of traditional web pages where every action (like adding a note) requires a full page refresh, AJAX allows the frontend to communicate with the server in the background. This results in:
- **Instant Feedback**: Notes appear/disappear without the screen flickering.
- **Lower Bandwidth**: Only JSON data is transferred, not the entire HTML page.

### How it's used here:
- **Loading Notes**: On page load, jQuery triggers a `GET` request. The server returns a JSON list of notes, and JavaScript builds the HTML rows on the fly.
- **Form Submission**: When you click "Add", the content is serialized into a JSON object and sent via a `POST` request. On a `200 OK` response, the UI is updated immediately.
- **Validation**: If you try to send an empty note, AJAX is blocked by a pre-submission check in JavaScript, saving server resources.

---

## 🏗️ JavaScript & jQuery Utilization

jQuery is used to simplify DOM manipulation and event handling.

### Key Logic:
- **Event Listeners**: `$(document).ready()` ensures script execution only after the DOM is safe. `$('#addBtn').click()` binds the logic to the button.
- **Dynamic HTML Generation**: Inside `loadNotes()`, we iterate through the note objects using `.forEach()` and use **Template Literals** (backticks) to inject HTML variables directly into the document:
  ```javascript
  html += `<div class="note-card">...</div>`;
  $('#notesList').html(html);
  ```
- **Real-time Filtering**: The search bar uses the `input` event. For every character typed, jQuery selects all `.note-card` elements, checks if their text matches the query, and uses `.toggle()` to hide or show them.

---

## 🗄️ Database & SQL (Django ORM)

While we use **SQLite** as the storage engine, the interaction is handled by the **Django Object-Relational Mapper (ORM)**.

### How SQL is generated:
You don't see `SELECT * FROM notes` because the ORM translates Python code into SQL:
- **Create**: `Note.objects.create(content=content)` → `INSERT INTO myapp_note (content) VALUES ('...');`
- **Read**: `Note.objects.all().order_by('-created_at')` → `SELECT * FROM myapp_note ORDER BY created_at DESC;`
- **Delete**: `note.delete()` → `DELETE FROM myapp_note WHERE id = ...;`
- **Update**: `note.save()` → `UPDATE myapp_note SET content = '...' WHERE id = ...;`

This abstraction prevents **SQL Injection** attacks and keeps the backend code clean and manageable.

---

## ⚙️ How to Run Locally

1.  **Install Django**:
    ```bash
    pip install django
    ```
2.  **Set up Database**:
    ```bash
    python manage.py migrate
    ```
3.  **Run Server**:
    ```bash
    python manage.py runserver
    ```
4.  **Access App**:
    Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in any modern browser.
