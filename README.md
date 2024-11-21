API Project: Book Review Platform
Welcome to the Book Review Platform API project! This project is a Django-based REST API that allows users to view, filter, search, sort, and paginate books and reviews. It also includes user registration, authentication, and basic recommendation functionality based on genres, authors, and user ratings.

Table of Contents
Project Overview
Features
Technologies Used
Getting Started
Database Configuration
Environment Variables
Running the API Locally
API Endpoints
1. Project Overview
The Book Review Platform API allows users to:

Search and filter books based on title, author, ISBN, genre.
Sort books by title, author, average rating, and date added.
Paginate lists of books and reviews.
Add reviews for books.
Basic recommendation system based on genres and authors.
User registration and authentication using JWT tokens.
2. Features
Search and Filtering: Search books by title, author, ISBN, or genre.
Sorting and Pagination: Sort books by title, author, average rating, or date. Supports pagination.
Add Reviews: Users can add reviews for books, including a rating and review content.
Recommendations: Recommendations are based on user ratings and genres.
User Authentication: Secure API access using JWT tokens.
Admin Features: CRUD operations on books and reviews.
3. Technologies Used
Django - Web framework (version 5.1.3)
Django REST Framework - Toolkit for building APIs (version 3.14.0)
Django JWT Authentication - JSON Web Token Authentication (version 5.0.0)
Django Filters - Filtering and querying in Django (version 23.1)
Django ORM - Object-Relational Mapping for database operations
Python - Programming Language (version 3.12.0)
PostgreSQL/MySQL - Database Management System (replace with your preferred database)
pip - Python package installer
4. Getting Started
Prerequisites
Before running the project locally, make sure you have the following installed:

Python (version 3.12.0)
Pip - Python package installer
Virtual Environment - You can create a virtual environment using venv or conda
Setting Up the Environment
Clone the repository:

bash:-
git clone https://github.com/Naveenjith/bookproject.git
cd book-review-platform
Create a virtual environment:

bash:-
python -m venv env  # For `venv`
# or
conda create --name bookenv python=3.12.0
Activate the virtual environment:

On Windows:
bash:-
.\env\Scripts\activate  # For `venv`
On macOS/Linux:
bash:-
source env/bin/activate  # For `venv` or `conda`
Install the required packages
Run the following command to install the project dependencies:

bash:-
pip install -r requirements.txt
Database Configuration
Create a .env file in the project root directory.

Add your database configuration:

For PostgreSQL:

plaintext:-
DB_ENGINE=django.db.backends.postgresql
DB_NAME=bookdata
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
For MySQL:

plaintext:-
DB_ENGINE=django.db.backends.mysql
DB_NAME=bookdata
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
Run Migrations
Apply migrations to set up the database:

bash:-
python manage.py migrate
Create a Superuser
Run the following command to create a superuser (admin user):

bash:-
python manage.py createsuperuser
Running the API Locally
Start the development server:

bash:-
python manage.py runserver
You can now access the API at http://127.0.0.1:8000/.

API Endpoints
Books:
GET /books/ - List all books.
GET /books/{id}/ - Retrieve a single book.
POST /books/ - Create a new book (Admin Only).
PUT /books/{id}/ - Update a book (Admin Only).
DELETE /books/{id}/ - Delete a book (Admin Only).
GET /books/?search={query} - Search for books.
GET /books/?genre={genre} - Filter books by genre.
GET /books/?sort={field} - Sort books by a specific field (e.g. title, author, average_rating).
GET /books/?page={page_number} - Paginate the book list.
Reviews:
GET /reviews/ - List all reviews.
GET /reviews/{id}/ - Retrieve a single review.
POST /reviews/ - Create a new review (User Only).
PUT /reviews/{id}/ - Update a review (User Only).
DELETE /reviews/{id}/ - Delete a review (User Only).
User Registration & Authentication:-
POST/register/-User Register
POSt/token/-jwt token Authentication
