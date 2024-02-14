from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    full_name = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    confirm_password = fields.Str(required=True, load_only=True)


class UserUpdateSchema(Schema):
    full_name = fields.Str()
    username = fields.Str()
    password = fields.Str()


class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
