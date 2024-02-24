from flask import Flask
from . import pet
from . import fact

def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def index():
        return 'Hello, Petfax!'
    
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    return app