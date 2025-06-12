from MarketMason.extensions import db

class Product(db.Model):
    __tablename__ = 'products'
    id           = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(128), nullable=False)
    price        = db.Column(db.Float, nullable=False)

    # optional back‐ref if you wire orders later
    orders       = db.relationship(
        'Order',
        secondary='order_product',
        back_populates='products'
    )
