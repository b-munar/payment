from marshmallow import Schema, fields

class NoteDeserializeSchema(Schema):
    note = fields.String(required=True)

class NoteSerializeSchema(Schema):
    id = fields.UUID()
    note = fields.String()
    updateAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')
    createdAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')