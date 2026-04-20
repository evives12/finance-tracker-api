# Finance Tracker REST API

A backend application built using Python, Flask, and SQLAlchemy to
manage, filter, and analyze financial transactions.

This project was built to practice backend development concepts
including RESTful API design, database modeling, and data analysis.

------------------------------------------------------------------------

## Features

-   Create, retrieve, and delete transactions
-   Filter transactions by category and date range
-   Aggregated spending summary by category
-   Input validation and error handling
-   RESTful API design

------------------------------------------------------------------------

## Tech Stack

-   Python
-   Flask
-   Flask-SQLAlchemy
-   SQLite

------------------------------------------------------------------------

## Project Structure
```
finance-tracker-api/ 
    │── app.py 
    │── config.py 
    │── models.py 
    │──requirements.txt 
    │── README.md
```
------------------------------------------------------------------------

## API Endpoints
```
POST /transactions
GET /transactions
GET /transactions?category=Food
GET /transactions?start_date=2026-04-01&end_date=2026-04-30
DELETE /transactions/{id}
GET /summary
GET /summary/category
```
------------------------------------------------------------------------

##  Example Response

```json
[
  {
    "id": 1,
    "amount": 25.5,
    "category": "Food",
    "description": "Lunch",
    "transaction_type": "expense",
    "date": "2026-04-17"
  }
]
```
------------------------------------------------------------------------

## Error Handling Example

```json
{ 
  "error": "Transaction not found"
}
```
------------------------------------------------------------------------

## How to Run

```
git clone https://github.com/evives12/finance-tracker-api.git
cd finance-tracker-api
pip install -r requirements.txt
python app.py
```


------------------------------------------------------------------------

 ## Future Improvements

-   Add authentication (JWT)
-   Deploy API to a cloud platform
-   Connect to PostgreSQL
-   Build a frontend interface