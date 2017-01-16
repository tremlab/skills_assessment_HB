"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   ABSTRACTION - hides unnecesary complexity from those using the code. It 
                "just works"
   ENCAPSULATION - wraps up a wide range of related attributes and actions 
                    into one "thing" that can be easily referenced and imported.
   POLYMORPHISM - flexibility within structure, to allow for adaptation to minor
                    differences between various classes & objects.

2. What is a class?

Magic! A class is a blueprint that can represent as simple or complex a 
structure as needed, and all of that 'intelligence', the attribues and actions, 
can be effortlessly handed over to each new object built from it.

3. What is an instance attribute?

This is a 'variable' value that is stored specifically on an INSTANCE of a class, 
i.e. the object itself, rather than being attached at the class level.
Putting the attribute here usualy indicates that the value is expected to 
be different for each instance, not uniform across the whole class.

4. What is a method?

A function that is attached to a certain class (type) of object, and would not work
if called on a different type/class.

5. What is an instance in object orientation?

An instance is a specific object that was built from a class 'blueprint' - 
but must not be confused with the class itself. The instance will inherit most, 
perhaps all, its structure and actions from its source class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

See 3 above ^

An example would be a class attribute of "purr!" greeting for all cats,
whereas each cat object might have an instance attribute of fur_color,
which might be black, or gray, or orange, etc. for each instance of cat.


"""


class Student(object):
    """Class for students. Test scores to be stored in a list
    on the instance attribute, as tuple of (test name, score)
    since a student may take multiple different tests.
    """

    def __init__(self, first_name, last_name, street_address):
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.scores = []

    #played around with repr & str... sort of got them working,
    #but they returned AND threw an error which was weird.. :(

    # def __repr__(self):
    #     print """
    #     First: %s
    #     Last: %s
    #     Address %s
    #     """ % (self.first_name,
    #         self.last_name,
    #         self.street_address)

    #     for score in self.scores:
    #         print self.scores[0], self.scores[1]


class Question(object):
    """Class for question & answer strings.
    """

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        print self.question
        student_answer = raw_input(">")
        if student_answer == self.answer:
            return True
        else:
            return False


class Exam(object):
    """Class for exams. question objects are stored in a list on each
    instance of exam.
    """

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, answer):
        e_question = Question(question, answer)
        self.questions.append(e_question)

    def administer(self):

        correct_scores = 0
        final_grade = 0

        for question in self.questions:
            answer_score = question.ask_and_evaluate()

            if answer_score:
                correct_scores += 1

        #oh python and your silly math... 2/3 = 0.0???
        #mulitply by 100 FIRST to retain any value
        final_grade = (correct_scores * 100) / len(self.questions)

        return final_grade

    # def __str__(self):

    #     printout = "Name: " + self.name

    #     if len(self.questions) > 0:
    #         for question in self.questions:
    #             printout = printout + "Question: " + self.question[0]
    #             printput = printout + "Correct answer: " + self.question[1]
    #     else:
    #         printout = prinout + "No questions found."

    #     return printout


class Quiz(Exam):
    """Subclass for quizzes. administer() returns only pass/fail
    (as True/False) instead of raw score like exam.administer()
    """
    def administer(self):
        final_grade = super(Quiz, self).administer()

        if final_grade >= 50:
            return True
        else:
            return False


def take_test(test, student):
    """function to administer either exam or quiz to a specifc
    instance of Student. Asks all questions on the test,
    counts correct answers, and both prints score and appends score
    to student instance attribute list.
    """
    print "\n%s, please complete the following questions for your %s test:\n" % (
        student.first_name, test.name)
    score = test.administer()

    #stores test name and score tuple on student instance list.
    student.scores.append((test.name, score))

    #careful! score of "66" also 'is True', hence explicit equivalence here
    if score == True:  # fie upon you, yellow flag! correct syntax!
        score = "PASS"
    if score is False:
        score = "FAIL"
    else:
        score = str(score)

    print "\n\n%s, %s --- scored %s on %s\n\n" % (
        student.last_name,
        student.first_name,
        score,
        test.name
        )

############################

# # play in the sandbox!!!!!!!!

# student1 = Student("Renee", "Balmert", "123 Main St")
# student2 = Student("Albert", "Einstein", "456 Broad St.")

# midterm = Exam("Midterm")
# final = Exam("Final")
# week3 = Quiz("Week3")

# midterm.add_question("Who is the best vampire slayer?", "Buffy")
# midterm.add_question("How many robot lions to make a Voltron?", "5")
# midterm.add_question("Who's going to win the SuperBowl?", "Steelers!")

# week3.add_question("Best desert OF ALL TIME???", "ice cream")
# week3.add_question("Cutest animal?", "baby sloth")
# week3.add_question("What is your quest?", "to seek the holy grail")

# take_test(midterm, student1)
# take_test(week3, student1)
# take_test(midterm, student2)
# take_test(week3, student2)


# def print_scores(student):
#     """ DRY :D print results"""
#     print "\n\n"
#     print student.first_name
#     print "\nscores:"

#     for score in student.scores:
#         print score[0] + ": " + str(score[1])


# print_scores(student1)
# print_scores(student2)
