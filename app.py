from flask import Flask, request, jsonify
from config import Config
from models import db, Transaction

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
            date=data['date']
        )

        db.session.add(new_transaction)
        db.session.commit()

        return jsonify({"message": "Transaction created successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/transactions', methods=['GET'])
def get_transactions():
    category = request.args.get('category')

    if category:
        transactions = Transaction.query.filter_by(category=category).all()
    else:
        transactions = Transaction.query.all()

    results = []

    for transaction in transactions:
        results.append({
            "id": transaction.id,
            "amount": transaction.amount,
            "category": transaction.category,
            "description": transaction.description,
            "transaction_type": transaction.transaction_type,
            "date": transaction.date
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


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)