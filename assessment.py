"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   1. Encapsulation: Allows for the data to be close to it's functionality. 
   2. Abstraction: Hides the complexity of the methods so the users doesn't need 
   to understand the details in order to use it.  
   3. Polymorphism: Allows for the interchangeability of components. 

2. What is a class?
   Class is a type of thing. 

3. What is an instance attribute?
    A characteristic that is specific to that individual instance of a class. 

4. What is a method?
    A method is a function within a class. 

5. What is an instance in object orientation?
    An instance is a specific instance of a class. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute is a characteristic that is specific to the whole class (
    or every instance of that class). An instance attribute is a characteristic
    that is specific to that instance of the class.

    For example, in the Dog Class. An example of a class attribute is that 
    that the species of this class is set is dog since the species of 
    this class is "dog" fo all instances. 

    An instance attribute in our Dog Class can be name. For each dog, each will have 
    a different name.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """ Defined Student object.  """

    def __init__(self, first_name, last_name, address):
      """ Initialize first, last name, and address atrributes. """

      self.first_name = first_name
      self.last_name  = last_name 
      self.address = address


class Question(object):
    """ Created question class. """

    def __init__(self, question, correct_answer): 
      """ Initialize question and answer attributes. """
      
      self.question = question
      self.correct_answer = correct_answer

    def ask_and_evaluate(self, answer):
      """ Prints question to console and ask user for an answer. """

      got_answer = False

      user_answer = raw_input(self.question)

      if user_answer.lower() == self.correct_answer:
        got_answer = True
      return got_answer


class Exam(object):
    """ Created Exam class. """

    def __init__(self, name):
      """ Initialize name attribute and set questions to a list. """

      self.name = name
      self.questions = []

    def add_question(self, question, correct_answer):
      """ Method that takes question and correct_answer as a parameter. 

      Makes a Question from parameters and append to exam's list of questions. 
      """

      new_question = Question(question, correct_answer)
      self.questions.append(new_question)

    def administer(self):
      """ Method to administer the exam and return user's score. """

      score = 0
      question_num = 0
      for question in self.questions: 
        question_num += 1
        if question.ask_and_evaluate(question) == True:
          score += 1 

      return score


class Quiz(Exam):
    """ Created Quiz class that inherits from Exam Class. """ 

    def administer(self):
      """ Method to adminster quiz where pass if over half questions are correct.
      """

      # Set passed to False 
      passed_quiz = False 

      # Run parent class's adminster method to determine student's score
      student_score = super(Quiz, self).administer()

      passing_num = len(self.questions)/ 2
      if student_score  > passing_num: 
        passed_quiz = True

      return passed_quiz

# Functions 
def take_test(student, exam):
    """ Administer the exam and assign student scores. """ 

    student_score = exam.administer()
    student.score = student_score


def example_exam():
    """ Creates an example. """

    my_exam = Exam('exam')

    my_exam.add_question('What is the first letter in the alphabet?', 'a')
    my_exam.add_question('What is the first number?','1')

    sam = Student('Sam','Cool','555 California St.')

    take_test(sam, my_exam)

    return sam.score


def example_quiz():
    """ Make example quiz. """

    my_quiz = Quiz('quiz')

    my_quiz.add_question('What is the first letter in the alphabet?','a')
    my_quiz.add_question('what is the first first number?','1')

    sam = Student('Sam','Cool','555 California St.')

    take_test(sam, my_quiz)

    return sam.score

print example_exam()
print example_quiz()







