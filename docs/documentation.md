# 🎬 FastAPI Movies API – Technical Documentation

> A companion document to the main **`README.md`**. It drills down into the internal design, HTTP surface, and key lessons learned while building the project.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Goals](#project-goals)
3. [Tech Stack & Key Libraries](#tech-stack--key-libraries)
4. [Dependency Injection](#dependency-injection)
5. [Modular Routers](#modular-routers)
6. [Running Locally](#running-locally)
7. [HTTP Endpoints](#http-endpoints)\
   7.1 [Summary](#summary)\
   7.2 [Error Responses](#error-responses)
8. [Validation & Constraints](#validation--constraints)
9. [Error Handling Strategy](#error-handling-strategy)
10. [Learnings & Key Takeaways](#learnings--key-takeaways)
11. [About Uvicorn](#about-uvicorn)
12. [Conclusion](#conclusion)
13. [Autor](#autor)


---

## Project Overview

The Movies API is a **CRUD** service that stores a catalogue of films in an in‑memory list (for now). It was built to explore **FastAPI** fundamentals such as routing, model validation, automatic documentation, and modular project organisation.

---

## Project Goals

- Gain hands‑on experience with **FastAPI** and asynchronous Python.
- Practise clean architecture by separating **routers**, **models**, and **business logic**.
- Learn to document an API using **Markdown** + the auto‑generated **Swagger UI**.
- Apply good DevOps habits: virtual environments, `requirements.txt`, environment variables, and automated tests.

---

## Tech Stack & Key Libraries

| Purpose          | Library                | Why it matters                              |
| ---------------- | ---------------------- | ------------------------------------------- |
| Web framework    | **FastAPI**            | Type‑hinted, async‑ready, automatic docs    |
| Data validation  | **Pydantic v2**        | Declarative schemas & runtime validation    |
| ASGI server      | **Uvicorn**            | Production‑grade server with hot‑reload     |
| Typing           | **mypy** (optional)    | Static type checking                        |

---

## Dependency Injection

FastAPI’s `Depends` mechanism wires common resources (e.g. DB sessions, auth checks) into endpoints. Even though this app only uses an in‑memory list, the pattern is demonstrated so the code can later migrate to a real database seamlessly:

```python
from fastapi import Depends, HTTPException

def get_db():
    return fake_db  # swap with real session later

@router.get("/movies")
async def list_movies(db = Depends(get_db)):
    return db
```

## Modular Routers

Endpoints are grouped by feature into **APIRouters**. This keeps each file short and composable:

```python
# app/routers/movies.py
router = APIRouter(prefix="/movies", tags=["movies"])
```

Routers are included in `main.py`:

```python
app.include_router(movies.router)
```

---

## Running Locally
### 1. Clone & enter repo

```bash
git clone https://github.com/youruser/fastapi-movies.git
cd fastapi-movies
```

### 2. Create venv & install deps

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the server

```bash
uvicorn app.main:app --reload
```

Visit [**http://127.0.0.1:8000/docs**](http://127.0.0.1:8000/docs) for Swagger UI (Default).

---

## HTTP Endpoints

### Summary

```
GET     /movies           → List all movies
GET     /movies/{id}      → Retrieve one movie
POST    /movies           → Create a new movie
PUT     /movies/{id}      → Replace entire movie
DELETE  /movies/{id}      → Remove movie
```

### Error Responses

- `404 Not Found` – movie ID does not exist
- `422 Unprocessable Entity` – request body fails Pydantic validation
- `500 Internal Server Error` – unhandled exceptions (should never happen in happy path)

---

## Validation & Constraints

Pydantic schemas enforce data types and custom rules:

```python
class Movie(BaseModel):
    title: str = Field(min_length=1)
    year: int = Field(ge=1888, le=datetime.now().year)  # first film was 1888
    genre: str = Field(..., description="Main genre")
```

---

## Error Handling Strategy

All domain‑specific errors are translated into **HTTPException** instances with meaningful status codes and messages. A global exception handler could be added for logging and sanitising unhandled errors.

---

## Learnings & Key Takeaways

- **FastAPI** makes async API development approachable and efficient.
- **APIRouter** promotes clean modularisation.
- Type hints + **Pydantic** reduce runtime bugs by catching bad payloads early.
- Automatic docs (Swagger UI / ReDoc) save manual effort and impress stakeholders.
- Separating config with **BaseSettings** keeps code 12‑factor‑app friendly.
- Writing tests with **httpx.AsyncClient** let me verify behaviour without spinning a server.
- Keeping secrets out of the repo via **dotenv** is essential for security.
- Clear docs like this file turn a simple exercise into a portfolio‑ready project.

---

## About Uvicorn
To call the application, I will use the **uvicorn main:app** command:
   
    bash
    uvicorn <namefile>:<application>

If I want **to change the port**, I must add to the original command:
    
    bash
    uvicorn <namefile>:<application> --port <port>

If I want the code changes to take effect **when the page is reloaded**, add:
    
    bash
    uvicorn <namefile>:<application> --port <port> --reload

If I want **other devices to be able to access it locally**, then the command would be:
   
    bash
    uvicorn <namefile>:<application> --host 0.0.0.0 --port <port> --reload

**Regarding Modularizations:**

If the file I want to access is in a different path than where I call it:
    
    bash
    uvicorn <directory>.<namefile>:<application> --port <port> --reload

---

## Conclusion

*While this project is basic, I believe it has laid the foundation for me to understand how an API works at an introductory level. I would like to give it a deeper understanding of AI so I can continue my education.*

---

## Autor
Built by **@Cristian "CodriX" Colares - AI beginner 🇦🇷**

---

