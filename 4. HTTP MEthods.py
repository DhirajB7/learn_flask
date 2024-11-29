import json
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Define the students dictionary
students = {
    "student_1": {
        "name": "Alice Johnson",
        "age": 20,
        "grade": "Sophomore",
        "subjects": ["Math", "Physics", "Computer Science"],
        "GPA": 3.8
    },
    "student_2": {
        "name": "Bob Smith",
        "age": 22,
        "grade": "Senior",
        "subjects": ["English", "History", "Philosophy"],
        "GPA": 3.4
    },
    "student_3": {
        "name": "Charlie Davis",
        "age": 19,
        "grade": "Freshman",
        "subjects": ["Biology", "Chemistry", "Environmental Science"],
        "GPA": 3.9
    },
    "student_4": {
        "name": "Diana Lee",
        "age": 21,
        "grade": "Junior",
        "subjects": ["Economics", "Statistics", "Finance"],
        "GPA": 3.7
    }
}

@app.route('/students/all/')
def get_all():
   return students

@app.route('/students/get/<student_id>/')
def get_by_id(student_id):
    if student_id in students :
        return students.get(student_id)
    else :
        return f'{student_id} not found'

@app.route('/students/add/<student_id>/',methods=['POST'])
def add_student(student_id):
    if student_id not in students :
        students[student_id] = request.json
        return request.json
    else:
        return f'{student_id} already present'

@app.route('/students/edit/<student_id>/',methods=['PUT'])
def edit_student(student_id):
    if student_id  in students :
        students[student_id] = request.json
        return request.json
    else:
        return f'{student_id} not found'

@app.route('/students/delete/<student_id>/',methods=['DELETE'])
def delete_student(student_id):
    if student_id in students :
        students.pop(student_id)
        return f'{student_id} removed.'
    else :
        return f'{student_id} not found'


@app.route('/students/<student_id>/',methods=['GET','POST','PUT','DELETE'])
def many_method(student_id):
    if request.method=='GET':
        return redirect(url_for('get_by_id',student_id=student_id))
    elif request.method=='POST':
        return redirect(url_for('add_student', student_id=student_id))
    elif request.method=='PUT':
        return redirect(url_for('edit_student', student_id=student_id))
    elif request.method=='DELETE':
        return redirect(url_for('delete_student', student_id=student_id))
    else :
        return f'{request.method} is not found'



if __name__ == '__main__':
   app.run('127.0.0.1',3001,True)