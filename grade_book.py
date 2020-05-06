from group import Group

class GradeBook:
  def __init__(self, students):
    self.classroom = Group(students)
  
  def __eq__(self, other):
    return self.classroom == other.classroom
  
  def check_assignment_grades(self):
    return self.classroom.check_assignment_grades()