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

You can run this project using **Docker** (Recommended) or locally using a virtual environment.

***

### Option A: Docker (Recommended)

This is the easiest way to run the project with the PostgreSQL database and Gunicorn server included.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/maxkunev/foodie-app.git
   cd foodie-app
   ```

2. **Set up environment variables:**
   Create a `.env` file in the root directory (you can use `.env.example` as a reference if available) and add your database credentials.

3. **Build and run the containers:**
   ```bash
   docker compose up --build -d
   ```

4. **Apply migrations and create an admin user:**
   ```bash
   docker compose exec web python manage.py migrate
   docker compose exec web python manage.py createsuperuser
   ```

5. **Open in browser:** [http://localhost:8000/](http://localhost:8000/)

***

### Option B: Local Virtual Environment

If you prefer running the app without Docker (using SQLite by default).

1. Clone the repository and navigate to the project folder.

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

***

## 📌 Development Roadmap & Status

Instead of standard checkboxes, here is the evolution of the project's architecture:

- ✅ **Dynamic UI** — Implemented HTMX-powered likes and favourites system.
- ✅ **Advanced Querying** — Added search, sorting, and category filtering.
- ✅ **REST API** — Built with Django REST Framework + drf-spectacular.
- ✅ **Containerization** — Fully containerized with Docker, Gunicorn, and PostgreSQL.
- ✅ **Deployment** — Successfully deployed on a managed PaaS ([Render.com](https://foodie-app-nmct.onrender.com/)).
- 📍 **Architecture Pivot** — Initially planned to manually configure a bare metal Linux server with Nginx. However, shifted to a modern containerized PaaS deployment (Docker + Render + WhiteNoise) to focus on scalable, immutable infrastructure.
- 🔄 **CI/CD Pipeline** — Planned for future iterations (e.g., GitHub Actions).

***

## 🧑‍💻 Author

**Max Kunev** — [github.com/maxkunev](https://github.com/maxkunev)
