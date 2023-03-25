import database
import ormar

class User(ormar.Model):
    class Meta:
        tablename: str = "users"
    id: int = ormar.Integer(primary_key=True)
    # email: str = ormar.String(max_length=255)
    # password: str = ormar.String(max_length=255)
    # first_name: str = ormar.String(max_length=255, nullable=True)
    # last_name: str = ormar.String(max_length=255)
    # category: str = ormar.String(max_length=255, default="User")