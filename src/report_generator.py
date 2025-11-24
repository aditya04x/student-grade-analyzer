import json
from utils.logger import get_logger

logger = get_logger(__name__)

def generate_report(stats, performance, output="report.json"):
    with open(output, "w") as f:
        json.dump({
            "statistics": stats,
            "performance": performance
        }, f, indent=2)

    logger.info(f"Report saved: {output}")
