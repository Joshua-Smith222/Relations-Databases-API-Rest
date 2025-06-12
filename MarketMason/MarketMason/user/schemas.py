# user/schemas.py
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import pre_load, ValidationError
from MarketMason.extensions import ma
from .models import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True   # if you ever include foreign-keys
        include_relationships = True

    @pre_load
    def normalize_keys(self, data, **kwargs):
        normalized = {}
        for key, val in data.items():
            lk = key.lower()
            if lk in ('username', 'email'):
                normalized[lk] = val
            else:
                normalized[key] = val
        return normalized
# instantiate them for import
user_schema  = UserSchema()
users_schema = UserSchema(many=True)
