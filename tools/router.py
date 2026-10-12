from tools.calculator import calculate
from tools.attendance import mark_attendance
from tools.timetable import analyze_timetable


def run_tool(tool_name, data):

    if tool_name == "calculator":

        return calculate(
            data["expression"]
        )

    elif tool_name == "attendance":

        return mark_attendance(
            student_id=data["student_id"],
            student_name=data["student_name"],
            subject=data["subject"],
            date=data["date"],
            status=data["status"]
        )

    elif tool_name == "timetable":

        return analyze_timetable(
            timetable_text=data["timetable"],
            day=data.get("day")
        )

    return {
        "success": False,
        "message": "Unknown tool."
    }