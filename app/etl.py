import json
import random
from datetime import datetime, timedelta

# This will generate list of random patients for testing purposes
patients = []

for i in range(1, 16):
    patient = {
        "patient_id": i,
        "age": random.randint(20, 90),
        "gender": random.choice(["M", "F"]),
        "blood_pressure_systolic": random.randint(90, 160),
        "blood_pressure_diastolic": random.randint(60, 100),
        "heart_rate": random.randint(55, 110),
        "appointment_date": (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
    }
    patients.append(patient)

# This will write the random data generated to the JSON file
with open("data/raw_patients.json", "w") as f:
    json.dump(patients, f, indent=4)

print("Patient data generated and saved to data/raw_patients.json")
