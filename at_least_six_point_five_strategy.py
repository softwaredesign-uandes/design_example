from abstract_final_grade_strategy import AbstractFinalGradeStrategy

class AtLeastSixPointFiveFinalGradeStrategy(AbstractFinalGradeStrategy):
  def calculate(self, grades):
    return max([self.average(grades), 6.5])