from fastapi import FastAPI
import sqlite3
import json

app = FastAPI()

# This is a function to get data from SQLite database that I created
def get_all_patients():
    
    db_path = "data/patient_data.db"

    conn = sqlite3.connect("data/patient_data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()

    col_names = [description[0] for description in cursor.description]

    # This will convert each row into a dictionary
    patients = [dict(zip(col_names, row)) for row in rows]

    conn.close()
    return patients

# This is the API endpoint to get all patients
@app.get("/patients")
def read_patients():
    try:
        return get_all_patients()
    except Exception as e:
        return {"error": str(e)}
