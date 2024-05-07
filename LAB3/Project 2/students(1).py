"""
File: student(1).py
Resources to manage a student's name and test scores.
"""
import random
class Student(object):

    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        return self.name
  
    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]
   
    def getAverage(self):
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        return max(self.scores)
 
    def __str__(self):
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    def __eq__(self, other):
        return self.name == other.name
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __ge__(self, other):
        return self.name >= other.name

def main():
    listofstudents = []
    student = Student("Aadi", 5)
    for i in range(1, 6):
        student.setScore(i, 100)
    listofstudents.append(student)

    Zee = Student("Zee", 4)
    for i in range(1, 5):
        Zee.setScore(i,100)
    listofstudents.append(Zee)
    
    Rei = Student("Rei", 4)
    for i in range(1, 5):
        Rei.setScore(i,100)
    listofstudents.append(Rei)
        
    Joson = Student("Joson", 3)
    for i in range(1, 4):
        Joson.setScore(i,100)
    listofstudents.append(Joson)

    random.shuffle(listofstudents)
    print("shuffled", end="->")
    for student in listofstudents:
        print (student.getName(), end =" ")

    listofstudents.sort()
    print()
    print ("Sorted" , end="->")
    for student in listofstudents:
        print (student.getName(), end = " ")
    print()
    print("Printing students")
    for persons in listofstudents:
        print(persons)


if __name__ == "__main__":
    main()


