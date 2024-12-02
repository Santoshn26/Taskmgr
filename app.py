from app import create_app
import os
from flask import Flask
from app.routes import register_routes  

app = create_app()
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



