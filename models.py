from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction (db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)