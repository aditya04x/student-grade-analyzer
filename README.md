# Student Grade Analyzer

This is a simple and modular Python project that helps analyze student marks.  
You can load marks from a CSV file or enter them manually, and the program will calculate important statistics and performance insights automatically.  
It also creates a clean JSON report and keeps logs of everything that happens.

This project was built as part of my introduction to problem solving coursework.


## What this project can do

### Load Marks
You can provide marks in two ways:
- Upload a CSV file  
- Enter marks manually in the terminal  

### Calculate Statistics
The program automatically finds:
- Mean  
- Median  
- Mode  
- Variance  
- Standard deviation  
- Highest and lowest marks  

### Analyze Performance
It also breaks down:
- How many students passed and failed  
- Pass percentage  
- Top 3 scorers  
- Weakest 3 scorers  

### Generate Report
Everything (stats + performance) is saved neatly in:
report.json
### Logging
A log file named:
grade_analyzer.log
is created so you can track warnings or errors (like invalid CSV rows).


##  Technologies Used

- Python 3
- Built-in modules:  
  csv, statistics, json, logging

No external libraries needed.


##  Project Structure

Student_Grade_Analyzer/
│
├── src/
│   ├── main.py
│   ├── input_handler.py
│   ├── stats_calculator.py
│   ├── performance_analyzer.py
│   ├── report_generator.py
│   └── utils/
│       └── logger.py
│
├── data/                (optional folder for CSV files)
├── screenshots/         (add your screenshots here)
├── README.md
├── statement.md
└── requirements.txt
---

##  How to Run the Program

### Step 1: Open terminal inside the project folder  
Run:
cd Student_Grade_Analyzer
### Step 2: Run the program  
Windows:
python src/main.py
Mac/Linux:
python3 src/main.py
### Step 3: Choose an option
You will see a menu:

===== STUDENT GRADE ANALYZER =====
1. Load marks from CSV
2. Enter marks manually
3. Exit
Choose the option you want.

##  CSV Format Example

If you choose the CSV option, use this format:

Name,Marks
Rahul,78
Sneha,65
Vijay,32
Nisha,92
Amit,55
Only the second column needs to be numeric.


## Output Files

### 1. report.json  
Contains:
- All calculated statistics  
- Performance breakdown  

### 2. grade_analyzer.log  
Contains logs of:
- Warnings  
- Errors  
- Execution flow  

## Screenshots

- The main menu  
- Final calculated results  
- report.json  
- log file  

## Possible Future Improvements

Here are some ideas that could be added later:
- Graphs using matplotlib  
- Support for multiple subjects  
- Exporting results as PDF  
- Simple GUI using Tkinter  
- Percentage and grade distribution charts  

## Author

Aditya Singh  
Python Programming Project


