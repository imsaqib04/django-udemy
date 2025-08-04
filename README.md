\# 🎬 Watchmate

**Watchmate** is a web application built using the Django REST Framework (DRF). It allows users to manage and track their personal watchlists of movies and series. The app provides a robust, RESTful API for managing watchlists, streaming platforms, and user reviews — making it easily integrable with any frontend.

---

## 🚀 Features

- 🔐 **User Authentication**: Token-based user registration, login, and logout.
- 📺 **Watchlist Management**: Create, retrieve, update, and delete movies or series.
- 🌐 **Streaming Platforms**: Full CRUD operations for platforms like Netflix, Prime, etc.
- 📝 **Review System**: Add, view, update, and delete reviews for items.
- 🔒 **Permissions**: Only the creator can modify or delete their reviews.
- 🛡️ **API Throttling**: Limits API calls to prevent abuse.
- 🔍 **Filtering & Searching**: Filter watchlists by title/platform, and perform search queries.
- 📄 **Pagination**: Improves performance for large watchlists.

---

## 🛠️ Installation

> Make sure Python and pip are installed on your system.

### 1. Clone the Repository

git clone <your-repository-url>
cd watchmate

2. Create and Activate a Virtual Environment
For macOS/Linux:

python3 -m venv venv
source venv/bin/activate

For Windows:
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install Django djangorestframework djangorestframework-authtoken django-filters

4. Run Migrations
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser
python manage.py createsuperuser

▶️ Usage
Start the development server:

python manage.py runserver

Visit the API: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

You can test APIs using tools like Postman, Insomnia, or through your own frontend.

📚 API Endpoints
🔐 User Authentication
Endpoint	Method	Description

/account/register/	POST	Register a new user

/account/login/	POST	Obtain an auth token

/account/logout/	POST	Invalidate the current token


🌐 Streaming Platforms

Endpoint	Method	Description

/watch/stream/	GET, POST	List all or create a new platform

/watch/stream/<int:pk>/	GET, PUT, DELETE	Retrieve, update, or delete


📺 Watchlist

Endpoint	Method	Description

/watch/list/	GET, POST	List all items or add a new one

/watch/<int:pk>/	GET, PUT, DELETE	Retrieve, update, or delete an item

/watch/list2/	GET	Paginated list with search


📝 Reviews

Endpoint	Method	Description

/watch/<int:pk>/reviews/	GET	Get all reviews for a specific watchlist item

/watch/<int:pk>/review-create/	POST	Create a new review

/watch/review/<int:pk>/	GET, PUT, DELETE	Retrieve, update, or delete a review

/watch/reviews/?username=<username>	GET	Get all reviews by a specific user


🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you would like to modify or add.

📄 License

This project is licensed under the MIT License. Feel free to use it as you like.
