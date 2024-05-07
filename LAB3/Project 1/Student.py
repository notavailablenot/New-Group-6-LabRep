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
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        return max(self.scores)
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __ge__(self, other):
        return self.name >= other.name
 
    def __str__(self):
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    student1 = Student("Ken", 5)
    student2 = Student("Alice", 5)
    
    print("Testing equality:")
    print("Are students equal?", student1 == student2)
    
    print("\nTesting less than:")
    print("Is student1 less than student2?", student1 < student2)
    
    print("\nTesting greater than or equal to:")
    print("Is student1 greater than or equal to student2?", student1 >= student2)

if __name__ == "__main__":
    main()
