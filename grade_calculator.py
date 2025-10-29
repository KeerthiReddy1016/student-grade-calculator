def calculate_grade(marks):
  if marks >= 90:
    grade = "A"
    message = "Excellent work!"
  elif marks >= 80:
    grade = "B"
    message = "Great job! keep it up!"
  elif marks >= 70:
    grade = "C"
    message = "Good effort, aim higher!"
  elif marks >= 60:
    grade = "D"
    message = "You passed, but can improve!"
  else:
    grade = "F"
    message = "Don't give up, keep trying!"
  return grade, message

marks = float(input("Enter your marks(0-100): "))
grade, message = calculate_grade(marks)
print(f"Your Grade: {grade}")
print(message)