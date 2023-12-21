from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

# Data model using Pydantic
class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str

class Student(StudentCreate):
    id: int

# Database connection setup
def create_connection():
    connection = sqlite3.connect("students.db")
    return connection

# Create table if not exists
def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )
    """)
    connection.commit()
    connection.close()

create_table()

# CRUD functions
def create_student(student: StudentCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (student.name, student.age, student.grade))
    connection.commit()
    student_id = cursor.lastrowid
    connection.close()
    return student_id

def read_students():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    connection.close()
    return [Student(id=row[0], name=row[1], age=row[2], grade=row[3]) for row in students]

def read_student(student_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()
    connection.close()
    if student:
        return Student(id=student[0], name=student[1], age=student[2], grade=student[3])
    raise HTTPException(status_code=404, detail="Student not found")

def update_student(student_id: int, updated_student: StudentCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (updated_student.name, updated_student.age, updated_student.grade, student_id))
    connection.commit()
    connection.close()
    return {"message": "Student updated successfully"}

def delete_student(student_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    connection.commit()
    connection.close()
    return {"message": "Student deleted successfully"}

# FastAPI endpoints
@app.post("/students/", response_model=Student)
def create_student_endpoint(student: StudentCreate):
    student_id = create_student(student)
    return {"id": student_id, **student.dict()}

@app.get("/students/", response_model=List[Student])
def read_students_endpoint():
    return read_students()

@app.get("/students/{student_id}", response_model=Student)
def read_student_endpoint(student_id: int):
    return read_student(student_id)

@app.put("/students/{student_id}")
def update_student_endpoint(student_id: int, updated_student: StudentCreate):
    return update_student(student_id, updated_student)

@app.delete("/students/{student_id}")
def delete_student_endpoint(student_id: int):
    return delete_student(student_id)
