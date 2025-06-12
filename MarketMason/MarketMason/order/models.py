from MarketMason.extensions import db

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    customer_name = db.Column(db.String(128), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

    # optional back‐ref if you wire products later
    # products = db.relationship(
    #     'Product',
    #     secondary='order_product',
    #     back_populates='orders'
    # )
