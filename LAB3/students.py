"""
File: student.py
Resources to manage a student's name and test scores.
"""

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
    student = Student("Lynzee", 5)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)

    Zee = Student("Zee", 4)
    for i in range(1, 5):
        student.setScore(i,100)
    print(Zee)
    
    Rei = Student("Rei", 4)
    for i in range(1, 5):
        student.setScore(i,100)
    print(Rei)
    
    print("First COMPARISON")
    print(f"Equal Comparison: {Zee == student}")
    print(f"Less Than Comparison: {Zee < student}")
    print(f"Greater Than Equal to Comparison: {Zee >= student}")

    print("SECOND COMPARISON")
    print(f"Equal Comparison: {Zee == Rei}")
    print(f"Less Than Comparison: {Zee < Rei}")
    print(f"Greater Than Equal to Comparison: {Zee >= Rei}")

if __name__ == "__main__":
    main()
