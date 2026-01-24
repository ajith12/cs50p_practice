class Student:
    #init method requires that the Student class be instantiated with name and house otherwise throws error
    def __init__(self,name,house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("What's your name:")
    house = input("Where do you live?:")
    #so when instantiate the class object you have to pass name and house along here else it will throw error
    student = Student(name,house)
    return student

if __name__=="__main__":
    main()