from MarketMason.extensions import ma
from .models import Product

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model               = Product
        load_instance       = True
        include_fk          = True
        include_relationships = True

product_schema   = ProductSchema()
products_schema  = ProductSchema(many=True)
