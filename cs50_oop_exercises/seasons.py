from datetime import date
from datetime import datetime
import inflect
import sys

p = inflect.engine()

def main():
    dob = get_dob()
    current = datetime.strptime('2000-01-01',"%Y-%m-%d")#datetime.today().date()
    time_diff = current - dob
    print(p.number_to_words(int(time_diff.total_seconds() // 60), andword="").capitalize()+" minutes")

def get_dob():
    dob = input("Date of birth: ")
    try:
        dob = datetime.strptime(dob,"%Y-%m-%d")
    except ValueError:
        sys.exit()
    return dob
    

if __name__ == "__main__":
    main()
