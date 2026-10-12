def calculate_attendance(attended: int, total: int):
    if total <= 0:
        return {
            "success": False,
            "message": "Total classes must be greater than 0."
        }

    percentage = (attended / total) * 100

    return {
        "success": True,
        "attended": attended,
        "total": total,
        "percentage": round(percentage, 2)
    }


def calculate(expression: str):
    """
    Basic calculator.
    Example:
    calculate("25 + 10")
    """

    try:
        allowed = "0123456789+-*/(). %"

        if not all(char in allowed for char in expression):
            return {
                "success": False,
                "message": "Invalid mathematical expression."
            }

        result = eval(expression, {"__builtins__": {}}, {})

        return {
            "success": True,
            "expression": expression,
            "result": result
        }

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }