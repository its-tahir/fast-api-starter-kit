# FastAPI Starter Kit

## Overview
A scalable, service-based FastAPI starter kit with clear separation of concerns, minimal and meaningful logging, and best practices for maintainability and growth.

## Project Structure
```
app/
  api/
    v1/
      endpoints/
      __init__.py
    __init__.py
  core/
    config.py           # .env-based config using Pydantic
    response.py
    error_handlers.py   # Centralized error handling
    exceptions.py       # Custom exception classes
    middleware.py
    logger.py
    __init__.py
  services/
    hello_service.py
    __init__.py
  models/
    __init__.py
  utils/
    decorators.py
    __init__.py
  main.py
  container.py         # App factory/container
  __init__.py
.env                   # Environment config
```

## Key Features
- **Service Layer:** All business logic in `services/` for maintainability.
- **Centralized Error Handling:** Custom handlers in `core/error_handlers.py`.
- **Custom Exceptions:** Define and handle business and auth errors in `core/exceptions.py`.
- **.env-based Config:** All config is loaded from `.env` using Pydantic's `BaseSettings`.
- **CORS Security:** CORS middleware is enabled and configurable.
- **Global Rate Limiting:** All endpoints are protected by global rate limiting (via `slowapi`).
- **Middleware:** Logging and rate limiting middleware included.
- **Decorators & Utils:**
  - `@api_response` for generic response and error handling
  - Template for authentication decorators
- **Minimal Logging:** Only errors and critical events are logged by default.

## Getting Started
1. **Create and activate a virtual environment (venv):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment:**
   Edit the `.env` file to set project config (see example in repo).
4. **Run the app:**
   ```bash
   uvicorn app.main:app --reload
   ```
5. Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API docs.

## Extending
- Add new endpoints in `api/v1/endpoints/` and corresponding business logic in `services/`.
- Add new models in `models/`.
- Add new middleware, error handlers, or decorators as needed.
- Use or extend the provided decorators for generic concerns (response, authentication, etc.).
- Add new config values to `.env` and `core/config.py` as needed.

## Example Endpoints
- `GET /hello` — Returns a hello message using the service layer and generic response decorator.
- `GET /hello-error` — Demonstrates error handling and logging using the generic response decorator.

---
This starter kit is designed for rapid development and easy scaling. Enhance as your project grows!
- No database packages are included yet. 
