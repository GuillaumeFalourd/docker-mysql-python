from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/employees")
async def get_employees():
    connection = mysql.connector.connect(
        user='root',
        password='RootPassword',
        host='mysql',
        port='3306',
        database='Company'
    )
    print('DB connected')
    cursor = connection.cursor(dictionary=True)
    cursor.execute('Select * FROM employees')
    employees = cursor.fetchall()
    datas = []
    for employee in employees:
        print(employee)
        data = {
            "first_name": employee["first_name"],
            "last_name": employee["last_name"],
            "email": employee["email"],
            "department": employee["department"]
        }
        datas.append(data)
    connection.close()
    print('DB closed')
    return { 'employees' : datas }
