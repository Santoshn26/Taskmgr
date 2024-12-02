from flask import Blueprint, request, jsonify
from app.models import get_tasks, add_task
from flask import render_template
import os

#print("Template folder:", app.template_folder)

def register_routes(app):
    @app.route('/')
    def index():
        print("Loading test.html")
        print(os.listdir('templates'))  # Check if Flask can find the directory
        return render_template('index.html')
        
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
