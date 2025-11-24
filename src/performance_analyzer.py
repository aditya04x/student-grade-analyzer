def analyze_performance(marks, pass_mark=40):
    if not marks:
        return None

    total = len(marks)
    passed = len([m for m in marks if m >= pass_mark])
    failed = total - passed

    return {
        "total_students": total,
        "passed": passed,
        "failed": failed,
        "pass_percentage": (passed / total) * 100,
        "top_performers": sorted(marks, reverse=True)[:3],
        "weak_students": sorted(marks)[:3]
    }
