import csv

def check_grades():
  with open("grades.csv", 'r') as grades_file:
    reader = csv.reader(grades_file, delimiter=',')
    file_lines = list(reader)
    
    for line in file_lines[1:]:
      student = line[0]
      file_average = int(line[-1])

      grades = map(int, line[1:-1])
      calculated_average = sum(grades) / len(grades) 

      if file_average != calculated_average:
        return False 


  return True


print check_grades()
