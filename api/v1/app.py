#!/usr/bin/python3
"""
flask app that runs the api
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(blueprint=app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def do_teardown(self):
    """
    closes the storage engine
    """
    storage.close()


if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST")
    port = os.environ.get("HBNB_API_PORT")
    if not host:
        host = "0.0.0.0"
    if not port:
        port = 5000
    app.run(host=host, port=port, threaded=True)
