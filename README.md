# 🍲 Foodie App

A Django-based web application for managing and exploring recipes, featuring browsing, searching, filtering, and user interaction.

> Originally started as part of a [Packt Django course](https://www.coursera.org/learn/packt-django-python-web-framework-the-comprehensive-guide-6ba4j), but has been significantly expanded — with fixed architectural issues, new functionality, improved UX/UI, and production-ready solutions. At this point, it is a fully developed pet project.

🚀 **Live demo:** [foodie-app-nmct.onrender.com](https://foodie-app-nmct.onrender.com/)

***

## ✨ Features

- Browse recipes
- Search functionality with advanced filtering and sorting
- Category filtering
- Custom pagination with improved UX logic
- Comments system
- User registration and authentication
- Profile photo upload
- Improved form validation
- ❤️ Likes / favourites system powered by HTMX/AJAX-request
- Persistent dark mode toggle for authenticated users
- In-memory caching for search and filtering results
- REST API with auto-generated documentation (DRF + drf-spectacular)

***

## 🧠 Technical Highlights

- Custom pagination with dynamic window logic
- Separation of concerns via `utils.py`
- Django Paginator integration
- Clean, reusable template structure
- Bootstrap-based UI
- HTMX for dynamic interactions without full page reloads
- Django REST Framework with drf-spectacular (OpenAPI/Swagger docs)
- Cloudinary integration for media storage
- WhiteNoise for static file serving
- PostgreSQL as the production database
- Gunicorn as the production WSGI server
- Docker + Docker Compose for containerized deployment
- Comprehensive test suite with API permission coverage
- Environment variables via `.env` and `dj-database-url`

***

## 🗂️ Project Structure

```
foodie_app/         # Home page logic
djangocoursera/     # Project settings
accounts/           # Authentication and user management
comments/           # Comments system
recipes/            # Core recipe logic
templates/          # HTML templates
static/             # Static files (CSS, images)
media/              # User-uploaded media
```

***

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

> For Docker-based setup, see `docker-compose.yml` in the repository root.

***

## 📌 Improvements Roadmap

- [x] Likes system (HTMX-powered)
- [x] Advanced search, sorting, and category filtering
- [x] REST API (Django REST Framework + drf-spectacular)
- [x] Deployed on Render.com (managed environment)
- [ ] ~~Bare Linux server setup (Nginx, Gunicorn, PostgreSQL)~~ — *decided to use a managed platform (Render) instead, which handles infrastructure concerns*
- [x] Containerization with Docker
- [ ] CI/CD pipeline — *not implemented; considered out of scope for current stage*

***

## 🧑‍💻 Author

**Max Kunev** — [github.com/maxkunev](https://github.com/maxkunev)
