# MarketMason/api.py
from flask import Blueprint, request, jsonify, abort
from .extensions import db
from .user.models import User
from MarketMason.user.schemas import user_schema, users_schema
from .extensions import csrf_protect
from .product.models import Product
from .product.schemas import product_schema, products_schema
from .order.models   import Order
from .order.schemas  import order_schema, orders_schema

api = Blueprint('api', __name__, url_prefix='/api')

#tell CSRF to not wrap any api routes
csrf_protect.exempt(api)
# CSRF protection is disabled for API routes

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
@api.route('/products', methods=['GET'])
def get_products():
    """GET /api/products → list all products"""
    return products_schema.jsonify(Product.query.all())

@api.route('/products', methods=['POST'])
def create_product():
    """POST /api/products → create a new product"""
    data = request.get_json() or {}
    p = product_schema.load(data, session=db.session)
    db.session.add(p)
    db.session.commit()
    return product_schema.jsonify(p), 201

@api.route('/orders', methods=['GET'])
def get_orders():
    """GET /api/orders → list all orders"""
    return orders_schema.jsonify(Order.query.all())
@api.route('/orders', methods=['POST'])
def create_order():
    """POST /api/orders → create a new order"""
    data = request.get_json() or {}
    o = order_schema.load(data, session=db.session)
    db.session.add(o)
    db.session.commit()
    return order_schema.jsonify(o), 201
