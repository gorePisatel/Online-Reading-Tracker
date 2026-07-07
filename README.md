# Online Reading Tracker

Online Reading Tracker is a Django web application for tracking books, reading
progress, reviews, and a personal reading library.

The project combines:

- Django Templates for the frontend;
- Django forms for user interaction;
- Django REST Framework for API endpoints;
- token-based authentication for API requests;
- Postman collection for API testing.

---

## Group Members

| # | Name | Responsibility |
|---|------|----------------|
| 1 | Saken Ayan | Frontend, Django Templates, CSS, auth pages |
| 2 | Askarova Akbota | Models, forms, Django views, admin panel |
| 3 | Bisenev Ualikhan | DRF API, serializers, token auth, Postman |

---

## Project Idea

Users can:

- register, log in, and log out;
- browse books;
- search and filter books;
- open book detail pages;
- add books to their personal library;
- update reading status and current page;
- write reviews and ratings;
- manage basic profile settings.

---

## Current Status

Already started:

- base Django project;
- custom `users` app;
- custom user model draft;
- user settings model draft;
- Django settings structure;
- README and planning documents.

Still needed:

- frontend templates;
- forms;
- book models;
- reading progress model;
- reviews/favorites;
- DRF serializers and API views;
- token authentication;
- Postman collection.

---

## Tech Stack

- Python
- Django
- Django Templates
- Django REST Framework
- SQLite
- HTML / CSS / JavaScript
- django-cors-headers
- Postman
- Git / GitHub

---

## Installation

Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If dependencies are missing:

```bash
pip install django python-decouple pillow djangorestframework django-cors-headers
```

Create `settings/.env`:

```env
PROJECT_SECRET_KEY=your-secret-key
PROJECT_ENV_ID=dev
```

Run migrations and start server:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

For production or hosting with `PROJECT_ENV_ID=prod`, collect static files before
starting the app:

```bash
python manage.py collectstatic --noinput
```

Static CSS, JavaScript, and images are served through WhiteNoise, so make sure
dependencies from `requirements.txt` are installed after pulling the repository.

Open:

```text
http://127.0.0.1:8000/
```

---

## Planned Apps

Simple version:

```text
apps/
├── users/
├── library/
└── tracker/
```

### `users`

Handles:

- registration;
- login/logout;
- user profile;
- user settings;
- roles: user, moderator, admin.

### `library`

Handles:

- genres;
- authors;
- books;
- book list/detail pages;
- book CRUD.

### `tracker`

Handles:

- reading progress;
- reading status;
- reviews;
- favorites.

Reviews and favorites can be placed here to keep the project smaller.

---

## Models

Planned models:

| Model | Purpose |
|-------|---------|
| CustomUser | User profile and roles |
| UserSettings | Theme, privacy, notifications |
| Genre | Book genres |
| Author | Book authors |
| Book | Book information |
| ReadingProgress | User reading status and current page |
| Review | User review and rating |
| Favorite | Saved books |

Required relationships:

```text
Book -> Genre
Book -> Author
ReadingProgress -> User
ReadingProgress -> Book
Review -> User
Review -> Book
Favorite -> User
Favorite -> Book
```

This satisfies the requirement for at least 4 models and at least 2
`ForeignKey` relationships.

---

## Main Pages

| Page | URL |
|------|-----|
| Home / book list | `/` |
| Book detail | `/books/<id>/` |
| Register | `/accounts/register/` |
| Login | `/accounts/login/` |
| Logout | `/accounts/logout/` |
| My library | `/my-library/` |
| Update progress | `/my-library/<id>/update/` |
| Create book | `/books/create/` |
| Update book | `/books/<id>/update/` |
| Delete book | `/books/<id>/delete/` |

---

## Forms

The project should include at least 4 forms:

- registration form;
- login form;
- book form;
- reading progress form;
- review form;
- user settings form.

---

## API Endpoints

### Auth

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login/` | Get token |
| POST | `/api/auth/logout/` | Logout / delete token |

### Books

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books/` | Book list |
| GET | `/api/books/<id>/` | Book detail |
| POST | `/api/books/create/` | Create book |
| PATCH | `/api/books/<id>/update/` | Update book |
| DELETE | `/api/books/<id>/delete/` | Delete book |

### Progress and Reviews

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/progress/` | Current user's progress |
| POST | `/api/progress/create/` | Add book to library |
| PATCH | `/api/progress/<id>/update/` | Update progress |
| GET | `/api/reviews/` | Review list |
| POST | `/api/reviews/create/` | Create review |

---

## DRF Requirements

The API part must include:

- at least 2 `serializers.Serializer`;
- at least 2 `serializers.ModelSerializer`;
- at least 2 function-based DRF views;
- at least 2 class-based views using `APIView`;
- token login endpoint;
- token logout endpoint;
- protected create/update/delete endpoints;
- objects linked to `request.user`.

---

## Token Authentication

Basic required version:

```python
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]
```

Request header:

```http
Authorization: Token your_token_here
```

Optional improvement: SimpleJWT can be used instead of DRF Token Auth if allowed.

---

## CORS

Use `django-cors-headers`:

```python
INSTALLED_APPS = [
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]
```

---

## Final Requirements Checklist

### Frontend

- [ ] Django Templates
- [ ] At least 4 forms
- [ ] At least 4 user actions
- [ ] Basic CSS
- [ ] At least 3 named URL paths
- [ ] Navigation between pages
- [ ] `{% for %}` loops
- [ ] `{% if %}` conditions
- [ ] Registration
- [ ] Login
- [ ] Logout
- [ ] Custom context processor or template tag
- [ ] Error/success messages

### Backend

- [ ] At least 4 models
- [ ] At least 2 `ForeignKey` relationships
- [ ] Admin customization
- [ ] Full CRUD for at least one model
- [ ] Created objects linked to `request.user`

### API

- [ ] DRF configured
- [ ] Token authentication
- [ ] CORS configured
- [ ] 2+ `serializers.Serializer`
- [ ] 2+ `serializers.ModelSerializer`
- [ ] 2+ DRF function-based views
- [ ] 2+ `APIView` class-based views
- [ ] Login/logout API endpoints
- [ ] Protected CRUD endpoints
- [ ] Postman collection

### Defense

- [ ] GitHub repository
- [ ] Commit history
- [ ] README.md
- [ ] Postman collection
- [ ] Presentation, maximum 4 pages
- [ ] Live demo
- [ ] All members can explain frontend and backend

---

## Notes

Detailed task distribution can be kept in `TASK_DISTRIBUTION.md`.

Detailed experimental code variants can stay in separate markdown files, for
example:

- `apps_users_simplified.md`
- `apps_users_serializers_1.md`
- `apps_users_views_1.md`
- `apps_users_urls_1.md`
