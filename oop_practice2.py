class Student:
    #init method requires that the Student class be instantiated with name and house otherwise throws error
    def __init__(self,name,house):
        self.name = name
        self.house = house

    #Getter for house
    @property
    def house(self):
        return self._house
    
    #Setter for house
    @house.setter
    def house(self,house):
        if not house:
            raise ValueError("Invalid house")
        self._house = house

    #Getter for name
    @property
    def name(self):
        return self._name
    
    #Setter for name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @classmethod
    def get(cls):
        name = input("What is your name: ")
        house = input("Where is your house: ")
        return cls(name,house)

    def team(self):
        if self.name == "David Beckham":
            return "Manchester United"
        elif self.name == "Ronaldo":
            return "Real Madrid"
        else:
            return "None"

def main():
    #student = get_student()
    student = Student.get()
    print(f"{student.name} from {student.house} and their team is {student.team()}")

#def get_student():
 #   name = input("What's your name:")
  #  house = input("Where do you live?:")
    #so when instantiate the class object you have to pass name and house along here else it will throw error
  #  return Student(name,house)

if __name__=="__main__":
    main()