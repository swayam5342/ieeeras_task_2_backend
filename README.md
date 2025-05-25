# 📚 FastAPI Book APIz

  

This is a simple Book Management API built with **FastAPI**. It supports basic CRUD operations (Create, Read, Update, Delete) for managing books stored in an in-memory dictionary.

  

---

  

## 🚀 Features

  

- Get a welcome message from the root endpoint

- Retrieve all books

- Add a new book

- Update an existing book

- Delete a book

  

---

  

## Requirement 

  

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)

- **Runtime**: Python 3.11+

- **Package Manager**: [uv](https://github.com/astral-sh/uv)

  

---

  

## 📦 Installation

  

1. **Clone the repository**

  

```bash

   git clone https://github.com/swayam5342/ieeeras_task_2_backend.git

   cd ieeeras_task_2_backend

```

  ---
  

2. **Create a virtual environment and install dependencies using uv**

  

```bash

uv sync

```

  

---

  3. **Create a `.env` file:

```
MONGODB_URI=
MONGO_DB_NAME=
```

## 🏁 Running the App

  

```bash

uvicorn app:app --reload

```

  
  

---

  
## 📖 API Endpoints

### Books

|Method|Endpoint|Description|
|---|---|---|
|GET|/items|List all books with filters|
|POST|/items|Add a new book|
|PUT|/items/{id}|Update a book by ID|
|DELETE|/items/{id}|Delete a book by ID|

### 🔍 Filtering & Pagination

`GET /items` supports:

- `skip`: items to skip (default: 0)
    
- `limit`: max items to return (default: 10)
    
- `author`, `genre`, `year`: optional filters
    

Example:

```bash
curl localhost:8000/items?author=John%20Doe&limit=5
```

```json
[
  {
    "id": 1,
    "title": "DSA in Java",
    "author": "John Doe",
    "year": 2019,
    "genre": "Programming"
  }
]
```

---

## 🧰 Project Structure

```bash
.
├── .EXAMPLE.ENV
├── .gitignore
├── .python-version
├── README.md
├── app
│   ├── __init__.py
│   ├── routes
│   │   └── home.py
│   ├── schemas
│   │   └── book.py
│   └── services
│       └── db.py
├── main.py
├── pyproject.toml
└── uv.lock
```
## 🧑‍💻 Author

  

- **Name**: [swayam](https://github.com/swayam5342)