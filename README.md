# Online Reading Tracker

Online Reading Tracker is a Django web application for browsing books, reading
books in a simple reader, tracking personal reading progress, and leaving
reviews.

The project combines:

- Django Templates for the frontend;
- Django forms for user interaction;
- Django REST Framework for API endpoints;
- token-based API authentication;
- SQLite for local development;
- Postman requests for API testing.

## Group Members

| # | Name | Responsibility |
|---|------|----------------|
| 1 | Saken Ayan | Frontend, Django Templates, CSS, auth pages |
| 2 | Askarova Akbota | Models, forms, Django views, admin panel |
| 3 | Bisenev Ualikhan | DRF API, serializers, token auth, Postman |

## Features

- Register, log in, and log out.
- Browse all books on the home page.
- Search books by title.
- Filter books by genre.
- Open a book detail page.
- Read a book at `/<book_id>/read/`.
- Calculate `total_pages` automatically from book text using the reader's
  default page size.
- Automatically add a book to the user's library when an authenticated user
  opens the reader.
- Save the user's last reader page and resume reading from that page.
- Add a book to My Library from the book detail page.
- Update reading status and current page.
- Leave reviews and 1-5 ratings as an authenticated user.
- View reviews and average rating as any visitor.
- Manage user profile settings and theme.
- Manage books, genres, users, progress, and reviews in Django Admin.

## Tech Stack

- Python
- Django
- Django Templates
- Django REST Framework
- SQLite
- HTML / CSS / JavaScript
- django-cors-headers
- WhiteNoise
- Postman

## Project Structure

```text
online_reading_tracker/
├── apps/
│   ├── library/
│   │   ├── models.py          # Genre, Book
│   │   ├── views.py           # catalog, detail, reader, book CRUD pages
│   │   ├── serializers.py     # book and genre API serializers
│   │   ├── api_views.py       # book and genre API views
│   │   ├── urls.py            # frontend book routes
│   │   └── api_urls.py        # API book routes
│   ├── tracker/
│   │   ├── models.py          # ReadingProgress, Review
│   │   ├── views.py           # My Library, progress, reviews
│   │   ├── serializers.py     # progress and review API serializers
│   │   ├── api_views.py       # progress and review API views
│   │   ├── urls.py            # frontend tracker routes
│   │   └── api_urls.py        # API tracker routes
│   └── users/
│       ├── models.py          # CustomUser, UserSettings
│       ├── views.py           # register, profile, settings, theme
│       ├── serializers.py     # user API serializers
│       ├── api_views.py       # token auth and profile API views
│       ├── urls.py            # frontend auth/profile routes
│       └── api_urls.py        # API user routes
├── settings/
│   ├── base.py                # installed apps, middleware, static/media, auth
│   ├── urls.py                # root urls
│   └── env/
│       ├── dev.py             # development settings
│       └── prod.py            # production settings
├── templates/
│   ├── base.html
│   ├── library/               # catalog, detail, reader, book forms
│   ├── tracker/               # my library, progress/review forms
│   └── users/                 # login, register, profile, settings
├── static/
│   ├── css/style.css
│   ├── js/theme.js
│   └── images/
├── media/                     # uploaded covers and avatars in development
├── docs/
│   ├── dbdiagram/             # exported ERD images/PDF
│   └── some_documents/        # requirements and DBML source
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `settings/.env`:

```env
PROJECT_SECRET_KEY=your-secret-key
PROJECT_ENV_ID=dev
```

Run migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Main Pages

| Page | URL |
|------|-----|
| Home / book list | `/` |
| Book detail | `/<book_id>/` |
| Book reader | `/<book_id>/read/` |
| Create book | `/create/` |
| Update book | `/<book_id>/update/` |
| Delete book | `/<book_id>/delete/` |
| Register | `/auth/register/` |
| Login | `/auth/login/` |
| Logout | `/auth/logout/` |
| Profile | `/auth/profile/` |
| Settings | `/auth/settings/` |
| My Library | `/my-library/` |
| Add to library | `/my-library/add/<book_id>/` |
| Update progress | `/my-library/progress/<progress_id>/` |
| Create review | `/my-library/review/<book_id>/` |
| Admin | `/admin/` |

## Models

| Model | Purpose |
|-------|---------|
| CustomUser | User account, profile fields, and role |
| UserSettings | Theme and user preferences |
| Genre | Book genre |
| Book | Book metadata, cover, description, and text |
| ReadingProgress | User's saved book, status, and current page |
| Review | User review text and rating |

Important relationships:

- `Book -> Genre`
- `Book -> CustomUser` through `created_by`
- `ReadingProgress -> CustomUser`
- `ReadingProgress -> Book`
- `Review -> CustomUser`
- `Review -> Book`

## Forms

- Registration form.
- User profile/settings form.
- Book form.
- Reading progress form.
- Review form.
- Login form through Django auth views.

## API Endpoints

Base URL:

```text
http://127.0.0.1:8000
```

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/users/register/` | Register user |
| POST | `/api/users/login/` | Get token |
| POST | `/api/users/logout/` | Delete token |
| GET | `/api/users/me/` | Current user |
| PATCH | `/api/users/me/update/` | Update profile |

### Books and Genres

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books/` | Book list |
| GET | `/api/books/?search=1984` | Search books |
| GET | `/api/books/?genre=3` | Filter by genre |
| GET | `/api/books/<book_id>/` | Book detail |
| POST | `/api/books/create/` | Create book |
| PATCH | `/api/books/<book_id>/update/` | Update book |
| DELETE | `/api/books/<book_id>/delete/` | Delete book |
| GET | `/api/books/genres/` | Genre list |
| POST | `/api/books/genres/create/` | Create genre |

Book API supports the `text` field, so book text can be created or updated
through Postman/API as well as through Django Admin.
The `total_pages` field is read-only and is recalculated automatically from
the book text.

### Progress and Reviews

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tracker/progress/` | Current user's progress |
| POST | `/api/tracker/progress/create/` | Add book to library |
| PATCH | `/api/tracker/progress/<progress_id>/update/` | Update progress |
| GET | `/api/tracker/reviews/` | Review list |
| POST | `/api/tracker/reviews/create/` | Create review |

Protected endpoints require:

```http
Authorization: Token your_token_here
```

## Postman

The tested Postman collection and local environment are included in the
repository:

```text
postman/online-reading-tracker.postman_collection.json
postman/online-reading-tracker.postman_environment.json
```

The environment can contain:

```text
base_url = http://127.0.0.1:8000
token = your_token_here
```

## Requirements Checklist

### Frontend

- [x] Django Templates.
- [x] At least 4 forms.
- [x] At least 4 user actions.
- [x] Basic CSS.
- [x] At least 3 named URL paths.
- [x] Navigation between pages.
- [x] `{% for %}` loops.
- [x] `{% if %}` conditions.
- [x] Registration.
- [x] Login.
- [x] Logout.
- [x] Custom context processor.
- [x] Error/success messages.

### Backend

- [x] At least 4 models.
- [x] At least 2 `ForeignKey` relationships.
- [x] Admin customization.
- [x] Full CRUD for Book through API and admin.
- [x] Created books, progress, and reviews linked to `request.user`.

### API

- [x] DRF configured.
- [x] Token authentication.
- [x] CORS configured.
- [x] 2+ `serializers.Serializer`.
- [x] 2+ `serializers.ModelSerializer`.
- [x] 2+ DRF function-based views.
- [x] 2+ `APIView` class-based views.
- [x] Login/logout API endpoints.
- [x] Protected create/update/delete endpoints.
- [x] Postman collection exported and committed.

## What Can Be Added Next

These are optional improvements. The current project already covers the main
course requirements, but these would make the demo stronger:

- Add automated tests for auth, book API, reader progress, and review creation.
- Add pagination to the book catalog and review list.
- Add review editing/deleting for the review owner.
- Add "remove from My Library" functionality.
- Add API endpoints for reading progress from the reader, if it needs to be
  demonstrated in Postman.
- Add a favicon to avoid `/favicon.ico` 404 logs during local demos.
- Add production deployment notes if the project will be hosted.

## Demo Flow

1. Register or log in.
2. Browse `/`, search and filter books.
3. Open a book detail page.
4. Show the Description and Reviews tabs.
5. Add a review and show the updated rating.
6. Click `Start reading`.
7. Move several pages forward in the reader.
8. Open `/my-library/` and show that the book was saved automatically with the
   saved page progress.
9. Click `Continue Reading` and show that the reader resumes from the saved
   page.
10. Update reading progress manually.
11. Show API login and a protected API request in Postman.
