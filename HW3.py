﻿# Your name: Priya Varshika Ganji
# Your student id: 28394873
# Your email: pganji@umich.edu
# List who you have worked with on this homework: Priya Ganji (by myself)


# import the random module for use in this program

import random

# Create the class Fortune_Teller
    # create the constructor (__init__) method
    # it takes as input: a list of possible answers
    # it sets this object's fortunes_list (instance variable) to the passed list of possible answers
    # it sets this object's questions_list (instance variable) to an empty list
    # it sets this object's fortunes_history_list (instance variable) to an empty list

class Fortune_Teller:

    def __init__(self, fortunes_list):
        self.fortunes_list = fortunes_list
        self.questions_list = []
        self.fortunes_history_list = []

    
    # create the __str__ method
    # It should return a string with all the fortunes
    # in fortunes_list separated by commas
    # For example : "Yes, No, Not clear"

    def __str__(self):
        list = ','.join(self.fortunes_list)
        return list

# need to finish !!!!

    # create the get_fortune method
    # it randomly picks an index from 0 to the number of items in the fortunes_list minus one
    # it adds that index to the end of the fortunes_history_list
    # it returns the answer at the picked index

    def get_fortune(self):

        num = random.randint(0, len(self.fortunes_list) - 1)
        self.fortunes_history_list.append(num)
        return self.fortunes_list[num]

    # create the question_check method that takes a question
    # it checks if the question is in the questions_list and if so returns
    #         "I've already answered that question”
    # Otherwise it adds the question to the questions_list and
    # returns the fortune from get_fortune

    def question_check(self, question):

        if (question in self.questions_list):
            return "I've already answered that question"

        else:
            self.questions_list.append(question)
            response = self.get_fortune()
            return response


    # create the print_questions_history method
    # prints "[answer index] question - answer" for each of the indices in the fortunes_history_list
    # from the first to the last with each on a separate line.  If there are no items in the
    # fortunes_history_list it prints "None yet"
    # it does not return anything!

    def print_questions_history(self):

        if self.fortunes_history_list == []:

            print ("None yet")

        else: 

            for i in range(len(self.fortunes_history_list)):
                print("[" + str(self.fortunes_history_list[i]) + ']' + self.questions_list[i] + " - " + self.fortunes_list[self.fortunes_history_list[i]])

        return

    # EXTRA POINTS
    # create the most_frequent method
    # it takes as input:
    #   a number, n. Ex: 200
    # it generates a random response n times by calling get_fortune
    # It prints the counts for each answer and
    # prints the most frequently occurring answer (Do not use a dictionary in this solution):
    #   Yes: 36
    #   No: 36
    #   Ask again: 48
    #   Maybe: 38
    #   Not clear: 47
    #   The most frequent answer after 200 was Not clear

def main():

    # You are welcome to replace the answer_list with your desired answers
    fortunes_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Fortune_Teller(fortunes_list)

    # get the first question or quit
    # Q for question
    Q = ("Ask a question or type quit: ")
    Que = input(Q)

    # loop while question is not "quit"

    while Que != "quit":

        Ans = bot.question_check(Que)
        print(Que + " - " + Ans)
        Q = ("Ask a question or type quit: ")
        Que = input(Q)
        
    return

        # get an answer from question_check

        # print question - answer

        # get the next question or quit 
   

def test():

    fortunes_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]

    print()
    print("Testing Fortune Teller:")
    bot2 = Fortune_Teller(fortunes_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no answers have been generated yet")
    bot2.print_questions_history()
    print()

    print("Asking the Question: Will I pass this semester?")
    print(bot2.question_check("Will I pass this semester?"))
    print()

    print("Asking the Question: Should I study today?")
    print(bot2.question_check("Should I study today?"))
    print()

    print("Asking the Question: Should I study today? (again)")
    print(bot2.question_check("Should I study today?"))
    print()

    print("Asking the Question: Is SI 206 the best class ever?")
    print(bot2.question_check("Is SI 206 the best class ever?"))
    print()

    print("Printing the history")
    bot2.print_questions_history()
    print()

    #EXTRA POINTS
    #Uncomment the lines below if you attempt the extra credit!
    # print("Testing most_common method with 200 responses")
    # bot2.most_common(200)


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test() 
    # TODO: Uncomment when you are ready to test your Fortune_Teller class