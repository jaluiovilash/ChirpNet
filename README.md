# ChirpNet

ChirpNet is a basic working model of Twitter, developed using Django for the backend and Bootstrap for the frontend. This project showcases the ability to create a functional social media platform, demonstrating skills in web development and backend integration.

## Features

- **User Registration**: Secure user registration and authentication.
- **Create Posts**: Users can create new posts with text and photos.
- **Edit Posts**: Users can edit their existing posts.
- **Delete Posts**: Users can delete their own posts.

## Project Overview

This is my first Django-based project where I have integrated user registration for security. ChirpNet allows users to create, edit, and delete posts, similar to how Twitter operates.

## Technologies Used

- **Django**: Backend framework for building the application.
- **Bootstrap**: Frontend framework for styling the application.
- **SQLite**: Database for storing user and post data.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ChirpNet.git
    cd ChirpNet
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

- **Registration**: Create an account using the registration form.
- **Login**: Login with your credentials.
- **Create Post**: Click on "Create chirp" to create a new post.
- **Edit Post**: Click on "Edit" next to a post to edit it.
- **Delete Post**: Click on "Delete" next to a post to delete it.

## Directory Structure

```bash
ChirpNet/
├── chirpnet/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── chirp/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
