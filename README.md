#  Finance Tracker REST API

A backend application built using Python, Flask, and SQLAlchemy to manage, filter, and analyze financial transactions.

---

##  Features

- Create, retrieve, and delete transactions
- Filter transactions by category and date range
- Aggregated spending summary by category
- Input validation and error handling
- RESTful API design

---

##  Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite

---

##  API Endpoints

### Create Transaction
POST /transactions

### Get All Transactions
GET /transactions

### Filter Transactions
GET /transactions?category=Food  
GET /transactions?start_date=2026-04-01&end_date=2026-04-30

### Delete Transaction
DELETE /transactions/{id}

### Summary
GET /summary  
GET /summary/category

---

## How to Run

```bash
git clone https://github.com/evives12/finance-tracker-api.git
cd finance-tracker-api
pip install -r requirements.txt
python app.py
```

---

## Future Improvements

- Add authentication (JWT)
- Deploy API
- Connect to PostgreSQL
- Frontend interface