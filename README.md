# Django Comments API Project

A Django project with REST APIs for managing comments using django-comments-xtd.

## Setup Instructions

1. **Activate Virtual Environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create Superuser (Optional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start Development Server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

## Simple Comments API

### 1. Create Comment (POST)
**URL:** `POST /api/comments/`

**Request Body:**
```json
{
    "application_id": "app123",
    "comments": "This is a sample comment"
}
```

**Response:**
```json
{
    "status": "success",
    "message": "Comment created successfully",
    "data": {
        "id": 1,
        "application_id": "app123",
        "comments": "This is a sample comment",
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-15T10:30:00Z"
    }
}
```

### 2. Get All Comments (GET)
**URL:** `GET /api/comments/`

### 3. Get Comment by ID (GET)
**URL:** `GET /api/comments/{id}/`

### 4. Get Comments by Application ID (GET)
**URL:** `GET /api/comments/application/{application_id}/`

## Django Comments XTD API (Extended Features)

### 5. Create Extended Comment (POST)
**URL:** `POST /api/xtd-comments/`

**Request Body:**
```json
{
    "application_id": "app123",
    "comments": "This is an extended comment with django-comments-xtd features",
    "user_name": "John Doe",
    "user_email": "john@example.com"
}
```

**Response:**
```json
{
    "status": "success",
    "message": "Extended comment created successfully",
    "data": {
        "id": 1,
        "application_id": "app123",
        "comments": "This is an extended comment with django-comments-xtd features",
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-15T10:30:00Z",
        "user_name": "John Doe",
        "user_email": "john@example.com",
        "is_public": true,
        "is_removed": false
    }
}
```

### 6. Get All Extended Comments (GET)
**URL:** `GET /api/xtd-comments/`

### 7. Get Extended Comment by ID (GET)
**URL:** `GET /api/xtd-comments/{id}/`

### 8. Get Extended Comments by Application ID (GET)
**URL:** `GET /api/xtd-comments/application/{application_id}/`

## Model Schema

### Comment Model
- `id`: Auto-generated primary key
- `application_id`: String field (max 255 chars) - Application identifier
- `comments`: Text field - Comment content
- `created_at`: DateTime field - Creation timestamp
- `updated_at`: DateTime field - Last update timestamp

## Testing the APIs

### Using curl:

#### Simple Comments:

1. **Create a simple comment:**
```bash
curl -X POST http://localhost:8000/api/comments/ \
  -H "Content-Type: application/json" \
  -d '{"application_id": "app123", "comments": "This is a test comment"}'
```

2. **Get all simple comments:**
```bash
curl -X GET http://localhost:8000/api/comments/
```

3. **Get simple comments by application ID:**
```bash
curl -X GET http://localhost:8000/api/comments/application/app123/
```

#### Extended Comments (Django Comments XTD):

4. **Create an extended comment:**
```bash
curl -X POST http://localhost:8000/api/xtd-comments/ \
  -H "Content-Type: application/json" \
  -d '{"application_id": "app123", "comments": "This is an extended comment", "user_name": "John Doe", "user_email": "john@example.com"}'
```

5. **Get all extended comments:**
```bash
curl -X GET http://localhost:8000/api/xtd-comments/
```

6. **Get extended comments by application ID:**
```bash
curl -X GET http://localhost:8000/api/xtd-comments/application/app123/
```

## Django Admin

Access the Django admin at `http://localhost:8000/admin/` to manage comments through the web interface.

## Dependencies

- Django 5.0.7
- Django REST Framework 3.15.2
- django-comments-xtd 2.10.8
- django-cors-headers 4.3.1

## Project Structure

```
POC/
├── comment_project/          # Main Django project
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── comments/                 # Comments Django app
│   ├── models.py            # Comment model
│   ├── views.py             # API views
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # App URL configuration
│   └── admin.py             # Admin configuration
├── requirements.txt         # Python dependencies
├── manage.py               # Django management script
└── README.md               # This file
```