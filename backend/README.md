# IP-SAKTI Sahayak - Backend

This directory contains the FastAPI backend for the IP-SAKTI Sahayak application. It serves the API endpoints that power the frontend, handling data retrieval for legal frameworks, patents, traditional knowledge (TK), fee calculations, and assessments.

If you are new to FastAPI, don't worry! It's designed to be fast, easy to use, and automatic with its documentation. 

Follow the steps below to start the server.

## Prerequisites
Make sure you have **Python 3.8+** installed on your system. 

## Getting Started

### 1. Open your terminal and navigate to the backend directory
(If you aren't already there)
```bash
cd backend
```

### 2. Create a Virtual Environment
It's best practice to isolate Python dependencies in a virtual environment.
```bash
# On Linux/macOS
python3 -m venv venv

# On Windows
python -m venv venv
```

### 3. Activate the Virtual Environment
Activate the environment so that packages install locally rather than globally on your system.
```bash
# On Linux/macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```
*(You should now see `(venv)` at the beginning of your terminal prompt).*

### 4. Install Dependencies
Install all required libraries (like FastAPI and Uvicorn) using the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 5. Start the Development Server
Use `uvicorn` to run the FastAPI application. The `--reload` flag makes the server restart automatically whenever you modify the code.
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Exploring the API

One of the best features of FastAPI is its automatic interactive API documentation. 
Once your server is running, open your web browser and go to:

👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

This will open the **Swagger UI**. You can see all the available API routes (like `/api/tk`, `/api/fees`, `/api/legal`), inspect what data they expect, and even test them directly from your browser by clicking "Try it out"!

## Project Structure
- `app/main.py`: The main FastAPI application file containing all the API routes.
- `data/`: Contains the JSON/JSONC files that act as the database for the application (e.g., fees, legal policies, TK records).
- `requirements.txt`: The list of Python packages required to run the server.