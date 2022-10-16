# Initialises the os.path module that gives access to your system's files directories
from _csv import writer, reader


def file_check(x):
    import os.path
    from csv import writer  # >>>>> allows for the creation of a CSV file
    # Excel file and recording the header

    if os.path.exists(x) is False:
        my_file = open(x, 'w', newline="\n", )
        my_pen = writer(my_file)
        my_header = ["Date", "Serial No", "First Name", "Surname", "Town", "Age", "Class Group", "Birthday(Day, Month)"]
        my_pen.writerow(my_header)
        my_file.close()
        print("The file has been created with header successfully")
    else:
        print("File exists, proceed to the records menu")
    return x


def record_count(input_file):
    """This function track the number of rows in the input_file"""
    row_count = -1  # Excluding the header
    for rows in open(input_file):
        row_count = row_count + 1
    return row_count


# Calculates the age and returns the birthdate in the specified format
def calc_age(birthdate):
    """This function calculates the user's age and returns its value,today's date,day of birth and month of birth"""
    import datetime
    date = datetime.date.today().strftime("%d-%m-%Y")  # >>>> Changes the format of the datetime method
    today = datetime.datetime.now()
    birthday = datetime.datetime.strptime(birthdate, "%m-%d-%Y")  # >>>> converts a string to datetime method
    age1 = (today - birthday) / 365
    age = int(age1.days)
    if age < 0:  # >>>>>>>raises an error because the value of age cannot be 0!
        raise ValueError
    full_month = birthday.strftime("%d, %B")  # >>>> changes the format of the datetime to day and month is full
    return age, full_month, date


# Groups the records in classes using their ages
def class_age(age):
    """This function classifies the users to groups according to their ages"""
    if age < 9:
        my_class = "Invalid"
    elif 9 <= age <= 15:
        my_class = "Favour"
    elif 16 <= age <= 70:
        my_class = "Knowledge"
    else:
        my_class = "Invalid"
    return my_class


# Accepts inputs of the user's details
def user_details():
    """This function receives the user's details and returns the values"""
    first_name = input("What is your first name?\n ")
    first_name = first_name.strip().title()  # >>>>> this removes spaces from the beginning and end of the input and
    # also changes it to title format
    last_name = input("\n What is your last name?\n ")
    last_name = last_name.strip().title()
    user_town = input("\nWhat town do you reside in?\n ")
    user_town = user_town.strip().title()
    d = input("\n Input your birthday in the format MM-DD-YYYY\n ")
    try:
        my_age, monthday, my_date = calc_age(
            d)  # Calls the function that calculates the age and returns the age, birthdate and today's date
        my_class = class_age(my_age)  # >>>>>> Calls the function that groups the user according to age.
    except ValueError:
        print(" Invalid input! Try again")
        d = input("\n Input your birthday in the format MM-DD-YYYY\n  ")
        try:
            my_age, monthday, my_date = calc_age(d)
            my_class = class_age(my_age)
        except ValueError:
            print("Another invalid input!")
            import datetime
            my_date = datetime.date.today().strftime("%d-%m-%Y")
            my_age, monthday, my_class = "Invalid", "Invalid", "Invalid"

    return first_name, last_name, user_town, my_age, monthday, my_date, my_class


# Reading the records in the CSV file created

def read_file(file_name):
    my_file = open(file_name, 'r', newline="\n")
    my_text = my_file.read()
    print(my_text)
    my_file.close()
    row_count = record_count(file_name)
    print(f"The file contains {row_count} records")


# Updating or adding records to the CSV file, 'a' is for append, which means 'to add'
def add_to_file(file_name):
    my_file = open(file_name, 'a', newline="\n")

    # >>>> This enables the user to add records to the code and the newline removes
    # unnecessary spaces
    my_pen = writer(my_file)
    row_count = record_count(file_name)

    first_n, last_n, my_town, student_age, birth, days_date, group = user_details()
    serial_no = row_count + 1
    records = [days_date, serial_no, first_n, last_n, my_town, student_age, group, birth]
    my_pen.writerow(records)
    my_file.close()
    print("...............................................................................")
    print(f" Student record {serial_no} has been successfully added to the file")


# Reading the records in the CSV file and printing it in an ordered format
def print_records(file_name):
    my_file = open(file_name, "r", newline='\n')
    row_count = record_count(file_name)
    my_reader = reader(my_file)
    for every_row in my_reader:
        for every_data in every_row:
            print("{0:<15}".format(every_data), end="\t")
        print()

    print()
    print(f"\n\nThe file contains {row_count} records")
    my_file.close()


def records_project():
    global file_test
    import os.path
    query = input("Hello there! Do you want to create or edit a file? \n'C' is for create,\n'E' is for edit.\n ")
    query = query.strip().upper()
    if query == "C":
        q = input("\nInput the name of file you want to create!\n ")
        q = q.strip().title()
        file_test = f"{q}" + ".csv"
    elif query == "E":
        p = input("\n What is the name of the file?\n ")
        p = p.strip().title()
        m = f"{p}" + ".csv"
        z = os.path.exists(m)
        if z:
            file_test = m
        else:
            print("\n The file does not exists! Please input existing file!\n ")
    file_name = file_check(file_test)
    a = input(" \nPress 'M' for the records menu\n ")
    a = a.strip().lower()
    if a == "m":
        b = input(
            "\n Welcome to CHM Records Database! \n A is for ADD\n \nR is for READ\n \nP is for PRINT\n \n Please "
            "select an action!")
        b = b.strip().lower()
        if b == "a":
            add_to_file(file_name)
            read_file(file_name)
        elif b == "r":
            read_file(file_name)
        elif b == "p":
            print_records(file_name)
        else:
            print("\nYou have selected a wrong action! Please try again later!\n ")
    else:
        print("\n You have chosen an invalid option! Please select 'M' for the records menu\n")

    while True:
        c = input("\n Do you want to take another action? Y/N? ")
        c = c.strip().lower()
        if c == "y":
            b = input("\n A is for ADD\n \nR is for READ\n \nP is for PRINT\n \n Please select an action!\n ")
            b = b.strip().lower()
            if b == "a":
                add_to_file(file_name)
                read_file(file_name)
            elif b == "r":
                read_file(file_name)
            elif b == "p":
                print_records(file_name)
            else:
                print("\nYou have selected a wrong action! Please try again later!\n ")
        else:
            print("\n Thank you for your time! ")
            break


records_project()
