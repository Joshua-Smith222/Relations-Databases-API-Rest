from marshmallow import EXCLUDE, pre_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from MarketMason.extensions import ma
from .models import Order

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True
        include_relationships = True
        fields = (
            'id',
            'order_date',
            'customer_name',
            'total_amount',
            'products'
        )
        unknown = EXCLUDE

    @pre_load
    def normalize_keys(self, data, **kwargs):
        normalized = {}
        for key, val in data.items():
            lk = key.lower()
            if lk in ('customer_name', 'order_date'):
                normalized[lk] = val
            else:
                normalized[key] = val
        return normalized

order_schema   = OrderSchema()
orders_schema  = OrderSchema(many=True)
