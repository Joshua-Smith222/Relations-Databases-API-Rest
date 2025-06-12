# MarketMason/api.py
from flask import Blueprint, request, jsonify, abort
from .extensions import db
from .user.models import User
from MarketMason.user.schemas import user_schema, users_schema
# from .product.models import Product
# from .product.schemas import product_schema, products_schema
# from .order.models   import Order
# from .order.schemas  import order_schema, orders_schema

api = Blueprint('api', __name__, url_prefix='/api')

# — Users —
@api.route('/users', methods=['GET'])
def get_users():
    """GET /api/users → list all users"""
    return users_schema.jsonify(User.query.all())

@api.route('/users', methods=['POST'])
def create_user():
    """POST /api/users → create a new user"""
    data = request.get_json() or {}
    user = user_schema.load(data, session=db.session)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201

# (Repeat similarly for Products & Orders)
