from datetime import date
from datetime import datetime
import inflect
import sys

class Dob:
    def __init__(self,dob):
        try:
            dob = datetime.strptime(dob,"%Y-%m-%d")
        except ValueError:
            print("Invalid date")
            sys.exit()
        self.dob = dob

p = inflect.engine()

def main():
    calc_dob = get_dob()
    current = datetime.strptime('2000-01-01',"%Y-%m-%d")#datetime.today().date()
    time_diff = current - calc_dob.dob
    print(p.number_to_words(int(time_diff.total_seconds() // 60), andword="").capitalize()+" minutes")

def get_dob():
    dob = input("Date of birth: ")
    return Dob(dob)
    

if __name__ == "__main__":
    main()
