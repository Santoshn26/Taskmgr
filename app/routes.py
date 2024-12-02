from flask import Blueprint, request, jsonify, render_template
from app.models import get_tasks, add_task
import os

def register_routes(app):
    # Define routes only once
    @app.route('/')
    def index():
        print("Loading index.html")
        print("Template folder:", app.template_folder) 
        print(os.listdir(app.template_folder))  # Ensure Flask can find the templates
        return render_template('index.html')  # Make sure index.html exists in templates folder
        
    @app.route('/tasks', methods=['GET'])
    def fetch_tasks():
        tasks = get_tasks()
        return jsonify(tasks), 200

    @app.route('/tasks', methods=['POST'])
    def create_task():
        data = request.json
        description = data.get('description')
        if not description:
            return {"error": "Task description is required"}, 400
        add_task(description)
        return {"message": "Task added successfully"}, 201
