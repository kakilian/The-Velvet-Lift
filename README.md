# The Velvet Lift 2025

**The Velvet Lift** is a Django web application for managing cosmetic lifting procedures. The project is modular and extensible, designed for both clinic staff and users to interact with ease.

---

## Project Overview

This project consists of several Django apps:

* **assets**: Static files (CSS, JS, images, icons)
* **appointments**: Manages appointment bookings and payment tracking
* **main\_features**: Core homepage and shared views
* **transformations**: Tracks before-and-after visual records of procedures
* **template\_app**: Global templates and layout (base, header, footer, home)
* **user\_profiles**: User profile and doctor management

---

## Models

### `user_profiles/models.py`

* `UserProfile`: Extends Django User model (adds phone, profile picture)
* `Doctor`: Associates User with specialization

### `appointments/models.py`

* `Appointment`: Connects Users and Doctors
* `Payment`: Captures related payment data

### `transformations/models.py`

* `Transformation`: Holds visual records of procedures (before/after)

---

## Setup Instructions

### Prerequisites

* Python 3.12.2
* Django 4.2.17
* See [requirements](#requirements)

### Installation

```bash
cd thevelvetlift
pip install -r requirements.txt
```

---

## Requirements

* Django
* Pillow
* Gunicorn
* Python-dotenv
* WhiteNoise

---

## Deployment

### Local Deployment

```bash
git clone https://github.com/kakilian/thevelvetlift.git
cd thevelvetlift
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Deployment to Render

* Connect GitHub repo
* Build command:

```bash
python manage.py migrate && python manage.py collectstatic --noinput
```

* Start command:

```bash
gunicorn the_velvet_lift.wsgi:application
```

* Add `.env` with keys:

```
SECRET_KEY=your_secret
DEBUG=False
```

* Add your domain to `ALLOWED_HOSTS` in `settings.py`

---

## Project Structure

```bash
The-Velvet-Lift/
├── manage.py
├── requirements.txt
├── the_velvet_lift/           # Django settings, wsgi, urls
├── assets/                    # Static files (css, js, images)
├── appointments/              # Appointments and Payments
├── main_features/             # Shared views
├── template_app/              # Reusable templates (base.html)
├── transformations/           # Procedure records
└── user_profiles/             # Extended user model
```

---

## Features

* Booking system for appointments
* User registration and profiles
* Admin dashboard
* Transformation gallery (before/after)
* Responsive styling with Bootstrap

---

## Bugs

### Solved

* Admin panel not loading: resolved missing `collectstatic`
* Static images not found: clarified pathing between `assets/` and `STATICFILES_DIRS`

### Unsolved

* Favicon not always appearing after deployment (possible static cache)

---

## Future Improvements

* Class-based views
* Admin dashboard improvements
* Rating system for treatments
* Newsletter signup (Mailchimp)
* Integration with payment provider (Stripe/PayPal)

---

## Credits

* Django Documentation
* Bootstrap (styling)
* FontAwesome + DevIcon (social icons)

---

## Notes

### Static Files:

```python
STATIC_URL = "/assets/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "assets")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```

### Templates:

Located in `template_app/templates/template_app/`

### .env File (local only):

```ini
SECRET_KEY=your-secret-key
DEBUG=True
```

---

## Introduction

A modern aesthetic clinic offering lifting procedures, non-invasive transformations, and high-touch consultation from certified doctors. Tailored for individuals seeking subtle enhancement.

---

## Problems and Testing

* Initial struggles with static file routing and inconsistent naming
* Pillow and Django versions needed compatibility management
* Migrating with apps in the wrong folder caused delays
* Debugging .env issues and untracked database errors slowed down early deployment

---

## Deployment Link

* Live Site: [https://the-velvet-lift.onrender.com](https://the-velvet-lift.onrender.com)
* GitHub Repo: [https://github.com/kakilian/thevelvetlift](https://github.com/kakilian/thevelvetlift)

---

## Author

**Katarina Kilian** — 2025
