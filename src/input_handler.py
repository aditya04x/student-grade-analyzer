import csv
from utils.logger import get_logger

logger = get_logger(__name__)

def load_marks_from_csv(path):
    marks = []
    try:
        with open(path) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                try:
                    marks.append(float(row[1]))
                except:
                    logger.warning(f"Invalid row: {row}")
    except Exception as e:
        logger.error(e)
    return marks

def input_marks_manually():
    marks = []
    print("Enter marks (type 'done'):")
    while True:
        x = input("Mark: ").strip()
        if x.lower() == "done":
            break
        try:
            marks.append(float(x))
        except:
            print("Invalid input")
    return marks
