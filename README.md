# MangaShelf — Django Templates + Django REST Framework Project

MangaShelf is a web application for browsing manga/books, managing genres, writing reviews, and saving favorite titles.  
The project includes a server-rendered frontend using **Django Templates** and a REST API using **Django REST Framework**.

> Replace the project name and group member names if your actual project has a different topic.

---

## Group Members

| # | Name | Main Responsibility |
|---|------|---------------------|
| 1 | Saken Ayan | Frontend, Django Templates, CSS, authentication pages |
| 2 | Askarova Akbota | Models, forms, Django views, admin panel, web CRUD |
| 3 | Bisenev Ualikhan | DRF API, serializers, token authentication, Postman collection |

---

## Project Goal

The goal of this project is to build a full-stack Django web application that demonstrates:

- dynamic pages rendered with Django Templates;
- user registration, login, and logout;
- database models with relationships;
- forms for user interaction;
- API endpoints using Django REST Framework;
- token-based authentication for API requests;
- full CRUD operations for at least one model;
- integration between frontend and backend;
- clear documentation and Postman API testing.

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Django Templates
- SQLite / PostgreSQL
- HTML
- CSS
- JavaScript
- django-cors-headers
- Postman
- Git / GitHub

---

## Main Features

### Frontend Features

- Home page with list of manga/books
- Detail page for each title
- Registration page
- Login and logout
- Dashboard for authenticated users
- Create/edit/delete content through forms
- Search or filter by genre
- Display success and error messages
- Basic responsive CSS styling

### Backend Features

- Database models with relationships
- Admin panel customization
- Django forms and ModelForms
- REST API with DRF
- Serializer and ModelSerializer usage
- Function-Based API Views
- Class-Based API Views using APIView
- Token-based login and logout
- CRUD API endpoints
- Objects linked to `request.user`
- CORS configuration
- Postman collection with example requests and responses

---

## Database Models

The project uses at least 4 models:

```text
Genre
Book
Review
Favorite
```

### Model Relationships

```text
Book → Genre
Review → User
Review → Book
Favorite → User
Favorite → Book
```

### Suggested Model Description

| Model | Description |
|------|-------------|
| Genre | Stores genres such as Action, Drama, Fantasy, Romance |
| Book | Stores manga/book information |
| Review | Stores user reviews and ratings |
| Favorite | Stores titles saved by users |

---

## Example ERD

```text
User
 ├── Review
 │     └── Book
 │           └── Genre
 └── Favorite
       └── Book
             └── Genre
```

---

## Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Shows list of books/manga |
| Detail | `/books/<id>/` | Shows detailed information |
| Register | `/accounts/register/` | Creates a new user |
| Login | `/accounts/login/` | Logs user in |
| Logout | `/accounts/logout/` | Logs user out |
| Dashboard | `/dashboard/` | Shows user-related data |
| Create Book | `/books/create/` | Creates a new book/manga |
| Create Review | `/reviews/create/` | Creates a review |
| Edit Book | `/books/<id>/edit/` | Updates book/manga information |
| Delete Book | `/books/<id>/delete/` | Deletes a book/manga |

---

## Forms

The project includes at least 4 forms:

| Form | Type | Purpose |
|------|------|---------|
| User Registration Form | Django Form / UserCreationForm | Register new users |
| Login Form | Django AuthenticationForm | Login existing users |
| Book Form | ModelForm | Create or update books/manga |
| Review Form | ModelForm | Create reviews |
| Genre Form | ModelForm | Create genres |

---

## Event Handlers / User Actions

The project includes at least 4 user actions:

| Action | Description |
|--------|-------------|
| Submit registration form | Creates a user account |
| Submit login form | Authenticates a user |
| Submit book form | Creates or updates a book |
| Submit review form | Creates a review |
| Click detail link | Opens detail page |
| Click filter/search button | Filters content by genre or search query |
| Click delete button | Deletes selected object |

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login/` | Returns auth token |
| POST | `/api/auth/logout/` | Deletes or invalidates auth token |

### Books API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books/` | Get list of books |
| GET | `/api/books/<id>/` | Get book details |
| POST | `/api/books/create/` | Create a book |
| PUT/PATCH | `/api/books/<id>/update/` | Update a book |
| DELETE | `/api/books/<id>/delete/` | Delete a book |

### Reviews API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/reviews/` | Get list of reviews |
| POST | `/api/reviews/create/` | Create a review |

### Genres API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/genres/` | Get list of genres |
| POST | `/api/genres/create/` | Create a genre |

---

## Serializers

The project includes both regular serializers and model serializers.

### `serializers.Serializer`

Used for custom validation and manual fields.

Examples:

```text
LoginSerializer
ReviewCreateSerializer
```

### `serializers.ModelSerializer`

Used for models.

Examples:

```text
BookSerializer
GenreSerializer
ReviewSerializer
FavoriteSerializer
```

---

## DRF Views

The project includes both Function-Based Views and Class-Based Views.

### Function-Based Views

Examples:

```text
api_book_list
api_review_create
```

### Class-Based Views

Examples:

```text
BookDetailAPIView
BookCRUDAPIView
```

---

## Authentication

The project uses two types of authentication:

### 1. Django Template Authentication

Used for the website:

- registration;
- login;
- logout;
- protected dashboard page.

### 2. Token-Based API Authentication

Used for API requests.

Example header:

```http
Authorization: Token your_token_here
```

---

## CORS

The project uses `django-cors-headers` to allow frontend requests to the backend API.

Example configuration:

```python
INSTALLED_APPS = [
    ...
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
```

---

## Project Structure

```text
mangashelf/
│
├── manage.py
├── requirements.txt
├── README.md
├── postman/
│   └── MangaShelf.postman_collection.json
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── catalog/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── serializers.py
│   ├── api_views.py
│   ├── templatetags/
│   │   └── catalog_tags.py
│   └── templates/
│       └── catalog/
│           ├── home.html
│           ├── book_detail.html
│           ├── book_form.html
│           ├── review_form.html
│           └── dashboard.html
│
├── accounts/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── accounts/
│           ├── register.html
│           └── login.html
│
└── static/
    └── css/
        └── style.css
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Run server

```bash
python manage.py runserver
```

### 8. Open project

```text
http://127.0.0.1:8000/
```

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

- [ ] At least 4 models
- [ ] At least 2 ForeignKey relationships
- [ ] At least 2 serializers using `serializers.Serializer`
- [ ] At least 2 serializers using `serializers.ModelSerializer`
- [ ] At least 2 DRF Function-Based Views
- [ ] At least 2 DRF Class-Based Views using `APIView`
- [ ] Token-based authentication
- [ ] Login/logout API endpoints
- [ ] Full CRUD for at least one model
- [ ] Created objects linked to `request.user`
- [ ] CORS configured
- [ ] Postman collection committed to repository

### Defense Requirements

- [ ] README file
- [ ] GitHub repository
- [ ] Commit history
- [ ] Postman collection
- [ ] Presentation, maximum 4 pages
- [ ] Live demo: frontend + backend
- [ ] All group members understand frontend and backend parts

---

# What To Do First

Before dividing the work, the group should complete a small shared setup.  
This avoids merge conflicts and makes the tasks more independent.

## Step 1 — Agree on project topic

Recommended topic:

```text
MangaShelf — manga/book catalog with reviews and favorites
```

## Step 2 — Create GitHub repository

One person creates the repository and adds all group members as collaborators.

## Step 3 — Create base Django project

```bash
django-admin startproject config .
python manage.py startapp catalog
python manage.py startapp accounts
```

## Step 4 — Install required packages

```bash
pip install django djangorestframework django-cors-headers
pip freeze > requirements.txt
```

## Step 5 — Configure installed apps

Add these apps to `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "catalog",
    "accounts",
]
```

## Step 6 — Create base models

Create the shared models first:

```text
Genre
Book
Review
Favorite
```

After that, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 7 — Push the initial project

```bash
git add .
git commit -m "Initial Django project setup"
git push
```

## Step 8 — Create separate branches

Each group member should work in a separate branch:

```bash
git checkout -b frontend-templates
git checkout -b backend-web
git checkout -b api-drf
```

---

# Team Task Distribution

The tasks below are designed so that 3 people can work mostly independently after the base setup is finished.

---

## Student 1 — Frontend + Django Templates + Styling

### Main Responsibility

Build the visible website pages using Django Templates, HTML, CSS, and basic JavaScript.

### Tasks

- [ ] Create `base.html`
- [ ] Create navigation bar
- [ ] Create home page template
- [ ] Create book/manga list page
- [ ] Create book/manga detail page
- [ ] Create dashboard template
- [ ] Create registration page template
- [ ] Create login page template
- [ ] Create book form template
- [ ] Create review form template
- [ ] Add `{% for %}` loops for lists
- [ ] Add `{% if %}` conditions for empty states and authentication checks
- [ ] Add CSS styling in `static/css/style.css`
- [ ] Add buttons and links for user actions
- [ ] Add search/filter UI
- [ ] Add frontend error and success message display
- [ ] Make pages visually consistent

### Files Mainly Edited

```text
templates/
static/css/style.css
catalog/templates/
accounts/templates/
```

### What This Person Should Explain During Defense

- How Django Templates receive data from views
- How `{% for %}` and `{% if %}` work
- How template inheritance works with `base.html`
- How navigation between pages works
- How forms are displayed in templates

---

## Student 2 — Models + Forms + Django Web Views + Admin

### Main Responsibility

Build the database structure and normal Django website logic.

### Tasks

- [ ] Create `Genre` model
- [ ] Create `Book` model
- [ ] Create `Review` model
- [ ] Create `Favorite` model
- [ ] Add at least 2 `ForeignKey` relationships
- [ ] Register models in `admin.py`
- [ ] Customize admin list display and search
- [ ] Create `BookForm`
- [ ] Create `ReviewForm`
- [ ] Create `GenreForm`
- [ ] Create function-based or class-based Django views for pages
- [ ] Create list view for books/manga
- [ ] Create detail view
- [ ] Create create/update/delete views for one model
- [ ] Link created objects to `request.user`
- [ ] Add Django messages for success and errors
- [ ] Create at least 3 named URL paths
- [ ] Add one custom template tag or context processor

### Files Mainly Edited

```text
catalog/models.py
catalog/forms.py
catalog/views.py
catalog/urls.py
catalog/admin.py
catalog/templatetags/
```

### What This Person Should Explain During Defense

- What each model does
- How `ForeignKey` relationships work
- What `ModelForm` does
- How CRUD works in Django
- How `request.user` is used
- How admin customization works

---

## Student 3 — DRF API + Serializers + Token Auth + Postman

### Main Responsibility

Build the REST API and prepare API testing through Postman.

### Tasks

- [ ] Install and configure Django REST Framework
- [ ] Install and configure `rest_framework.authtoken`
- [ ] Configure `django-cors-headers`
- [ ] Create at least 2 `serializers.Serializer`
- [ ] Create at least 2 `serializers.ModelSerializer`
- [ ] Create API login endpoint
- [ ] Create API logout endpoint
- [ ] Create at least 2 DRF Function-Based Views
- [ ] Create at least 2 DRF Class-Based Views using `APIView`
- [ ] Create `GET /api/books/`
- [ ] Create `GET /api/books/<id>/`
- [ ] Create `POST /api/books/create/`
- [ ] Create `PUT/PATCH /api/books/<id>/update/`
- [ ] Create `DELETE /api/books/<id>/delete/`
- [ ] Protect create/update/delete endpoints with token authentication
- [ ] Make sure created objects are linked to `request.user`
- [ ] Create Postman collection
- [ ] Add example requests and responses
- [ ] Commit Postman collection to repository

### Files Mainly Edited

```text
catalog/serializers.py
catalog/api_views.py
catalog/api_urls.py
config/settings.py
config/urls.py
postman/
```

### What This Person Should Explain During Defense

- What serializers do
- Difference between `Serializer` and `ModelSerializer`
- Difference between FBV and APIView
- How token authentication works
- How API CRUD works
- What CORS is needed for
- How Postman collection was prepared

---

# Integration Plan

After everyone finishes their part, the group should integrate the project.

## Integration Checklist

- [ ] Pull latest changes from all branches
- [ ] Resolve merge conflicts
- [ ] Run migrations
- [ ] Test registration
- [ ] Test login
- [ ] Test logout
- [ ] Test home page
- [ ] Test detail page
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

# Git Workflow

## Branches

```text
main
frontend-templates
backend-web
api-drf
```

## Basic workflow

```bash
git checkout main
git pull

git checkout -b your-branch-name

# work on your task

git add .
git commit -m "Describe your changes"
git push origin your-branch-name
```

After finishing a task, create a Pull Request on GitHub.

---

# Suggested Commit Examples

```text
Initial Django project setup
Add catalog models
Add authentication pages
Add book list and detail templates
Add book CRUD forms
Add DRF serializers
Add API authentication endpoints
Add Postman collection
Update README
Fix template navigation
Improve CSS styling
```

---

# Defense Plan

The presentation should be maximum 4 pages.

## Slide 1 — Project Overview

- Project name
- Group members
- Main idea
- Tech stack

## Slide 2 — Frontend

- Django Templates
- Pages
- Forms
- Authentication
- CSS
- Template tags or context processor

## Slide 3 — Backend and API

- Models
- Relationships
- Serializers
- DRF views
- Token authentication
- CRUD

## Slide 4 — Demo and Requirements

- What will be shown in the live demo
- Postman collection
- GitHub repository
- Requirements checklist

---

# Live Demo Plan

During the demo, show:

1. Home page with dynamic list of books/manga
2. Registration
3. Login
4. Dashboard
5. Create book or review through form
6. Update or delete object
7. API login in Postman
8. API GET request
9. API POST request with token
10. API update/delete request
11. GitHub repository with README and commits
12. Postman collection in repository

---

# Common Defense Questions

## What is Django Template?

Django Template is a system that allows HTML pages to display dynamic data from Django views.

## What is DRF?

Django REST Framework is a library used to build REST APIs in Django.

## What is a serializer?

A serializer converts Django/Python objects into JSON and validates JSON data before saving it.

## What is the difference between `Serializer` and `ModelSerializer`?

`Serializer` is written manually.  
`ModelSerializer` is connected to a Django model and can generate fields automatically.

## What is `ForeignKey`?

`ForeignKey` is a relationship where many objects can be connected to one object.

Example:

```text
Many reviews can belong to one book.
```

## What is token authentication?

Token authentication allows the API to identify a user by a special token sent in the request header.

## What is CORS?

CORS controls whether a frontend from one origin can send requests to a backend from another origin.

## What is `request.user`?

`request.user` is the currently authenticated user making the request.

---

## Project Status

| Part | Status |
|------|--------|
| Frontend templates | Not started |
| Django models | Not started |
| Forms | Not started |
| Web views | Not started |
| Authentication | Not started |
| DRF API | Not started |
| Postman collection | Not started |
| Presentation | Not started |

---

## License

This project is created for educational purposes as part of the Web Development course.
