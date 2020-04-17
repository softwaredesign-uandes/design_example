from load_grade_book import load_gradebook_from_file

grade_book = load_gradebook_from_file('grades.csv')
print grade_book.check_assignment_grades()