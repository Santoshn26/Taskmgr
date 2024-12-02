from app import create_app
from app.routes import register_routes
import os

app = create_app()  # Only create the app once here
#register_routes(app)  # Register routes once

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.config['MYSQL_HOST'] = '192.168.29.142'
    app.config['MYSQL_PORT'] = 3306 
    app.config['MYSQL_USER'] = 'root' 
    app.config['MYSQL_PASSWORD'] = 'Mrdev@0612'  
    app.config['MYSQL_DB'] = 'task_manager' 


