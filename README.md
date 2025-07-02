# FastAPI Project Setup

This project uses FastAPI with a clean, class-based structure.

## Setup Instructions

1. **Create a virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```
2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

## Run Instructions

- **Start the development server:**
  ```powershell
  uvicorn app.main:app --reload
  ```
- **Swagger API Documentation:**
  Open your browser and go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Project Structure

```
menu-ai/
│   README.md
│   requirements.txt
│
├───venv/
└───app/
    ├── __init__.py
    ├── main.py
    ├── api/
    │   ├── __init__.py
    │   └── v1/
    │       ├── __init__.py
    │       └── endpoints/
    │           ├── __init__.py
    │           └── hello.py
    └── core/
        ├── __init__.py
        └── config.py
```

## Notes
- This structure is scalable and suitable for production projects.
- No database packages are included yet. 