import statistics
from utils.logger import get_logger

logger = get_logger(__name__)

def calculate_statistics(marks):
    if not marks:
        return None

    stats = {
        "mean": statistics.mean(marks),
        "median": statistics.median(marks),
        "mode": None,
        "variance": None,
        "std_dev": None,
        "highest": max(marks),
        "lowest": min(marks)
    }

    try:
        stats["mode"] = statistics.mode(marks)
    except:
        stats["mode"] = "No unique mode"

    if len(marks) > 1:
        stats["variance"] = statistics.variance(marks)
        stats["std_dev"] = statistics.stdev(marks)

    return stats
