from abstract_final_grade_strategy import AbstractFinalGradeStrategy

class AverageFinalGradeStrategy(AbstractFinalGradeStrategy):
  def calculate(self, grades):
    return self.average(grades)