class Student:
  def __init__(self, assignment_grades, assignment_final_grade, name):
    self.assignment_grades = assignment_grades
    self.assignment_final_grade = assignment_final_grade
    self.name = name
  
  def __eq__(self, other):
    if self.name != other.name:
      return False 
    if self.assignment_final_grade != other.assignment_final_grade:
      return False
    if len(self.assignment_grades) != len(other.assignment_grades):
      return False
    for i in range(len(self.assignment_grades)):
      if self.assignment_grades[i] != other.assignment_grades[i]:
        return False
    return True
  
  def check_assignment_grades(self):
    def is_close(a, b, rel_tol=1e-09, abs_tol=0.0):
      return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
    calculated_average = sum(self.assignment_grades) / len(self.assignment_grades) 

    return is_close(self.assignment_final_grade, calculated_average) 