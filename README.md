----------

# 🎮 Django Game

A web application built with **Django** for hosting and playing simple games. The goal of this project is to practice Django fundamentals (models, views, templates, forms) while creating fun and interactive games that run in the browser.

----------

## 🚀 Features

-   User-friendly web interface to browse and play games.
    
-   Each game is implemented as a Django app for modularity.
    
-   Extendable: easily add new games by creating new apps.
    
-   Clean and simple UI with Django templates.
    

----------

## 🛠️ Tech Stack

-   **Python 3.10+**
    
-   **Django 5.x**
    
-   HTML, CSS, JavaScript (for frontend interactivity)
    
-   SQLite (default) or PostgreSQL (optional)
    

----------

## ⚙️ Installation & Setup

1.  Clone the repository:
    
    ```bash
    git clone https://github.com/your-username/django-game.git
    cd django-game
    
    ```
    
2.  Create & activate a virtual environment:
    
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    
    ```
    
3.  Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
4.  Apply migrations:
    
    ```bash
    python manage.py migrate
    
    ```
    
5.  Run the development server:
    
    ```bash
    python manage.py runserver
    
    ```
    
6.  Open the app in your browser:
    
    ```
    http://127.0.0.1:8000
    
    ```
    

----------

## 🎲 Planned Games

-   Tic Tac Toe
    
-   Number Guessing Game
    
-   Rock Paper Scissors
    
-   More to come...
    

----------

## 🤝 Contributing

Want to add a new game? Create a new Django app inside the project and submit a pull request!

----------
