from input_handler import load_marks_from_csv, input_marks_manually
from stats_calculator import calculate_statistics
from performance_analyzer import analyze_performance
from report_generator import generate_report
from utils.logger import get_logger

logger = get_logger(__name__)

def menu():
    print("\n===== STUDENT GRADE ANALYZER =====")
    print("1. Load marks from CSV")
    print("2. Enter marks manually")
    print("3. Exit")
    return input("Choose option: ")

def main():
    while True:
        c = menu()

        if c == "1":
            path = input("CSV path: ")
            marks = load_marks_from_csv(path)

        elif c == "2":
            marks = input_marks_manually()

        elif c == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
            continue

        if not marks:
            print("No marks found.")
            continue

        stats = calculate_statistics(marks)
        perf = analyze_performance(marks)
        generate_report(stats, perf)

        print("\n--- ANALYSIS COMPLETE ---")
        print("Mean:", stats["mean"])
        print("Median:", stats["median"])
        print("Pass %:", perf["pass_percentage"])
        print("-------------------------------")

if __name__ == "__main__":
    main()
