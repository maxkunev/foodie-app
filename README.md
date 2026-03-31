# 🍲 Foodie App

A Django-based web application for managing and exploring recipes, featuring browsing, searching, filtering, and user interaction.

> Originally started as part of a Packt Django course (https://www.coursera.org/learn/packt-django-python-web-framework-the-comprehensive-guide-6ba4j), but has been significantly expanded — with fixed architectural issues, new functionality, improved UX/UI, and more production-ready solutions. At this point, it is a fully developed pet project.

---

## ✨ Features

- Browse recipes
- Search functionality
- Category filtering
- Custom pagination with improved UX logic
- Comments system
- User registration and authentication
- Profile photo upload
- Improved form validation

---

## 🧠 Technical Highlights

- Custom pagination with dynamic window logic
- Separation of concerns via `utils.py`
- Django Paginator integration
- Clean, reusable template structure
- Bootstrap-based UI

---

## 🗂️ Project Structure

- foodie_app/ # Home page logic
- djangocoursera/ # Project settings
- accounts/ # Authentication and user management
- comments/ # Comments system
- recipes/ # Core recipe logic
- templates/ # HTML templates
- static/ # Static files (CSS, images)
- media/ # User-uploaded media

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/maxkunev/foodie-app.git
cd foodie-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

### 6. Open in browser

- http://127.0.0.1:8000/


---

## 📌 Planned Improvements

- Likes system
- Full-text search
- REST API (Django REST Framework)
- Deploying on a **bare Linux server** (e.g. Ubuntu)
- Full manual setup of:
  - Nginx
  - Gunicorn
  - PostgreSQL
  - Environment variables and security
- Containerization with **Docker**
- CI/CD pipeline integration

---

## 🧑‍💻 Author

**Max Kunev** — [github.com/maxkunev](https://github.com/maxkunev)

---

