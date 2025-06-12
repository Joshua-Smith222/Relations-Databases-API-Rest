from MarketMason.extensions import ma
from .models import Order

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True
        include_relationships = True

order_schema   = OrderSchema()
orders_schema  = OrderSchema(many=True)
