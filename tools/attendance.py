from datetime import datetime


attendance_records = []


def mark_attendance(
    student_id: str,
    student_name: str,
    subject: str,
    date: str,
    status: str
):
    status = status.lower()

    if status not in ["present", "absent"]:
        return {
            "success": False,
            "message": "Status must be present or absent."
        }

    record = {
        "student_id": student_id,
        "student_name": student_name,
        "subject": subject,
        "date": date,
        "status": status
    }

    attendance_records.append(record)

    return {
        "success": True,
        "message": "Attendance marked successfully.",
        "record": record
    }