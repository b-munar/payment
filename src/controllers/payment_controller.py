from flask_restful import Resource
from flask import request

from src.database.session import Session
from src.models.payment_model import CardModel
from src.schemas.payment_schema import PaymentDeserializeSchema, PaymentSerializeSchema
from src.utils.authorization import authorization

class PaymentController(Resource):
    method_decorators = [authorization]
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        payment_create_schema = PaymentDeserializeSchema()
        
        errors = payment_create_schema.validate(request_json)
        if errors:
            return "", 400
        
        payment_create_dump = payment_create_schema.dump(request_json)
        payment_create_dump["user"] = kwargs["user"]["id"]
        
        # token = kwargs["token"]
        # If you need to use another microservice,
        # use this token with the request library,
        # remember to paste the Bearer before the token
        
        session = Session()
        new_payment = CardModel(**payment_create_dump)
        session.add(new_payment)
        session.commit()

        payment_created_schema = PaymentSerializeSchema()
        payment_created_dump = payment_created_schema.dump(new_payment)
        return payment_created_dump, 201
    
    def get(self, **kwargs):
        payment_schema = PaymentSerializeSchema()

        session = Session()
        query = session.query(CardModel).filter(CardModel.user==kwargs["user"]["id"])
        session.close()
        
        payments = [payment_schema.dump(payment) for payment in query]
        return payments, 200

