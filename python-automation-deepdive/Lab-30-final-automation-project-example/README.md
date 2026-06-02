# API Automation Pipeline (Python)

## Overview
This project is a Python-based automation pipeline that fetches data from a public API, processes it, filters results dynamically using CLI arguments, and stores output in a CSV file with logging support.

It simulates a real-world ETL-style automation workflow used in DevOps and AIOps systems.

---

## Features
- API data fetching using requests
- Data transformation and filtering
- CLI-based dynamic input (--user_id)
- CSV output generation
- Logging for monitoring and debugging
- Error handling for production safety

---

## Tech Stack
- Python 3
- Requests library
- CSV module
- Logging module
- Argparse module

---

## Project Structure
fetch_data.py # Main automation script
user_posts.csv # Output file
app.log # Execution logs
screenshots/ # Execution proof

---

## How to Run

### Default run
```bash
python fetch_data.py
CLI run
python fetch_data.py --user_id 3
#Screenshots
Execution Output

CLI Execution

CSV Output

Logs

#Key Learnings
Building API-based automation pipelines
Data transformation techniques in Python
CLI tool development
Logging and error handling for production scripts
Structuring code like real DevOps tools
