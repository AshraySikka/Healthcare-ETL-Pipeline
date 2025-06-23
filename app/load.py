import json
import sqlite3

# This will load the transformed patient data
with open("data/transformed_patients.json", "r") as f:
    patients = json.load(f)

# This will connect to SQLite database
conn = sqlite3.connect("data/patient_data.db")
cursor = conn.cursor()

# This will create patients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY,
    age INTEGER,
    gender TEXT,
    blood_pressure_systolic INTEGER,
    blood_pressure_diastolic INTEGER,
    heart_rate INTEGER,
    appointment_date TEXT,
    risk_category TEXT,
    risk_flags TEXT
)
""")

# This will insert the patient data into table
for patient in patients:
    cursor.execute("""
        INSERT OR REPLACE INTO patients (
            patient_id, age, gender,
            blood_pressure_systolic, blood_pressure_diastolic,
            heart_rate, appointment_date,
            risk_category, risk_flags
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        patient["patient_id"],
        patient["age"],
        patient["gender"],
        patient["blood_pressure_systolic"],
        patient["blood_pressure_diastolic"],
        patient["heart_rate"],
        patient["appointment_date"],
        patient["risk_category"],
        ", ".join(patient["risk_flags"]) 
    ))

# This will commit the changes and close the connection
conn.commit()
conn.close()

print("Patient data successfully loaded into SQLite database.")
