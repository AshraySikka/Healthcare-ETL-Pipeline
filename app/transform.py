import json

# This will load the data from raw JSON
with open("data/raw_patients.json", "r") as f:
    patients = json.load(f)

# This will flag the risky patients
for patient in patients:
    systolic = patient["blood_pressure_systolic"]
    diastolic = patient["blood_pressure_diastolic"]
    heart_rate = patient["heart_rate"]

    patient["risk_flags"] = []

    if systolic > 140 or diastolic > 90:
        patient["risk_flags"].append("high_blood_pressure")

    if heart_rate < 60 or heart_rate > 100:
        patient["risk_flags"].append("abnormal_heart_rate")

    # Classifying the risk category based on the flags
    if "high_blood_pressure" in patient["risk_flags"] or "abnormal_heart_rate" in patient["risk_flags"]:
        patient["risk_category"] = "high"
    else:
        patient["risk_category"] = "low"

# Save the data with risk flags and categories to a new JSON file
with open("data/transformed_patients.json", "w") as f:
    json.dump(patients, f, indent=4)

print("Transformed patient data saved to data/transformed_patients.json")
