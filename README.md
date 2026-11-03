# Little Lemon: Django REST API

A back-end REST API for the fictional **Little Lemon** restaurant, built with **Django** and **Django REST Framework** as the capstone project of a professional back-end development certificate.

It lets authenticated users manage the restaurant's **menu** and **table bookings**, with token-based authentication provided by **Djoser**.

## Features

- Full CRUD for **menu items** and **table bookings**
- Token authentication (register, log in, log out) via Djoser
- Browsable API (DRF) plus JSON responses
- Django admin panel for managing data
- Unit tests for the models and the menu endpoint
- Runs out of the box on SQLite; MySQL supported through environment variables

## Tech Stack

Python 3.12+ · Django 6.1 · Django REST Framework · Djoser · SQLite (default) / MySQL

## Project Structure

```
django-backend-capstone-project/
├── workspace/
│   └── littlelemon/
│       ├── manage.py
│       ├── .env.example             # Template for your local .env
│       ├── littlelemon/             # Project config
│       │   ├── settings.py          # Reads secrets from environment variables
│       │   └── urls.py              # Root routes (admin, restaurant, auth)
│       ├── restaurant/              # Main app
│       │   ├── models.py            # Menu, Booking
│       │   ├── serializers.py
│       │   ├── views.py             # Menu views + BookingViewSet
│       │   ├── urls.py
│       │   ├── admin.py
│       │   ├── migrations/
│       │   └── static/restaurant/   # Logo
│       ├── templates/index.html     # Home page
│       └── tests/                   # test_models.py, test_views.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12 or newer
- Git

### 1. Clone the repository

```bash
git clone https://github.com/saharty7/django-backend-capstone-project.git
cd django-backend-capstone-project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cd workspace/littlelemon
cp .env.example .env        # Windows: copy .env.example .env
```

Open `.env` and set a `SECRET_KEY`. The defaults use SQLite, so no database setup is needed.

<details>
<summary>Using MySQL instead (optional)</summary>

1. `pip install mysqlclient`
2. In `.env` set `DB_ENGINE=mysql` and fill in `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.
3. Create the database first: `CREATE DATABASE LittleLemon;`

</details>

### 5. Set up the database and run

```bash
python manage.py migrate
python manage.py createsuperuser    # optional, for /admin/
python manage.py runserver
```

Open **http://127.0.0.1:8000/restaurant/** for the home page.

### 6. Run the tests

```bash
python manage.py test
```

## API Endpoints

All `restaurant/` endpoints require an auth token: `Authorization: Token <your-token>`.

| Method              | Endpoint                          | Description                  | Auth |
| ------------------- | --------------------------------- | ---------------------------- | ---- |
| POST                | `/auth/users/`                    | Register a new user          | No   |
| POST                | `/auth/token/login/`              | Get an auth token            | No   |
| POST                | `/auth/token/logout/`             | Invalidate the token         | Yes  |
| GET, POST           | `/restaurant/menu/`               | List / create menu items     | Yes  |
| GET, PUT, PATCH, DELETE | `/restaurant/menu/{id}`       | Retrieve / update / delete   | Yes  |
| GET, POST           | `/restaurant/booking/tables/`     | List / create bookings       | Yes  |
| GET, PUT, PATCH, DELETE | `/restaurant/booking/tables/{id}/` | Retrieve / update / delete | Yes  |

### Quick example

```bash
# 1. Register
curl -X POST http://127.0.0.1:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username": "demo", "password": "StrongPass#2026"}'

# 2. Log in and copy the "auth_token" value
curl -X POST http://127.0.0.1:8000/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "demo", "password": "StrongPass#2026"}'

# 3. Create a menu item
curl -X POST http://127.0.0.1:8000/restaurant/menu/ \
  -H "Authorization: Token <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"Title": "Greek Salad", "Price": "12.50", "Inventory": 20}'
```

## Data Models

- **Menu**: `Title`, `Price`, `Inventory`
- **Booking**: `Name`, `No_of_guests`, `BookingDate`

## License

Released under the [MIT License](LICENSE).

## Author

**Ahmed Amr Ibrahim Elsaharty**: Computer & AI Engineering student, Ain Shams University
[GitHub](https://github.com/saharty7) · [LinkedIn](https://www.linkedin.com/in/ahmed-amr-elsaharty-942248354/)
