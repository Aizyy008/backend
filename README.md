# Backend (Django) README

## Backend Setup - Django

This section of the project is the backend, built using Django and Django REST Framework (DRF). It handles all the server-side logic, database interactions, and provides RESTful APIs to the mobile app.

## Table of Contents

- [Django Setup](#django-setup)
  - [Install Python](#install-python)
  - [Clone the Project](#clone-the-project)
  - [Set Up the Virtual Environment](#set-up-the-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Set Up the Database](#set-up-the-database)
  - [Run Migrations](#run-migrations)
  - [Create a Superuser](#create-a-superuser)
  - [Start the Django Server](#start-the-django-server)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Django Setup

### Install Python
Make sure you have Python 3.8 or higher installed. You can download Python from the [official Python website](https://www.python.org/downloads/).

### Clone the Project
Clone the repository using your preferred Git client.

### Set Up the Virtual Environment
Navigate to the backend folder and create a virtual environment:
```bash
python -m venv venv
```

### Activate the Virtual Environment
For Windows, use:
```bash
venv\Scripts\activate
```

For Mac/Linux, use:
```bash
source venv/bin/activate
```

### Install Dependencies
Install the required Python packages by running:
```bash
pip install -r requirements.txt
```

### Set Up the Database
Django uses SQLite by default, but you can configure it to use PostgreSQL, MySQL, or other databases. Modify the `DATABASES` section in the `settings.py` file.

### Run Migrations
Run the migrations to set up the database:
```bash
python manage.py migrate
```

### Create a Superuser
To access the Django admin panel, create a superuser:
```bash
python manage.py createsuperuser
```

### Start the Django Server
Start the Django development server:
```bash
python manage.py runserver
```

By default, the server will run at `http://127.0.0.1:8000`.

## Project Structure

- `manage.py`: Django's command-line utility for managing the app.
- `myapp/`: Contains models, views, and serializers for your application.
- `migrations/`: Database migration files.
- `models.py`: Contains the database models.
- `views.py`: Contains the views that handle HTTP requests.
- `serializers.py`: Converts models to JSON and vice versa.
- `requirements.txt`: List of Python dependencies (e.g., Django, djangorestframework).
- `settings.py`: Contains Django settings, including database and installed apps.
- `urls.py`: URL routing configuration for your app.

## Environment Variables

Some environment variables are required for running the backend:

- **JWT Token for Authentication**: Ensure proper setup for JWT authentication in Django. This includes handling token generation and authentication.
- **Django Settings**: In `settings.py`, set the DEBUG flag for development or production environments:
  ```python
  DEBUG = True  # for development (set to False in production)
  ```

## Running the Application

### Running Django
After setting up your environment, navigate to the Django project directory and activate the virtual environment. Then, run the following to start the Django development server:

```bash
python manage.py runserver
```

Your backend will be accessible at `http://127.0.0.1:8000`.

## Contributing

We welcome contributions to this project! Please follow these steps if you would like to contribute:

1. Fork the repository.
2. Create a new branch (e.g., `git checkout -b feature-xyz`).
3. Make your changes.
4. Commit your changes (e.g., `git commit -am 'Add new feature'`).
5. Push your changes (e.g., `git push origin feature-xyz`).
6. Create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.
