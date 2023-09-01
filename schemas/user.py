from marshmallow import Schema, ValidationError, fields, validates
from models.user import Role, Status, User


class UserSchema(Schema):
    id = fields.Integer(dumps_only=True)
    name = fields.Str(required=True)
    date_of_birth = fields.Date(format="%Y-%m-%d", allow_none=True, default=None)
    status = fields.Enum(Status, required=True)
    role = fields.Enum(Role, required=True)
    picture = fields.Raw(allow_none=True)
    password = fields.Str(allow_none=False, required=True)
    is_deleted = fields.Boolean(default=False, load_only=True)
    email = fields.Email(required=True)

    @validates("name")
    def validate_username(self, value: str):
        if value.isspace():
            raise ValidationError("Username cannot be empty")

    @classmethod
    def create_schema_obj_from_dbo(cls, user_obj: User):
        return cls().load(
            {
                "id": user_obj.id,
                "password": user_obj.password,
                "picture": user_obj.picture,
                "is_deleted": user_obj.is_deleted,
                "role": user_obj.role,
                "status": user_obj.status,
                "date_of_birth": user_obj.date_of_birth,
                "name": user_obj.name,
            }
        )

    class Meta:
        exclude = ("is_deleted",)
