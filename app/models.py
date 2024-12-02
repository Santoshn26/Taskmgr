from app.database import mysql

def get_tasks():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    return tasks

def add_task(description):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO tasks (description, status) VALUES (%s, %s)", (description, "Pending"))
    mysql.connection.commit()
    cursor.close()
