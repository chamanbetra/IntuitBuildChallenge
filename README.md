# IntuitBuildChallenge
Build Challenge - Intuit - Chaman Betrabet

This repository contains two Python assignments completed as part of the Intuit Build Challenge.  
Both assignments demonstrate clean code, modular structure, unit testing, and Python best practices.

---

#🛠 Common Setup Instructions

These instructions apply to both Assignment1 and 2

## 1️⃣ Install Python 3

Make sure Python 3.x is installed:

```bash
python3 --version
```
##  Create virtual environment if needed 

```bash
python3 -m venv venv
```

Activate it:
Mac/Linux:
```bash
source venv/bin/activate
```
Windows:
```bash
venv\Scripts\activate
```

# 📘 Assignment 1 — Producer–Consumer Pattern (Multithreading)

### **Description**
Implements a classic Producer–Consumer system using:
- `threading.Thread`
- `queue.Queue`
- Proper locking & synchronization
- Graceful thread shutdown

This assignment demonstrates:
- Concurrency handling in Python  
- Thread-safe communication  
- Deterministic consumption of produced items

### **How to Run**
```bash
cd "Producer Consumer Pattern"
python3 main_assignment1.py
```
### **Sample Output**
<img width="1722" height="748" alt="image" src="https://github.com/user-attachments/assets/5304cc5c-1328-4a7a-af98-0e1bac374679" />

### **Run Tests** 
```bash
python3 -m unittest test_assignment1.py
```

# 📘 Assignment 2 — CSV Sales Data Analysis 

### **Description**
This assignment performs data analysis on a sales dataset using Python and pandas.  
It demonstrates data ingestion, grouping, filtering, aggregation, sorting, and unit testing.

A sample CSV file is auto-generated if the `data/` folder does not contain one. 

### **How to Run**
```bash
cd "CSVDataAnalysis"
python3 main_assignment2.py
```

### **Sample Output**
<img width="952" height="465" alt="Screenshot 2025-11-19 at 1 31 00 PM" src="https://github.com/user-attachments/assets/d8f90ef5-c7c2-473c-876f-e4f423a38289" />

### **Run Tests** 
```bash
python3 -m unittest test_assignment2.py
```




