from flask import Flask
from flask_cors import CORS
from routes.qa_routes import qa_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints
    app.register_blueprint(qa_blueprint, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
