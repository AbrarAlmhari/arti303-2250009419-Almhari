class Student:
    """A single student record."""

    def __init__(self, name, age, gpa, is_enrolled=True):
        if not 0.0 <= gpa <= 4.0:
         raise ValueError("GPA must be between 0.0 and 4.0") 
        self.name = name
        self.age = age
        self.gpa = gpa
        self.is_enrolled = is_enrolled

    def is_dean_list(self):
        """Return True if this student's GPA qualifies for the Dean's list."""
        return self.gpa >= 3.5

    def report_line(self):
        """Return a one-line, human-readable summary of this student."""
        status = "made the Dean's list" if self.is_dean_list() else "did not make the Dean's list"
        enrollment = "is enrolled" if self.is_enrolled else "is not enrolled"
        return f"{self.name} (age {self.age}, GPA {self.gpa:.2f}) {enrollment} and {status}."

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age}, gpa={self.gpa})"
    
def average_gpa(students):
    if len(students) == 0:
        return 0.0

    total = sum(student.gpa for student in students)
    return float(total / len(students))
def dean_list_students(students):
    return [student for student in students if student.is_dean_list()]
def letter_grade(gpa):
    if gpa >= 3.7:
        return "A"
    elif gpa >= 2.7:
        return "B"
    elif gpa >= 1.7:
        return "C"
    elif gpa >= 1.0:
        return "D"
    else:
        return "F"
def oldest_student(students):
    if not students:
        return None
    oldest = students[0]
    for s in students:
        if s.age > oldest.age:
            oldest = s
    return oldest
def group_by_enrollment(students):
    enrolled = []
    not_enrolled = []

    for student in students:
        if student.is_enrolled:
            enrolled.append(student)
        else:
            not_enrolled.append(student)

    return enrolled, not_enrolled
def student_risk_report(students):
    """Categorize students based on their GPA and enrollment status."""
    report = {
        "excellent": [],
        "doing_well": [],
        "needs_improvement": [],
        "at_risk": []
    }

    for student in students:
        if not student.is_enrolled:
            report["at_risk"].append(student)
        elif student.gpa >= 3.5:
            report["excellent"].append(student)
        elif student.gpa >= 2.7:
            report["doing_well"].append(student)
        else:
            report["needs_improvement"].append(student)

    return report