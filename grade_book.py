from publisher import Publisher

class GradeBook(Publisher):
  def __init__(self, students):
    Publisher.__init__(self)
    self.students = students
  
  def __eq__(self, other):
    if len(self.students) != len(other.students):
      return False
    for i in range(len(self.students)):
      if not(self.students[i] == other.students[i]):
        return False
    return True
  
  def check_assignment_grades(self):
    for student in self.students:
      self.notify('checking student ' + student.name)
      if not student.check_assignment_grades():
        return False
    return True