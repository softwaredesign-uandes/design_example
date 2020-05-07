from load_grade_book import load_gradebook_from_file
from subscriber import Subscriber

class App(Subscriber):
  def run(self):
    grade_book = load_gradebook_from_file('grades.csv')
    grade_book.add_subscriber(self)
    print grade_book.check_assignment_grades()

  def handle(self, event):
    print event

App().run()