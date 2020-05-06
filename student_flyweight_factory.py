from student_flyweight import StudentFlyweight

class StudentFlyweightFactory:
  def __init__(self):
    self.student_flyweigt_map = {}

  def create_flyweight(self, assignment_grades, assignment_final_grade):
    h = hash((frozenset(assignment_grades), assignment_final_grade))
    if h not in self.student_flyweigt_map:
      self.student_flyweigt_map[h] = StudentFlyweight(assignment_grades, assignment_final_grade)

    return self.student_flyweigt_map[h]
    