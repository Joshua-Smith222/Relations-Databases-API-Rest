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
    order = order_schema.load(data, session=db.session)
    db.session.add(order)
    db.session.commit()
    return order_schema.jsonify(order), 201
@api.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['PUT'])
@csrf_protect.exempt
def add_product_to_order(order_id, product_id):
    """PUT /api/orders/<order_id>/add_product/<product_id> → add a product to an order"""
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    order.products.append(product)
    db.session.commit()
    return order_schema.jsonify(order), 200
@api.route('/orders/<int:order_id>/remove_product/<int:product_id>', methods=['DELETE'])
@csrf_protect.exempt
def remove_product_from_order(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    if product in order.products:
        order.products.remove(product)
        db.session.commit()
    # return the updated order as JSON
    return order_schema.jsonify(order), 200


@api.route('/orders/user/<int:user_id>', methods=['GET'])
@csrf_protect.exempt
def get_orders_for_user(user_id):
    """GET /api/orders/user/<user_id> → list all orders belonging to that user."""
    orders = Order.query.filter_by(user_id=user_id).all()
    return orders_schema.jsonify(orders)


@api.route('/orders/<int:order_id>/products', methods=['GET'])
@csrf_protect.exempt
def get_products_for_order(order_id):
    """GET /api/orders/<order_id>/products → list all products on that order."""
    order = Order.query.get_or_404(order_id)
    # order.products is a list of Product objects
    return products_schema.jsonify(order.products)
