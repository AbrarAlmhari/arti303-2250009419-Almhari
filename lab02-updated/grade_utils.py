"""Helpers for converting a GPA on the 5.00 scale into a letter grade."""

def letter_grade(gpa):
    """Return the letter grade (A, B, C, D or F) for a GPA out of 5.00."""
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
