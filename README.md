#  Student Grade Analyzer

A modular and efficient Python tool to analyze student marks using statistical methods.  
This project allows users to load marks from a CSV file or enter them manually, compute all key statistics, analyze class performance, and generate a structured JSON report.  
All logs are stored in a log file for debugging and tracking.

This project fulfills academic requirements for Python Programming, covering modular design, file handling, functions, logging, and structured reporting.


##  Features

###  1. CSV / Manual Input Options
- Load marks from a `.csv` file  
- OR enter marks manually through the command-line interface  

###  2. Statistical Analysis
Automatically calculates:
- Mean  
- Median  
- Mode  
- Variance  
- Standard deviation  
- Highest and lowest marks  

###  3. Performance Evaluation
- Total students  
- Passed and failed count  
- Pass percentage  
- Top 3 performers  
- Weakest 3 performers  

###  4. Report Generator
- Generates `report.json` with:
  - Full statistical summary  
  - Performance insights  

###  5. Logging
- All warnings, errors, and processes are stored in `grade_analyzer.log`  

##  Technologies Used

- **Python 3.x**
- Standard libraries only:
  - `csv`
  - `statistics`
  - `json`
  - `logging`

No external libraries required.

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
├── data/ (optional)
│   └── sample_marks.csv
│
├── screenshots/ (add yourself)
│
├── README.md
├── statement.md
└── requirements.txt
```

---

##  How to Run the Project

### 1️ Step into the project folder
```
cd Student_Grade_Analyzer
```

### 2️ Run the main file

Windows:
python src/main.py

Mac/Linux:
python3 src/main.py

### 3️ Choose input method
1. Load marks from CSV
2. Enter marks manually
3. Exit

### 📌 CSV Format Example

Name,Marks
Rahul,78
Sneha,65
Vijay,32
Nisha,92
Amit,55
```

---

##  Output Files Generated

### `report.json`
Contains:
- All computed statistics  
- Performance evaluation results  

### `grade_analyzer.log`
Contains:
- Warnings  
- Errors  
- Execution details  

##  License
This project is open for educational and academic use.

---

##  Author
**Aditya Singh**


