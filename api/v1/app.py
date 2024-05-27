from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', '5000')
app.config['SERVER_NAME'] = f"{host}:{port}"


app.register_blueprint(blueprint=app_views)


@app.teardown_appcontext
def close_storage(exc=None):
    """
    closes the storage engine
    """
    storage.close()


if __name__ == "__main__":
    app.run(host=host, port=int(port), threaded=True)
