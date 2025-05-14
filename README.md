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

## 🧠 Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Runtime**: Python 3.11+
- **Package Manager**: [uv](https://github.com/astral-sh/uv)

---

## 📦 Installation

1. **Clone the repository**

```bash
   git clone https://github.com/swayam5342/ieeeras_task_1_backend.git
   cd ieeeras_task_1_backend
```


2. **Create a virtual environment and install dependencies using uv**

```bash
uv sync
```

---

## 🏁 Running the App

```bash
uvicorn app:app --reload
```


---

## 🧪 API Endpoints

|Method|Endpoint|Description|
|---|---|---|
|GET|`/`|Welcome message|
|GET|`/items`|Get all books|
|POST|`/items`|Add a new book|
|PUT|`/items/{item_id}`|Update a book by ID|
|DELETE|`/items/{item_id}`|Delete a book by ID|

---

## 🧾 Sample Book Schema

```json
{
  "id": 1,
  "title": "Sample Book",
  "author": "Sample Author",
  "year": 2023,
  "genre": "Fiction"
}
```

---

## 📁 Project Structure

```
root
├── .gitignore
├── .python-version
├── README.md
├── app
│   ├── __init__.py
│   ├── routes
│   │   └── home.py
│   └── schemas
│       └── book.py
├── main.py
├── pyproject.toml
└── uv.lock
```

---


## 🧑‍💻 Author

- **Name**: [swayam](https://github.com/swayam5342)