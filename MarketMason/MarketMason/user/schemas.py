# user/schemas.py

from MarketMason.extensions import ma
from .models import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True   # if you ever include foreign-keys

# instantiate them for import
user_schema  = UserSchema()
users_schema = UserSchema(many=True)
