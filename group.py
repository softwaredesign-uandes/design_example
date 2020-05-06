from gradeable import Gradeable

class Group(Gradeable):
  def __init__(self, gradeables):
    self.gradeables = gradeables
  
  def __eq__(self, other):
    if len(self.gradeables) != len(other.gradeables):
      return False
    for i in range(len(self.gradeables)):
      if not(self.gradeables[i] == other.gradeables[i]):
        return False
    return True

  def check_assignment_grades(self):
    for gradeable in self.gradeables:
      if not gradeable.check_assignment_grades():
        return False
    return True