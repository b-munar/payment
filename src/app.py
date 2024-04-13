from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.controllers.ping_controller import Ping
from src.controllers.payment_controller import PaymentController

def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    api.add_resource(Ping, '/payment/ping')
    api.add_resource(PaymentController, '/payment')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=80, host='0.0.0.0')
else:
    gunicorn_app = create_app()