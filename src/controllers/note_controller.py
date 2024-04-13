from flask_restful import Resource
from flask import request

from src.database.session import Session
from src.models.note_model import NoteModel
from src.schemas.note_schema import NoteDeserializeSchema, NoteSerializeSchema
from src.utils.authorization import authorization

class NoteController(Resource):
    method_decorators = [authorization]
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        note_create_schema = NoteDeserializeSchema()
        
        errors = note_create_schema.validate(request_json)
        if errors:
            return "", 400
        
        note_create_dump = note_create_schema.dump(request_json)
        note_create_dump["user"] = kwargs["user"]["id"]
        
        # token = kwargs["token"]
        # If you need to use another microservice,
        # use this token with the request library,
        # remember to paste the Bearer before the token
        
        session = Session()
        new_note = NoteModel(**note_create_dump)
        session.add(new_note)
        session.commit()

        note_created_schema = NoteSerializeSchema()
        note_created_dump = note_created_schema.dump(new_note)
        return note_created_dump, 201
    
    def get(self, **kwargs):
        note_schema = NoteSerializeSchema()

        session = Session()
        query = session.query(NoteModel).filter(NoteModel.user==kwargs["user"]["id"])
        session.close()
        
        notes = [note_schema.dump(note) for note in query]
        return notes, 200

