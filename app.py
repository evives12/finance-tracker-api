from flask import Flask, request, jsonify
from sqlalchemy import Transaction

from config import Config
from models import db, Transaction
from datetime import date, datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def home():
    return {"message": "Finance Tracker API is running"}

@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()

    #input validation
    required_fields = ['amount', 'category', 'description', 'transaction_type', 'date' ]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required."}), 400

    try:
        new_transaction = Transaction(
            amount=float(data['amount']),
            category=data['category'],
            description=data['description'],
            transaction_type=data['transaction_type'],
            date=datetime.strptime(data['date'], '%Y-%m-%d').date()
        )

        db.session.add(new_transaction)
        db.session.commit()

        return jsonify({"message": "Transaction created successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/transactions', methods=['GET'])
def get_transactions():
    category = request.args.get('category')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = Transaction.query

    if category:
        query = query.filter_by(category=category)

    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        query = query.filter(Transaction.date >= start_date)

    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        query = query.filter(Transaction.date <= end_date)

    transactions = query.all()

    results = []

    for transaction in transactions:
        results.append({
            "id": transaction.id,
            "amount": transaction.amount,
            "category": transaction.category,
            "description": transaction.description,
            "transaction_type": transaction.transaction_type,
            "date": transaction.date.strftime('%Y-%m-%d')
        })

    return jsonify(results), 200

@app.route('/summary', methods=['GET'])
def get_summary():
    transactions = Transaction.query.all()
    total_income = 0
    total_expense = 0

    for transaction in transactions:
        if transaction.transaction_type.lower() == 'income':
            total_income += transaction.amount
        elif transaction.transaction_type.lower() == 'expense':
            total_expense += transaction.amount

    return jsonify({
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    }), 200

@app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)

    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404

    db.session.delete(transaction)
    db.session.commit()

    return jsonify({"message": "Transaction deleted successfully"}), 200
@app.route('/summary/category', methods=['GET'])
def category_summary():
    transactions = Transaction.query.all()
    summary = {}

    for transaction in transactions:
        category = transaction.category

        if category not in summary:
            summary[category] = 0

        summary[category] += transaction.amount

    return jsonify(summary), 200



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)