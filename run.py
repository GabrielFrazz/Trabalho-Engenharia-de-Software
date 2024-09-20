from app import app
from app.engine.security import Admin
from app.api_routes import api

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
