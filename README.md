
# Mastermind Showcase (Django + PostgreSQL)

A Django app that lists mastermind members on the home page and shows an individual page per member with **images/videos** and **social links**. Uses **PostgreSQL** (via `DATABASE_URL`) and supports file uploads.

## Quick start

### 1) Create and fill `.env`
Copy `.env.example` to `.env` and adjust values if needed.
```env
DEBUG=1
SECRET_KEY=change-me-please
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/mgshowcase
```

### 2) Run Postgres with Docker
```bash
docker compose up -d
```

### 3) Install & migrate
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed
python manage.py runserver
```

Open http://127.0.0.1:8000 for the site and http://127.0.0.1:8000/admin/ for the admin.

## Adding media
In **Admin**, open a Member and add **Media**:
- Upload a local **file** OR paste a **URL**
- Choose **Image** or **Video**

## Note
In development, Django serves uploaded files at `/media/`. For production, configure a storage service (S3, R2, etc.).
