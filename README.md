# Online Reading Tracker

Online Reading Tracker is a Django project for saving books, tracking reading
progress, writing reviews, and managing a personal reading library.

The project is planned as a full-stack Django application:

- server-rendered pages with Django Templates;
- user registration, login, logout, and profile settings;
- book catalog with genres, authors, reviews, and reading progress;
- REST API with Django REST Framework;
- token-based API authentication;
- Postman collection for API testing.

---

## Current Project Status

This repository already contains the base Django project and the first version
of the custom users app.

Implemented or started:

- custom user model: `CustomUser`;
- email-based login field;
- user roles: `user`, `moderator`, `admin`;
- user profile fields: `username`, `first_name`, `last_name`, `avatar`, `bio`;
- user settings model: `UserSettings`;
- settings for theme, private profile, and notifications;
- custom user admin draft;
- base Django settings split into `settings/base.py`, `settings/env/dev.py`,
  and `settings/env/prod.py`;
- draft markdown examples for users admin, serializers, views, urls, and apps.

Still needs to be implemented:

- templates and frontend pages;
- forms;
- catalog/book models;
- reading progress models;
- review/favorite models;
- DRF serializers and views in real `.py` files;
- API urls;
- CORS and DRF settings;
- Postman collection.

---

## Group Members

| # | Name | Main Responsibility |
|---|------|---------------------|
| 1 | Saken Ayan | Frontend, Django Templates, CSS, authentication pages |
| 2 | Askarova Akbota | Models, forms, Django views, admin panel, web CRUD |
| 3 | Bisenev Ualikhan | DRF API, serializers, token authentication, Postman collection |

---

## Project Goal

The goal is to build a Django web application where users can:

- create an account and log in;
- browse books;
- filter books by genre or author;
- search books by title;
- open a book detail page;
- add a book to a personal library;
- choose reading status;
- track current page and reading percentage;
- rate completed books;
- write reviews;
- manage profile and user settings.

The project must also demonstrate:

- Django Templates;
- Django forms and ModelForms;
- database relationships;
- customized Django admin;
- Django REST Framework API;
- token authentication;
- protected API endpoints;
- Postman API testing.

---

## Tech Stack

- Python
- Django
- Django Templates
- Django REST Framework
- SQLite for development
- PostgreSQL as an optional production database
- HTML
- CSS
- JavaScript
- django-cors-headers
- Postman
- Git / GitHub

---

## Required Python Packages

Minimum packages for the current project:

```bash
pip install django python-decouple pillow
```

Packages needed for the REST API part:

```bash
pip install djangorestframework django-cors-headers
```

Recommended full install command:

```bash
pip install django python-decouple pillow djangorestframework django-cors-headers
```

After installing dependencies:

```bash
pip freeze > requirements.txt
```

The repository currently also contains `djangorestframework_simplejwt` in
`requirements.txt`. See the JWT note near the end of this README.

---

## Planned Apps

The project can stay simple and use a small number of apps.

```text
apps/
├── users/
├── library/
├── tracker/
└── interactions/
```

### `apps.users`

Already started. Handles:

- custom user model;
- email login;
- user roles;
- avatar and bio;
- user settings;
- API registration/login/profile endpoints later.

### `apps.library`

Planned app for the book catalog. Handles:

- genres;
- authors;
- books;
- book list and detail pages;
- book CRUD for admins or moderators.

### `apps.tracker`

Planned app for personal reading progress. Handles:

- adding books to a user's library;
- reading status;
- current page;
- progress percentage;
- reading dates.

### `apps.interactions`

Planned app for user actions around books. Handles:

- reviews;
- ratings;
- favorites.

If the project needs to stay smaller, `tracker` and `interactions` can be
merged into `library`.

---

## Database Models

The project should include at least 4 models. A good final model set:

```text
CustomUser
UserSettings
Genre
Author
Book
ReadingProgress
Review
Favorite
```

### Already Started

| Model | Description |
|------|-------------|
| CustomUser | Custom user with email login, username, avatar, bio, and role |
| UserSettings | User theme, privacy, and notification settings |

### Planned Models

| Model | Description |
|------|-------------|
| Genre | Stores book genres |
| Author | Stores book authors |
| Book | Stores book title, description, cover, page count, genre, and author |
| ReadingProgress | Connects user and book, stores status and current page |
| Review | Stores user review and rating for a book |
| Favorite | Stores books saved by a user |

### Relationships

```text
CustomUser -> UserSettings
Book -> Genre
Book -> Author
ReadingProgress -> CustomUser
ReadingProgress -> Book
Review -> CustomUser
Review -> Book
Favorite -> CustomUser
Favorite -> Book
```

This gives more than 2 `ForeignKey` relationships, which satisfies the backend
requirement.

---

## Example ERD

```text
CustomUser
 ├── UserSettings
 ├── ReadingProgress
 │    └── Book
 │         ├── Genre
 │         └── Author
 ├── Review
 │    └── Book
 └── Favorite
      └── Book
```

---

## Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Shows list of books |
| Book detail | `/books/<id>/` | Shows book information and reviews |
| Register | `/accounts/register/` | Creates a new user |
| Login | `/accounts/login/` | Logs user in |
| Logout | `/accounts/logout/` | Logs user out |
| Profile | `/profile/` | Shows user profile and settings |
| My library | `/my-library/` | Shows books saved by current user |
| Update progress | `/my-library/<id>/update/` | Updates reading status and current page |
| Add book | `/books/add/` | Adds a new book |
| Edit book | `/books/<id>/edit/` | Updates book information |
| Delete book | `/books/<id>/delete/` | Deletes a book |

---

## Forms

The project should include at least 4 forms.

| Form | Type | Purpose |
|------|------|---------|
| UserRegistrationForm | Django Form / UserCreationForm style | Register users |
| LoginForm | AuthenticationForm | Login users |
| UserSettingsForm | ModelForm | Update theme, privacy, notifications |
| BookForm | ModelForm | Create or update books |
| ReadingProgressForm | ModelForm | Update status and current page |
| ReviewForm | ModelForm | Create or edit reviews |

---

## Event Handlers / User Actions

The project should include at least 4 user actions.

| Action | Description |
|--------|-------------|
| Submit registration form | Creates a user account |
| Submit login form | Authenticates a user |
| Click book detail link | Opens book detail page |
| Submit book form | Creates or updates a book |
| Click add to library | Creates reading progress for current user |
| Submit progress form | Updates reading status/current page |
| Submit review form | Creates a review |
| Click search/filter | Filters books by title, genre, or author |
| Click delete | Deletes a selected object |

---

## API Endpoints

These endpoints are enough for the API and Postman part.

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login/` | Returns API token |
| POST | `/api/auth/logout/` | Deletes or invalidates API token |
| GET | `/api/users/personal-info/` | Returns current user profile |
| PATCH | `/api/users/update-profile/` | Updates current user profile |

### Books API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books/` | Get book list |
| GET | `/api/books/<id>/` | Get book detail |
| POST | `/api/books/create/` | Create a book |
| PUT/PATCH | `/api/books/<id>/update/` | Update a book |
| DELETE | `/api/books/<id>/delete/` | Delete a book |

### Reading Progress API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/progress/` | Get current user's reading progress |
| POST | `/api/progress/create/` | Add a book to personal library |
| PATCH | `/api/progress/<id>/update/` | Update status or current page |

### Reviews API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/reviews/` | Get reviews |
| POST | `/api/reviews/create/` | Create a review |

### Genres API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/genres/` | Get genres |
| POST | `/api/genres/create/` | Create a genre |

---

## Serializers

The project should include both `serializers.Serializer` and
`serializers.ModelSerializer`.

### `serializers.Serializer`

Good examples:

```text
LoginSerializer
LogoutSerializer
ReviewCreateSerializer
```

### `serializers.ModelSerializer`

Good examples:

```text
UserReadSerializer
BookSerializer
GenreSerializer
AuthorSerializer
ReadingProgressSerializer
ReviewSerializer
FavoriteSerializer
```

---

## DRF Views

The project must include both function-based DRF views and class-based views
using `APIView`.

### Function-Based Views

Examples:

```text
api_book_list
api_review_create
api_genre_list
```

### Class-Based Views

Examples:

```text
BookDetailAPIView
BookCreateAPIView
BookUpdateDeleteAPIView
ReadingProgressAPIView
```

---

## Authentication

The project uses two types of authentication.

### 1. Django Template Authentication

Used for the normal website:

- registration;
- login;
- logout;
- protected profile page;
- protected my library page.

### 2. Token-Based API Authentication

Used for API requests.

With DRF token auth, the request header looks like this:

```http
Authorization: Token your_token_here
```

Required apps:

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',
]
```

Basic DRF setting:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
```

---

## CORS

Use `django-cors-headers` if the frontend sends API requests from another
origin.

```python
INSTALLED_APPS = [
    # ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
```

---

## Project Structure

Current simplified structure:

```text
online_reading_tracker/
├── apps/
│   └── users/
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── docs/
├── settings/
│   ├── base.py
│   ├── conf.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── env/
│       ├── dev.py
│       └── prod.py
├── manage.py
├── requirements.txt
└── README.md
```

Suggested final structure:

```text
online_reading_tracker/
├── apps/
│   ├── users/
│   ├── library/
│   ├── tracker/
│   └── interactions/
├── templates/
├── static/
├── postman/
├── settings/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/online-reading-tracker.git
cd online-reading-tracker
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is incomplete:

```bash
pip install django python-decouple pillow djangorestframework django-cors-headers
```

### 5. Create `.env`

Create `settings/.env`:

```env
PROJECT_SECRET_KEY=your-secret-key
PROJECT_ENV_ID=dev
```

### 6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create superuser

```bash
python manage.py createsuperuser
```

### 8. Run server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Important Notes Before Running

- `AUTH_USER_MODEL = 'users.CustomUser'` depends on `UsersConfig.label = 'users'`.
- It is safer to use `'apps.users.apps.UsersConfig'` in `INSTALLED_APPS`.
- `ImageField` requires Pillow.
- The current `apps/users/admin.py` uses `_('...')`, so it should import:

```python
from django.utils.translation import gettext_lazy as _
```

- The API examples in markdown files are not active until copied into real
  `.py` files and DRF is added to `INSTALLED_APPS`.

---

## Requirements Checklist

### Frontend Requirements

- [ ] Dynamic content rendered with Django Templates
- [ ] At least 4 forms
- [ ] At least 4 event handlers / user actions
- [ ] Basic CSS styling
- [ ] At least 3 named paths in `urls.py`
- [ ] Navigation between pages
- [ ] `{% for %}` loops in templates
- [ ] `{% if %}` conditions in templates
- [ ] Registration
- [ ] Login
- [ ] Logout
- [ ] At least 1 custom context processor or template tag
- [ ] Graceful error handling and messages

### Backend Requirements

- [x] Custom user model started
- [x] User settings model started
- [ ] At least 4 models total
- [ ] At least 2 `ForeignKey` relationships
- [ ] Register models in admin
- [ ] Customize admin list display and search
- [ ] Create Django forms / ModelForms
- [ ] Create web views for pages
- [ ] Create list/detail pages
- [ ] Create create/update/delete views for one model
- [ ] Link created objects to `request.user`
- [ ] Add Django messages for success and errors
- [ ] Create at least 3 named URL paths
- [ ] Add one custom template tag or context processor

### API Requirements

- [ ] Install and configure Django REST Framework
- [ ] Configure token authentication
- [ ] Configure `django-cors-headers`
- [ ] Create at least 2 `serializers.Serializer`
- [ ] Create at least 2 `serializers.ModelSerializer`
- [ ] Create API login endpoint
- [ ] Create API logout endpoint
- [ ] Create at least 2 DRF function-based views
- [ ] Create at least 2 DRF class-based views using `APIView`
- [ ] Create API CRUD endpoints for books
- [ ] Protect create/update/delete endpoints with token authentication
- [ ] Link created objects to `request.user`
- [ ] Create Postman collection
- [ ] Add example requests and responses
- [ ] Commit Postman collection to repository

### Defense Requirements

- [x] README file
- [ ] GitHub repository
- [ ] Commit history
- [ ] Postman collection
- [ ] Presentation, maximum 4 pages
- [ ] Live demo: frontend + backend
- [ ] All group members understand frontend and backend parts

---

## Suggested Work Plan

### Step 1 - Finish Users App

- Fix `apps/users/admin.py` imports.
- Add `UsersConfig.label = 'users'`.
- Register `UserSettings` in admin.
- Add user serializers, urls, and API views if API auth is done in `users`.
- Add forms and templates for registration/login/profile if web auth is done in
  `users`.

### Step 2 - Add Library App

Create:

```bash
mkdir -p apps/library
python manage.py startapp library apps/library
```

Models:

- `Genre`
- `Author`
- `Book`

Views/pages:

- book list;
- book detail;
- create book;
- update book;
- delete book.

### Step 3 - Add Tracker App

Create model:

```text
ReadingProgress
```

Fields:

- user;
- book;
- status;
- current page;
- started date;
- finished date;
- progress percentage property.

### Step 4 - Add Interactions

Create:

- `Review`
- `Favorite`

Make sure reviews and favorites are linked to `request.user`.

### Step 5 - Add API

Create:

- serializers;
- function-based API views;
- APIView classes;
- protected endpoints;
- API urls;
- Postman collection.

---

## Team Task Distribution

### Student 1 - Frontend + Django Templates + Styling

Main responsibility:

- templates;
- navigation;
- CSS;
- registration/login pages;
- book list/detail templates;
- my library page;
- forms display;
- success/error messages.

Files mainly edited:

```text
templates/
static/
apps/*/templates/
```

### Student 2 - Models + Forms + Django Web Views + Admin

Main responsibility:

- models;
- ModelForms;
- Django views;
- urls;
- admin customization;
- CRUD pages.

Files mainly edited:

```text
apps/library/models.py
apps/library/forms.py
apps/library/views.py
apps/library/urls.py
apps/library/admin.py
apps/tracker/models.py
apps/interactions/models.py
```

### Student 3 - DRF API + Serializers + Token Auth + Postman

Main responsibility:

- DRF settings;
- serializers;
- token auth;
- API views;
- API urls;
- Postman collection.

Files mainly edited:

```text
apps/users/serializers.py
apps/users/views.py
apps/users/urls.py
apps/library/serializers.py
apps/library/api_views.py
apps/library/api_urls.py
settings/base.py
settings/urls.py
postman/
```

---

## Integration Checklist

- [ ] Pull latest changes from all branches
- [ ] Resolve merge conflicts
- [ ] Run migrations
- [ ] Test admin login
- [ ] Test registration
- [ ] Test login
- [ ] Test logout
- [ ] Test home page
- [ ] Test book detail page
- [ ] Test create form
- [ ] Test update form
- [ ] Test delete function
- [ ] Test API login
- [ ] Test API CRUD in Postman
- [ ] Check that protected API endpoints require token
- [ ] Check that created objects are linked to user
- [ ] Check CSS and navigation
- [ ] Check README
- [ ] Check Postman collection in repository

---

## Git Workflow

Suggested branches:

```text
main
frontend-templates
backend-web
api-drf
```

Basic workflow:

```bash
git checkout main
git pull
git checkout -b your-branch-name
git add .
git commit -m "Describe your changes"
git push origin your-branch-name
```

---

## Defense Plan

The presentation should be maximum 4 pages.

### Slide 1 - Project Overview

- project name;
- group members;
- main idea;
- tech stack.

### Slide 2 - Frontend

- Django Templates;
- pages;
- forms;
- authentication;
- CSS;
- template tags or context processor.

### Slide 3 - Backend and API

- models;
- relationships;
- serializers;
- DRF views;
- token authentication;
- CRUD.

### Slide 4 - Demo and Requirements

- live demo plan;
- Postman collection;
- GitHub repository;
- requirements checklist.

---

## Live Demo Plan

During the demo, show:

1. Home page with dynamic book list
2. Registration
3. Login
4. Profile/settings page
5. Book detail page
6. Add book to my library
7. Update reading progress
8. Create review
9. API login in Postman
10. API GET request
11. API POST request with token
12. API update/delete request
13. GitHub repository with README and commits
14. Postman collection in repository

---

## Common Defense Questions

### What is Django Template?

Django Template is a system that allows HTML pages to display dynamic data from
Django views.

### What is DRF?

Django REST Framework is a library used to build REST APIs in Django.

### What is a serializer?

A serializer converts Django/Python objects into JSON and validates JSON data
before saving it.

### What is the difference between `Serializer` and `ModelSerializer`?

`Serializer` is written manually. `ModelSerializer` is connected to a Django
model and can generate fields automatically.

### What is `ForeignKey`?

`ForeignKey` is a relationship where many objects can be connected to one
object.

Example:

```text
Many reviews can belong to one book.
```

### What is token authentication?

Token authentication allows the API to identify a user by a token sent in the
request header.

### What is CORS?

CORS controls whether a frontend from one origin can send requests to a backend
from another origin.

### What is `request.user`?

`request.user` is the currently authenticated user making the request.

---

## Optional JWT Remark

The mandatory requirement says token-based authentication. The simplest school
version is DRF Token Authentication:

```python
'rest_framework.authtoken'
```

Header:

```http
Authorization: Token your_token_here
```

For a more modern variant, this can be replaced with SimpleJWT:

```bash
pip install djangorestframework-simplejwt
```

Settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

Header:

```http
Authorization: Bearer your_access_token
```

SimpleJWT gives access and refresh tokens, which is usually better for real API
projects. It still satisfies the general idea of token-based authentication,
but if the course specifically expects `rest_framework.authtoken`, use DRF Token
Auth for the final checklist and mention JWT as an improvement.

---

## License

This project is created for educational purposes as part of the Web Development
course.
