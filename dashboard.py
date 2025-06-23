import streamlit as st
import sqlite3
import pandas as pd

# This will set the page configuration for the Streamlit Dashboard
st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

# This will connect to SQLite database (that I created in the ETL process)
conn = sqlite3.connect("data/patient_data.db")
query = "SELECT * FROM patients"
df = pd.read_sql_query(query, conn)

st.title("Healthcare ETL Dashboard")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Patients", len(df))
col2.metric("High Risk", len(df[df["risk_category"] == "high"]))
col3.metric("Low Risk", len(df[df["risk_category"] == "low"]))

# Filters
st.sidebar.header("Filter Patients")
age_filter = st.sidebar.slider(
    "Age Range", 
    int(df["age"].min()), 
    int(df["age"].max()), 
    (20, 60)
)
gender_filter = st.sidebar.multiselect(
    "Gender", 
    df["gender"].unique(), 
    default=list(df["gender"].unique())
)
all_flags = set()
for flags in df["risk_flags"]:
    if flags.strip() == "":
        all_flags.add("None")
    else:
        for flag in flags.split(", "):
            if flag:
                all_flags.add(flag)

risk_flag_filter = st.sidebar.multiselect(
    "Risk Flags",
    sorted(all_flags),
    default=list(sorted(all_flags))
)

# This will apply the filters
filtered_df = df[
    (df["age"] >= age_filter[0]) &
    (df["age"] <= age_filter[1]) &
    (df["gender"].isin(gender_filter)) &
    (df["risk_flags"].apply(lambda x: ("None" in risk_flag_filter and x.strip() == "") or any(flag in x for flag in risk_flag_filter)))
]

st.subheader("Patient Records")
st.dataframe(filtered_df)

conn.close()
