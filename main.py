from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

students = [];

class Student(BaseModel):
    id: int
    name: str
    age: int
    grade: str

@app.get("/students")
def get_students():
    return { "students": students }

@app.post('/students')
def create_student(student: Student):
    students.append(student)
    return { "message": "Student Added", "student": student }

@app.get('/student/{id}')
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    #if not found
    raise HTTPException(status_code=404, detail="Student not found")

@app.put('/student/{id}')
def update_student(id: int, updated_student: Student):
    print(id, updated_student)
    for index, student in enumerate(students):
        if student.id == id:
            students[index] = updated_student
            return { "message": "Student Updated", "student": updated_student }
    raise HTTPException(status_code=404, detail="Student not found")