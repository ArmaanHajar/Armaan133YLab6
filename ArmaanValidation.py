def is_valid_int(val):
    try:
        int(val)
        return True
    except:
        return False

def input_int(prompt):
    while True:
        val = input(prompt)
        if is_valid_int(val):
            return int(val)
        print("Please type a valid input!")

def input_int_in_range(prompt, min, max):
    while True:
        val = input_int(prompt)
        if val >= min and val <= max:
            return val
        print("Number must be between", min, "and", max)

def is_valid_string(val):
    try:
        str(val)
        return True
    except:
        return False

def input_str(prompt):
    while True:
        val = input(prompt)
        if is_valid_string(val):
            return str(val)
        print("Please type a valid input!")

def y_or_n(prompt):
    while True:
        val = input_str(prompt)
        if val == "Y" or val == "y":
            return False
        elif val == "N" or val == "n":
            return True
        print("Please enter Y or N!")

def M_or_F(prompt):
    while True:
        val = input_str(prompt)
        if val == "M" or val == "m":
            return "M"
        elif val == "F" or val == "f":
            return "F"
        print("Please enter M or F!")