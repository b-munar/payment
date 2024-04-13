from marshmallow import Schema, fields

class PaymentDeserializeSchema(Schema):
    payment = fields.String(required=True)

class PaymentSerializeSchema(Schema):
    id = fields.UUID()
    payment = fields.String()
    updateAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')
    createdAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')