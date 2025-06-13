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
            'user_id',
            'products'
        )
        unknown = EXCLUDE

    @pre_load
    def normalize_keys(self, data, **kwargs):
        return { k.lower(): v for k, v in data.items() }

order_schema   = OrderSchema()
orders_schema  = OrderSchema(many=True)
