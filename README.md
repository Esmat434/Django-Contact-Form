# Django Contact Form Website

A simple contact form web application built using Django. Users can submit their contact information and message, which is stored in the database or sent to an email address (optional).

## Features

- User-friendly contact form (Name, Email, Subject, Message)
- Backend validation
- Data stored in the database
- Admin panel to view submitted messages
- Optional: Send form content to an email address

## Technologies Used

- Python 3.10
- Django 5.2
- SQLite (default) or MySQL/PostgreSQL
- Bootstrap (for frontend styling)

## Project Structure
ContactForm/
- │
- ├── contact/             # App for contact form
- │   ├── migrations/
- │   ├── templates/
- │   │   └── contact.html
- │   ├── admin.py
- │   ├── models.py
- │   ├── views.py
- │   └── forms.py
- │   └── signals.py
- │   └── email_config.py
- │
- ├── core/
- │   ├── settings.py
- │   ├── urls.py
- │   └── wsgi.py
- │
- ├── db.sqlite3
- ├── manage.py
- └── requirements.txt


## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Esmat434/Django-Contact-Form.git
cd ContactForm

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
