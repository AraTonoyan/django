# Django Project

Welcome to the Django Marketplace Project! This project is an online marketplace where users can buy various items. It is built using Django and incorporates many of Django's powerful features and tools.

## Table of Contents

- [Project Status](#project-status)
- [Features](#features)
- [Installation](#installation)
  - [Create and Activate a Virtual Environment](#create-and-activate-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Apply Database Migrations](#apply-database-migrations)
  - [Create a Superuser](#create-a-superuser)
  - [Run the Development Server](#run-the-development-server)
- [Usage](#usage)
- [Admin Panel](#admin-panel)
- [Technologies Used](#technologies-used)
- [Database](#database)
- [Development](#development)
- [Contributing](#contributing)

## Project Status

**Note:** This project is currently incomplete. It is a work in progress created as part of my learning journey with Django. While many core features are implemented, additional functionality and improvements are still being developed.

## Features

- Admin authentication and authorization
- Product listing and detail pages
- Shopping cart functionality
- Order processing (in development)
- Admin panel for managing products, orders, and users
- Use of Django migrations and tools for database management

## Installation

Follow these steps to set up the project on your local machine:

### Create and Activate a Virtual Environment

1. **Create a virtual environment named `venv`:**
   ```
   python -m venv venv

2. **Activate the virtual environment:**
- On macOS/Linux:
  ```
  source env/bin/activate
  ```
- On Windows:
  ```
  .\env\Scripts\activate
  ```

### Install Dependencies

3. **Install the required dependency:**
   ```
   pip install pillow

### Apply Database Migrations

4. **Apply Django database migrations:**
    ```
   python manage.py migrate

### Create a Superuser

5. **Create a Django superuser:**
    ```
   python manage.py createsuperuser

### Run the Development Server

6. **Start the Django development server:**
    ```
   python manage.py runserver

## Usage

Once the server is running, you can access the application in your web browser at `http://127.0.0.1:8000/`.

## Admin Panel

The admin panel is accessible at `http://127.0.0.1:8000/admin/`. Use the superuser credentials you created earlier to log in. The admin panel allows you to manage products, orders, users, and other aspects of the application.

## Technologies Used

- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **SQLite 3:** A lightweight database used for development and testing.

## Database

This project uses SQLite 3 for the database, which is a simple and easy-to-use database engine suitable for development and small-scale applications.

## Development

This project is being developed as a part of my education in Django. Throughout the development process, I have utilized many of Django's tools and features, including:

- **Django Migrations:** For database schema changes.
- **Django Admin:** For managing application data.
- **Django ORM:** For database interactions.
- **Django Views and Templates:** For rendering HTML pages and handling requests.

## Contributing

Contributions are welcome! If you have suggestions or find issues, please create a pull request or open an issue on GitHub.
