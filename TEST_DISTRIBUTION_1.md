# Online Reading Tracker - Team Task Distribution

Этот файл нужен, чтобы каждому участнику было понятно:

- что именно он делает;
- какие файлы в основном трогает;
- как проверить, что задача готова;
- что показывать на защите.

Статусы для чекбоксов:

- `[ ]` не начато
- `[~]` в процессе
- `[x]` готово
- `[?]` вопрос / блокер

---

## Общая структура проекта

Чтобы не усложнять проект, делаем 3 приложения:

```text
apps/
├── users/
├── library/
└── tracker/
```

### `apps.users`

Пользователи, регистрация, логин, настройки профиля.

Модели:

```text
CustomUser
UserSettings
```

### `apps.library`

Общий каталог книг.

Модели:

```text
Genre
Book
```

### `apps.tracker`

Личная библиотека пользователя, прогресс чтения, отзывы.

Модели:

```text
ReadingProgress
Review
```

Итого 6 моделей. Этого достаточно для требования `at least 4 models`.

---

## Кто за что отвечает

| Участник | Основная зона | Коротко |
|----------|---------------|---------|
| Student 1 - Saken Ayan | Frontend | Templates, CSS, страницы, формы на HTML |
| Student 2 - Askarova Akbota | Backend Web | Models, forms, Django views, admin, web CRUD |
| Student 3 - Bisenev Ualikhan | API | DRF, serializers, token auth, Postman |

---

## Общие правила работы

- [ ] Каждый работает в своей ветке.
- [ ] Никто не пушит напрямую в `main`.
- [ ] Перед началом новой задачи нужно сделать `git pull`.
- [ ] После завершения задачи создается Pull Request.
- [ ] Перед merge нужно проверить, что проект запускается.
- [ ] Если добавлены модели, нужно сделать migrations.
- [ ] Если добавлены зависимости, нужно обновить `requirements.txt`.

Ветки:

```text
frontend-templates
backend-web
api-drf
```

---

# Student 1 - Frontend, Templates, CSS

## Главная цель

Сделать видимые страницы сайта через Django Templates:

- общая база сайта;
- навигация;
- страницы книг;
- страницы регистрации/login;
- личная библиотека;
- формы;
- базовый CSS.

## Основные файлы

```text
templates/base.html
static/css/style.css
apps/users/templates/users/
apps/library/templates/library/
apps/tracker/templates/tracker/
```

## Задачи

### 1. Base Template

- [ ] Создать `templates/base.html`.
- [ ] Добавить HTML-структуру страницы.
- [ ] Подключить CSS.
- [ ] Добавить navbar.
- [ ] Добавить ссылки: Home, Books, My Library, Login, Register, Logout.
- [ ] Добавить блок для Django messages.
- [ ] Добавить `{% block title %}`.
- [ ] Добавить `{% block content %}`.

Проверка:

- [ ] Все страницы наследуются от `base.html`.
- [ ] Navbar отображается на всех страницах.
- [ ] Messages отображаются, если backend их передает.

### 2. CSS

- [ ] Создать `static/css/style.css`.
- [ ] Стилизовать navbar.
- [ ] Стилизовать forms.
- [ ] Стилизовать кнопки.
- [ ] Стилизовать список книг.
- [ ] Стилизовать карточку/детальную страницу книги.
- [ ] Стилизовать my library.
- [ ] Добавить простую адаптивность.

Проверка:

- [ ] Страницы выглядят аккуратно.
- [ ] Формы не разваливаются.
- [ ] На маленьком экране всё читаемо.

### 3. Users Templates

- [ ] Создать `users/register.html`.
- [ ] Создать `users/login.html`.
- [ ] Создать `users/profile.html`, если будет profile/settings page.
- [ ] Показать форму регистрации.
- [ ] Показать форму логина.
- [ ] Показать ошибки формы.
- [ ] Показать кнопку logout для авторизованного пользователя.

Проверка:

- [ ] Registration page открывается.
- [ ] Login page открывается.
- [ ] Ошибки формы видны.
- [ ] Навигация меняется для logged in / anonymous user.

### 4. Library Templates

- [ ] Создать home/book list template.
- [ ] Создать book detail template.
- [ ] Создать book form template.
- [ ] Создать confirm delete template.
- [ ] Показать title.
- [ ] Показать author_name.
- [ ] Показать genre.
- [ ] Показать description.
- [ ] Показать total_pages.
- [ ] Добавить ссылку `View details`.
- [ ] Добавить кнопку `Add to my library`.
- [ ] Добавить search input.
- [ ] Добавить genre filter.

Проверка:

- [ ] Book list показывает книги через `{% for %}`.
- [ ] Empty state работает через `{% if %}`.
- [ ] Detail page показывает одну книгу.
- [ ] Search/filter форма отображается.

### 5. Tracker Templates

- [ ] Создать `tracker/my_library.html`.
- [ ] Создать `tracker/progress_form.html`.
- [ ] Создать `tracker/review_form.html`.
- [ ] Показать книги пользователя.
- [ ] Показать reading status.
- [ ] Показать current page.
- [ ] Показать progress percentage.
- [ ] Добавить ссылку update progress.
- [ ] Добавить форму review/rating.

Проверка:

- [ ] My Library открывается только для logged in user.
- [ ] Прогресс отображается понятно.
- [ ] Review form отображается.

## Требования, которые закрывает Student 1

- [ ] Django Templates.
- [ ] Basic CSS.
- [ ] At least 4 event handlers: submit, links, filters, buttons.
- [ ] `{% for %}` loops.
- [ ] `{% if %}` conditions.
- [ ] Navigation between pages.
- [ ] Error/success messages on templates.

## Что объяснять на защите

- [ ] Как работает `base.html`.
- [ ] Как работают `{% for %}` и `{% if %}`.
- [ ] Как формы выводятся в templates.
- [ ] Как работает navigation.
- [ ] Где подключается CSS.

---

# Student 2 - Models, Forms, Django Views, Admin

## Главная цель

Сделать backend для обычного сайта:

- models;
- ModelForms;
- Django views;
- urls;
- admin;
- CRUD для книг;
- связь объектов с `request.user`.

## Основные файлы

```text
apps/users/models.py
apps/users/forms.py
apps/users/views.py
apps/users/urls.py
apps/users/admin.py

apps/library/models.py
apps/library/forms.py
apps/library/views.py
apps/library/urls.py
apps/library/admin.py

apps/tracker/models.py
apps/tracker/forms.py
apps/tracker/views.py
apps/tracker/urls.py
apps/tracker/admin.py

settings/base.py
settings/urls.py
```

## Задачи

### 1. Users App

- [ ] Упростить `CustomUser`, если команда решила использовать `AbstractUser`.
- [ ] Оставить поля `role`, `avatar`, `bio`.
- [ ] Сделать `UserSettings`.
- [ ] Добавить `label = 'users'` в `UsersConfig`.
- [ ] Подключить `apps.users.apps.UsersConfig` в `INSTALLED_APPS`.
- [ ] Проверить `AUTH_USER_MODEL = 'users.CustomUser'`.
- [ ] Зарегистрировать `CustomUser` в admin.
- [ ] Зарегистрировать `UserSettings` в admin.
- [ ] Создать registration form.
- [ ] Создать user settings form.
- [ ] Создать register view.
- [ ] Создать profile/settings view.
- [ ] Подключить users urls.

Проверка:

- [ ] `python manage.py makemigrations` работает.
- [ ] `python manage.py migrate` работает.
- [ ] `python manage.py createsuperuser` работает.
- [ ] Admin открывает пользователей.
- [ ] Registration работает.
- [ ] Login/logout работает.

### 2. Library App

- [ ] Создать `apps/library`.
- [ ] Добавить app в `INSTALLED_APPS`.
- [ ] Создать `Genre` model.
- [ ] Создать `Book` model.
- [ ] В `Book` добавить `title`.
- [ ] В `Book` добавить `author_name` как `CharField`.
- [ ] В `Book` добавить `genre` как `ForeignKey`.
- [ ] В `Book` добавить `description`.
- [ ] В `Book` добавить `total_pages`.
- [ ] В `Book` добавить `cover`, если нужна обложка.
- [ ] В `Book` добавить `created_by` как `ForeignKey` to user.
- [ ] В `Book` добавить `created_at`.
- [ ] В `Book` добавить `updated_at`.
- [ ] Зарегистрировать `Genre` в admin.
- [ ] Зарегистрировать `Book` в admin.
- [ ] Создать `BookForm`.
- [ ] Создать `GenreForm`.

Проверка:

- [ ] В admin можно создать genre.
- [ ] В admin можно создать book.
- [ ] Book связан с genre.
- [ ] Book связан с user через `created_by`.

### 3. Library Web Views

- [ ] Создать book list view.
- [ ] Добавить search по title.
- [ ] Добавить filter по genre.
- [ ] Создать book detail view.
- [ ] Создать book create view.
- [ ] Создать book update view.
- [ ] Создать book delete view.
- [ ] При создании book сохранять `created_by = request.user`.
- [ ] Добавить success/error messages.
- [ ] Создать urls для library.
- [ ] Подключить library urls в `settings/urls.py`.

Проверка:

- [ ] `/` или `/books/` показывает список книг.
- [ ] `/books/<id>/` показывает книгу.
- [ ] Create book работает.
- [ ] Update book работает.
- [ ] Delete book работает.
- [ ] Search/filter работают.

### 4. Tracker App

- [ ] Создать `apps/tracker`.
- [ ] Добавить app в `INSTALLED_APPS`.
- [ ] Создать `ReadingProgress` model.
- [ ] `ReadingProgress.user` -> ForeignKey to user.
- [ ] `ReadingProgress.book` -> ForeignKey to Book.
- [ ] Добавить status choices: `want_to_read`, `reading`, `completed`, `dropped`.
- [ ] Добавить `current_page`.
- [ ] Добавить `created_at`.
- [ ] Добавить `updated_at`.
- [ ] Добавить property `progress_percent`.
- [ ] Запретить дубль progress для одной пары user + book.
- [ ] Создать `Review` model.
- [ ] `Review.user` -> ForeignKey to user.
- [ ] `Review.book` -> ForeignKey to Book.
- [ ] Добавить `rating`.
- [ ] Добавить `text`.
- [ ] Добавить `created_at`.
- [ ] Зарегистрировать `ReadingProgress` в admin.
- [ ] Зарегистрировать `Review` в admin.
- [ ] Создать `ReadingProgressForm`.
- [ ] Создать `ReviewForm`.

Проверка:

- [ ] В admin виден progress.
- [ ] В admin видны reviews.
- [ ] Progress связан с user и book.
- [ ] Review связан с user и book.
- [ ] `progress_percent` считается.

### 5. Tracker Web Views

- [ ] Создать my library view.
- [ ] Создать add to library view.
- [ ] Создать update progress view.
- [ ] Создать create review view.
- [ ] Все tracker views закрыть через login required.
- [ ] В progress/review всегда использовать `request.user`.
- [ ] Не давать пользователю редактировать чужой progress.
- [ ] Добавить messages.
- [ ] Создать tracker urls.
- [ ] Подключить tracker urls в `settings/urls.py`.

Проверка:

- [ ] Logged in user может добавить book в my library.
- [ ] Logged in user может обновить progress.
- [ ] Logged in user может создать review.
- [ ] Anonymous user не может открыть protected pages.

## Требования, которые закрывает Student 2

- [ ] At least 4 models.
- [ ] At least 2 ForeignKey relationships.
- [ ] At least 4 forms.
- [ ] CRUD for at least one model.
- [ ] Objects linked to `request.user`.
- [ ] Admin customization.
- [ ] At least 3 named URL paths.
- [ ] Django authentication pages.

## Что объяснять на защите

- [ ] Какие модели есть и зачем.
- [ ] Где используются ForeignKey.
- [ ] Как работает `ModelForm`.
- [ ] Как работает CRUD для Book.
- [ ] Как используется `request.user`.
- [ ] Как настроен admin.

---

# Student 3 - DRF API, Serializers, Token Auth, Postman

## Главная цель

Сделать API часть проекта:

- DRF setup;
- serializers;
- API views;
- token login/logout;
- protected endpoints;
- Postman collection.

## Основные файлы

```text
apps/users/serializers.py
apps/users/api_views.py
apps/users/api_urls.py

apps/library/serializers.py
apps/library/api_views.py
apps/library/api_urls.py

apps/tracker/serializers.py
apps/tracker/api_views.py
apps/tracker/api_urls.py

settings/base.py
settings/urls.py
postman/
```

## Задачи

### 1. DRF Setup

- [ ] Установить `djangorestframework`.
- [ ] Установить `django-cors-headers`.
- [ ] Добавить `rest_framework` в `INSTALLED_APPS`.
- [ ] Добавить `rest_framework.authtoken` в `INSTALLED_APPS`.
- [ ] Добавить `corsheaders` в `INSTALLED_APPS`.
- [ ] Добавить CORS middleware.
- [ ] Настроить `REST_FRAMEWORK`.
- [ ] Выполнить migrations после добавления authtoken.

Проверка:

- [ ] Проект запускается.
- [ ] `python manage.py migrate` проходит.
- [ ] DRF browsable API открывается.

### 2. Users API

- [ ] Создать `apps/users/serializers.py`.
- [ ] Создать `UserReadSerializer` как `ModelSerializer`.
- [ ] Создать `UserRegisterSerializer` как `ModelSerializer`.
- [ ] Создать `LoginSerializer` как обычный `Serializer`.
- [ ] Создать `LogoutSerializer` как обычный `Serializer`, если нужен.
- [ ] Создать API register endpoint.
- [ ] Создать API login endpoint.
- [ ] Создать API logout endpoint.
- [ ] Создать API personal-info endpoint.
- [ ] Создать API update-profile endpoint.
- [ ] Подключить users api urls.

Проверка:

- [ ] API register создает пользователя.
- [ ] API login возвращает token.
- [ ] API logout удаляет token.
- [ ] Personal-info работает только с token.
- [ ] Update-profile работает только с token.

### 3. Library API

- [ ] Создать `apps/library/serializers.py`.
- [ ] Создать `GenreSerializer` как `ModelSerializer`.
- [ ] Создать `BookSerializer` как `ModelSerializer`.
- [ ] Создать хотя бы один обычный `Serializer` для custom validation/search.
- [ ] Создать book list API.
- [ ] Создать book detail API.
- [ ] Создать book create API.
- [ ] Создать book update API.
- [ ] Создать book delete API.
- [ ] Создать genre list API.
- [ ] Создать genre create API.
- [ ] При создании book использовать `request.user`.

Проверка:

- [ ] `GET /api/books/` работает без token или по выбранным permissions.
- [ ] `GET /api/books/<id>/` работает.
- [ ] `POST /api/books/create/` требует token.
- [ ] `PATCH /api/books/<id>/update/` требует token.
- [ ] `DELETE /api/books/<id>/delete/` требует token.

### 4. Tracker API

- [ ] Создать `apps/tracker/serializers.py`.
- [ ] Создать `ReadingProgressSerializer` как `ModelSerializer`.
- [ ] Создать `ReviewSerializer` как `ModelSerializer`.
- [ ] Создать `ReviewCreateSerializer` как обычный `Serializer`.
- [ ] Создать progress list API.
- [ ] Создать add progress API.
- [ ] Создать update progress API.
- [ ] Создать reviews list API.
- [ ] Создать create review API.
- [ ] Все create/update endpoints связать с `request.user`.
- [ ] Запретить редактировать чужой progress.

Проверка:

- [ ] `GET /api/progress/` показывает progress текущего user.
- [ ] `POST /api/progress/create/` требует token.
- [ ] `PATCH /api/progress/<id>/update/` требует token.
- [ ] `POST /api/reviews/create/` требует token.
- [ ] Review создается от текущего user.

### 5. DRF View Requirements

- [ ] Сделать минимум 2 Function-Based Views через `@api_view`.
- [ ] Сделать минимум 2 Class-Based Views через `APIView`.
- [ ] Использовать `permission_classes`.
- [ ] Возвращать правильные status codes.
- [ ] Обрабатывать validation errors.

Простой вариант распределения:

```text
Function-Based Views:
- api_book_list
- api_review_create

APIView:
- BookDetailAPIView
- BookUpdateDeleteAPIView
```

### 6. Postman

- [ ] Создать папку `postman/`.
- [ ] Создать collection.
- [ ] Добавить request: API register.
- [ ] Добавить request: API login.
- [ ] Добавить request: API logout.
- [ ] Добавить request: book list.
- [ ] Добавить request: book detail.
- [ ] Добавить request: create book with token.
- [ ] Добавить request: update book with token.
- [ ] Добавить request: delete book with token.
- [ ] Добавить request: progress list.
- [ ] Добавить request: add progress.
- [ ] Добавить request: update progress.
- [ ] Добавить request: review list.
- [ ] Добавить request: create review.
- [ ] Сохранить example responses.
- [ ] Commit Postman collection в repository.

## Требования, которые закрывает Student 3

- [ ] DRF configured.
- [ ] CORS configured.
- [ ] Token login/logout.
- [ ] 2+ `serializers.Serializer`.
- [ ] 2+ `serializers.ModelSerializer`.
- [ ] 2+ Function-Based DRF Views.
- [ ] 2+ APIView classes.
- [ ] API CRUD for Book.
- [ ] Protected endpoints.
- [ ] Objects linked to `request.user`.
- [ ] Postman collection.

## Что объяснять на защите

- [ ] Что такое serializer.
- [ ] Разница `Serializer` и `ModelSerializer`.
- [ ] Разница FBV и APIView.
- [ ] Как работает token authentication.
- [ ] Где используется `request.user`.
- [ ] Как тестировать API через Postman.

---

# Integration Checklist

Эта часть делается вместе после того, как каждый закончил свою зону.

- [ ] Все ветки смерджены.
- [ ] Конфликты решены.
- [ ] `requirements.txt` актуальный.
- [ ] `.env` настроен.
- [ ] `python manage.py makemigrations` работает.
- [ ] `python manage.py migrate` работает.
- [ ] `python manage.py createsuperuser` работает.
- [ ] Сервер запускается.
- [ ] Admin открывается.
- [ ] Registration работает.
- [ ] Login работает.
- [ ] Logout работает.
- [ ] Book list работает.
- [ ] Book detail работает.
- [ ] Book CRUD работает.
- [ ] My Library работает.
- [ ] Update progress работает.
- [ ] Review create работает.
- [ ] API login возвращает token.
- [ ] API protected endpoints требуют token.
- [ ] Postman collection работает.
- [ ] README.md актуальный.
- [ ] Presentation готова.

---

# Final Requirement Checklist

## Frontend

- [ ] Django Templates render dynamic content.
- [ ] At least 4 forms.
- [ ] At least 4 event handlers.
- [ ] Basic CSS.
- [ ] At least 3 named paths.
- [ ] Navigation between pages.
- [ ] `{% for %}` loops.
- [ ] `{% if %}` conditions.
- [ ] Registration.
- [ ] Login.
- [ ] Logout.
- [ ] Custom context processor or template tag.
- [ ] Graceful error handling/messages.

## Backend

- [ ] At least 4 models.
- [ ] At least 2 ForeignKey relationships.
- [ ] Optional custom manager if needed.
- [ ] Full CRUD for at least one model.
- [ ] Created objects linked to authenticated user.

## API

- [ ] 2+ serializers using `serializers.Serializer`.
- [ ] 2+ serializers using `serializers.ModelSerializer`.
- [ ] 2+ Function-Based Views using DRF decorators.
- [ ] 2+ Class-Based Views using `APIView`.
- [ ] Token-based login endpoint.
- [ ] Token-based logout endpoint.
- [ ] CORS configured.
- [ ] Postman collection committed.

## Defense

- [ ] README.md exists.
- [ ] GitHub repository exists.
- [ ] Commit history exists.
- [ ] Postman collection exists.
- [ ] Presentation is maximum 4 pages.
- [ ] Live demo is ready.
- [ ] All members can explain frontend and backend parts.
