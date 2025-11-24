# Project Statement – Student Grade Analyzer

## 1. Problem Statement
Teachers and students often have marks stored in spreadsheets or written in notebooks, and analyzing them manually takes time.  
Calculating averages, finding top performers, or knowing how many students passed or failed usually requires repetitive work.  
Mistakes also happen easily when numbers are entered or calculated manually.

To make this process simpler and more accurate, I created a Python-based tool that can automatically analyze student marks and generate useful insights.


## 2. Scope of the Project
This project focuses on helping users:
- Load marks from a CSV file or enter them manually  
- Automatically calculate important statistical values  
- Analyze overall class performance  
- Generate a clean report in JSON format  
- Keep logs of issues or invalid entries  

The project does not include:
- A GUI (graphical interface)  
- Database storage  
- Visualization graphs (these can be added in the future)


## 3. Target Users
This project can be helpful for:
- Teachers who want quick insights into student performance  
- Students who want to analyze their own or a batch’s marks  
- Educational evaluators  
- Beginners learning Python and data handling  
- Anyone who wants an automated way to analyze marks  


## 4. High-Level Features

###  Input Handling
Users can:
- Load a CSV file containing names and marks  
- Enter marks manually through the terminal  

###  Statistical Calculations
The system calculates:
- Mean  
- Median  
- Mode  
- Variance  
- Standard deviation  
- Highest and lowest marks  

###  Performance Insights
The tool evaluates:
- Total students  
- Number of passed and failed students  
- Pass percentage  
- Top 3 performers  
- Lowest 3 performers  

###  Report Generation
All results are saved neatly in a report.json file so they can be viewed anytime or shared easily.

###  Logging
A log file (grade_analyzer.log) records:
- Errors  
- Warnings  
- Invalid CSV rows  
- Program activity  


This project successfully shows how Python can be used for real-world data handling, automation, and statistical analysis in a simple and practical way.

