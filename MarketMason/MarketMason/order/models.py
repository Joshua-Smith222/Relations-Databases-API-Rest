from MarketMason.extensions import db
from datetime import datetime

order_product = db.Table(
    'order_product',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.UniqueConstraint('order_id', 'product_id', name='order_product_uc')
)


class Order(db.Model):
    __tablename__ = 'orders'
    id         = db.Column(db.Integer,   primary_key=True)
    order_date = db.Column(db.DateTime,  default=datetime.utcnow, nullable=False)
    user_id    = db.Column(db.Integer,   db.ForeignKey('users.id'), nullable=False)

    products = db.relationship(
       'Product',
       secondary=order_product,
       back_populates='orders'
    )


    # optional back‐ref if you wire products later
    products = db.relationship(
        'Product',
        secondary='order_product',
        back_populates='orders'
    )
