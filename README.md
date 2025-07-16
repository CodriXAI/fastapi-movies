# 🎬 FastAPI Movies API

A simple RESTful API built with FastAPI that allows you to manage a collection of movies.  
This project was created as a hands-on exercise to learn how to build and document APIs using FastAPI.

---

## 🚀 Features

- 🔍 Get a list of movies
- 🎥 Add a new movie
- ❌ Delete a movie by ID
- ✏️ Update movie information
- ⚡ FastAPI + Uvicorn for blazing fast performance

---

## 📦 Tech Stack

- **FastAPI** – web framework for building APIs
- **Pydantic** – data validation and settings management
- **Uvicorn** – ASGI server for serving the app
- **Python 3.10+**

---

## ▶️ How to Run

### 1. Clone the repo

    ```bash
    git clone https://github.com/CodriXAI/fastapi-movies.git
    cd fastapi-movies
    ```

### 2. Create virtual environment
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

### 3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

### 4. Run the app
    ```bash
    uvicorn main:app --reload
    ```

Then open your browser at http://127.0.0.1:8000/docs to see the auto-generated Swagger UI.

---

## 🧠 What I Learned
- How to build APIs with `FastAPI`

- How to define and validate models using `Pydantic`

- How to organize project files cleanly

- How to serve and test **endpoints**

- How to document APIs with `Swagger UI`

See the [extended documentation here](docs/documentation.md)

---

## 📄 License
This project is open source and available under the MIT License.

---
## Autor
Built by **@Cristian "CodriX" Colares - AI beginner 🇦🇷**

---
