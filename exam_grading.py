def exam_grade(score):
    if score > 100:
        grade = None
    elif score > 90:
        grade = "A"
    elif score >= 85:
        grade = "B"
    elif score >= 75:
        grade = "C"
    elif score >= 0:
        grade = "D"
    else:
        grade = None
    return grade
    
print(exam_grade(101))  # Should be None
print(exam_grade(95))  # Should be A
print(exam_grade(85))  # Should be B
print(exam_grade(75))  # Should be C
print(exam_grade(65))  # Should be D
print(exam_grade(55))  # Should be D
print(exam_grade(-1))  # Should be None
