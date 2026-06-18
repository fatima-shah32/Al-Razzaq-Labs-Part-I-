# Lab 01: Introduction to Python for ML

## Objective

Understand the basics of Python and its importance in Machine Learning.

---

## Task 1: Verify Python Installation

```bash
python3 --version
Python is a high-level interpreted programming language widely used in Machine Learning because it is readable, simple, and has powerful ML libraries.

Task 2: Create Virtual Environment
python3 -m venv ml-env
source ml-env/bin/activate
Task 3: Install ML Libraries
pip install numpy pandas scikit-learn
Task 4: Check Installed Libraries

File: check_libraries.py

import numpy as np
import pandas as pd
import sklearn

print("NumPy Version:", np.__version__)
print("Pandas Version:", pd.__version__)
print("Scikit-Learn Version:", sklearn.__version__)

Run:

python check_libraries.py
Task 5: Hello ML Program

File: hello_ml.py

print("Hello, ML")

Run:

python hello_ml.py

Expected output:

Hello, ML
Summary
Command	Purpose
python3 --version	Check Python version
python3 -m venv ml-env	Create virtual environment
source ml-env/bin/activate	Activate environment
pip install numpy pandas scikit-learn	Install ML libraries
python hello_ml.py	Run Hello ML script
python check_libraries.py	Check library versions
Conclusion

In this lab, I learned the basics of Python for Machine Learning, installed essential ML libraries, and created a simple Hello ML program.
