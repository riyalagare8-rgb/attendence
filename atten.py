import sys
def calculate_attendance(classes_held, classes_attended):
    return (classes_attended / classes_held) * 100


if __name__ == "__main__":
    print("Attendance Eligibility Checker")

    # CLI requires arguments
    if len(sys.argv) != 3:
        print("Error: Please provide classes held and classes attended")
        print("Usage: python attendance.py <classes_held> <classes_attended>")
        sys.exit(1)

    try:
        classes_held = float(sys.argv[1])
        classes_attended = float(sys.argv[2])

        attendance_percentage = calculate_attendance(classes_held, classes_attended)
        print(f"Attendance Percentage: {attendance_percentage}")

        if attendance_percentage >= 75:
            print("Eligible")
        else:
            print("Not Eligible")

    except ValueError:
        print("Error: Inputs must be numbers")
        sys.exit(1)
