from ArmaanValidation import input_int_in_range, M_or_F
from Name import Name
from time import sleep

def welcome():
    print("Welcome to my program!")
    sleep(.75)
    print("This program will show you the top 50 most popular names from the year and gender of your choice")
    sleep(.75)

def get_inputs():
    gender = M_or_F("What gender? (Choose M or F): ")
    year = input_int_in_range("What year (Between 1915 - 2014): ", 1915, 2014)
    names = Name.fetch_names(year, gender)
    print(F"{'Name Count':^20} {'Name':^20} {'Year':^20} {'Gender':^20}")
    for name in names:
        print(F"{name.get_name_count():^20} {name.get_name():^20} {name.get_year():^20} {name.get_gender():^20}")

def main():
    welcome()
    get_inputs()

if __name__ == "__main__":
    main()