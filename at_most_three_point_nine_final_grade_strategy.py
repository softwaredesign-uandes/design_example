from abstract_final_grade_strategy import AbstractFinalGradeStrategy

class AtMostThreePointNineFinalGradeStrategy(AbstractFinalGradeStrategy):
  def calculate(self, grades):
    return min([self.average(grades), 3.9])