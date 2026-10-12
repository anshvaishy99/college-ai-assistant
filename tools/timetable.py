def analyze_timetable(timetable_text: str, day: str = None):

    if not timetable_text:
        return {
            "success": False,
            "message": "Timetable data is empty."
        }

    return {
        "success": True,
        "day": day,
        "timetable": timetable_text
    }