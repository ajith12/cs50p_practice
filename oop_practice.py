class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("What's your name:")
    house = input("Where do you live?:")
    student = Student(name,house)
    return student

if __name__=="__main__":
    main()