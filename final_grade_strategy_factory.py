from at_most_three_point_nine_final_grade_strategy import AtMostThreePointNineFinalGradeStrategy
from at_least_six_point_five_strategy import AtLeastSixPointFiveFinalGradeStrategy
from average_final_grade_strategy import AverageFinalGradeStrategy

class FinalGradeStrategyFactory:
  def strategy(self, grades):
    if len(filter(lambda g: g >= 6, grades)) == len(grades):
      return AtLeastSixPointFiveFinalGradeStrategy()
    elif len(filter(lambda g: g <= 2, grades)) >= 1:
      return AtMostThreePointNineFinalGradeStrategy()
    else:
      return AverageFinalGradeStrategy()