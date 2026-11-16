class InvalidGradeError(Exception):
    pass


def validate_grade(value):
    try:
        grade = float(value)

    except ValueError:
        raise InvalidGradeError("Grade must be a numeric value.")

    if grade < 0 or grade > 100:
        raise InvalidGradeError("Grade must be between 0 and 100.")

    return grade


def main():
    test_values = ["85", "abc", "-10", "120"]

    for value in test_values:
        try:
            grade = validate_grade(value)
            print("Valid grade:", grade)

        except InvalidGradeError as e:
            print("Invalid grade:", e)


main()