from marshmallow import Schema, fields

class PaymentDeserializeSchema(Schema):
    card = fields.String(required=True)
    date = fields.String(required=True)
    cvv = fields.String(required=True)
    name = fields.String(required=True)

class PaymentSerializeSchema(Schema):
    id = fields.UUID()
    card = fields.String()
    date = fields.String()
    cvv = fields.String()
    name = fields.String()
    updateAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')
    createdAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')