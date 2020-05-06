from student_flyweight_factory import StudentFlyweightFactory

class Student:
  def __init__(self, assignment_grades, assignment_final_grade, name):
    self.flyweight = StudentFlyweightFactory().create_flyweight(assignment_grades, assignment_final_grade)
    self.name = name
  
  def __eq__(self, other):
    if self.name != other.name:
      return False 
    if self.flyweight.assignment_final_grade != other.flyweight.assignment_final_grade:
      return False
    if len(self.flyweight.assignment_grades) != len(other.flyweight.assignment_grades):
      return False
    for i in range(len(self.flyweight.assignment_grades)):
      if self.flyweight.assignment_grades[i] != other.flyweight.assignment_grades[i]:
        return False
    return True
  
  def check_assignment_grades(self):
    def is_close(a, b, rel_tol=1e-09, abs_tol=0.0):
      return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
    calculated_average = sum(self.flyweight.assignment_grades) / len(self.flyweight.assignment_grades) 

    return is_close(self.flyweight.assignment_final_grade, calculated_average) 