# Healthcare-ETL-Pipeline
Python ETL pipeline that extracts patient data from JSON, flags health risks, and loads it into a SQLite database. Demonstrates data processing, transformation, and database management skills through a healthcare focused end to end project.

## Features

- Extract patient data from JSON files
- Transform data by adding risk flags and categorizing patient risk levels
- Load transformed data into a SQLite database
- Demonstrates Python scripting, data processing, and database management

## Technologies Used

- Python 3
- JSON for data storage
- SQLite for database management
- VS Code for development

## Project Structure

data/: Folder containing raw and processed JSON and SQLite DB

app/:
  - extract.py: Script to extract/generate raw patient data
  - transform.py: Script to transform raw data and add risk flags
  - load.py: Script to load transformed data into SQLite DB

venv/: Python virtual environment folder


## Getting Started

### Prerequisites

- Python 3 installed on your machine
- VS Code or any preferred IDE
- Required Python packages: `json`, `sqlite3`

### Running the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/Healthcare-ETL-Pipeline.git
cd Healthcare-ETL-Pipeline
