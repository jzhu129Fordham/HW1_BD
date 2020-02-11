# Python Project
# Group member: Kefan Zha, kzha@fordham.edu
#               Chongdi Fu, cfu13@fordham.edu
#               Yanqi Shi ,yshi133@fordham.edu
#               Jing Zhu, jzhu129@fordham.edu
# ===========================================================================


# Import packages

import pandas as pd


# ===========================================================================
# Function definition
# Function 1: call help list
def help_list():
    print('Help List: \n'
          'Query 0: Call help list \n'
          'Query 1: Display all data \n'
          'Query 2: Search students with last name starting with certain string \n'
          'Query 3: Search students graduating on a certain year \n'
          'Query 4: Get a summary of students graduating on/after a certain year \n'
          'Query 5: Search students in a certain program \n'
          'Query q: Quit the system')


# Function 2: quit the system
def quit_sys():
    print('Thank you for using the Student Query Tool!')


# Function 3: formatted print
def formatted(print_list, field_name):
    res = pd.DataFrame(print_list)
    res.columns = field_name
    print(res)


# Function 4: display all student records
def all_display(data):
    formatted(data, head)


# Function 5: display students whose last name begins with a certain string (case insensitive)
def name_search(data, char):
    res = []
    found = False
    for i in range(len(data)):
        try:
            start_char = data[i][1].index(char.capitalize())
        except ValueError:
            continue
        else:
            if start_char == 0:
                res.append(data[i])
                found = True
    if not found:
        print('No data found.')
    else:
        formatted(res, head)


# Function 6: display all records for students whose graduating year is a certain year
def year_search(data, year):
    res = []
    found = False
    for i in range(len(data)):
        if str(data[i][3]) == year:
            res.append(data[i])
            found = True
    if not found:
        print('No data found.')
    else:
        formatted(res, head)


# Function 7: display a summary report of number and percent of students in each program,
#             for students graduating on/after a certain year
def get_report(data, method, year):
    new_data = []
    if method == 'on':
        for k in range(len(data)):
            if str(data[k][3]) == year:
                new_data.append(data[k])
    elif method == 'after':
        for k in range(len(data)):
            if str(data[k][3]) >= year:
                new_data.append(data[k])
    program = []
    count = []
    percent = []
    found = False
    for i in range(len(new_data)):
        if new_data[i][5] not in program:
            program.append(new_data[i][5])
            count.append(0)
        for j in range(len(program)):
            if new_data[i][5] == program[j]:
                count[j] += 1
                found = True
    for i in range(len(count)):
        percent.append(str(round(count[i] / len(new_data) * 100, 2)) + '%')
    if not found:
        print('No data found.')
    else:
        print(f'Report for students graduating {method} {year}:')
        formatted([count, percent], program)


# Function 8: display all records for students in a certain program
def program_search(data, program):
    res = []
    found = False
    for i in range(len(data)):
        if str(data[i][5]) == program.upper():
            res.append(data[i])
            found = True
    if not found:
        print('No data found.')
    else:
        formatted(res, head)


# Function 9: load data
def data_load():
    read = False
    while not read:
        try:
            path = input('Please input the path of the data file: ')
            student_in = pd.read_csv(path, sep="\t")
        except FileNotFoundError:
            print('File not found. Please check the path.')
            continue
        else:
            read = True
    return student_in


# ===========================================================================
# Data Prepare

# Load data
print('Welcome to the Student Query Tool!')
student = data_load()
print('Data has been loaded!')

# Store the data frame into a list
head = []
for i in range(6):
    head.append(student.columns[i])
student_table = []
for i in range(len(student)):
    row = []
    for j in range(6):
        row.append(student.iloc[i, j])
    student_table.append(row)
# Set maximum display
pd.options.display.max_rows = 100


# ===========================================================================
# System run

print('Please check the help list to choose the query:')
help_list()
input('Press Enter to continue.')
print()
query = input('Please select the query number. (Enter 0 to call help list)')
while query != 'q':
    if_query = True
    if query == '0':
        help_list()
        if_query = False
    elif query == '1':
        all_display(student_table)
    elif query == '2':
        char = input("Please input the student's last name (You can only input the first few letters): ")
        name_search(student_table, char)
    elif query == '3':
        grad_year = input('Please input the graduation year: ')
        year_search(student_table, grad_year)
    elif query == '4':
        method = input('Please input the method (You can use on/after): ')
        while method != 'on' and method != 'after':
            method = input('Please input a valid method (You can use on/after): ')
        grad_year = input('Please input the graduation year: ')
        get_report(student_table, method, grad_year)
    elif query =='5':
        prog = input('Please input the program: ')
        program_search(student_table, prog)
    else:
        print('Invalid query number.')
        if_query = False
    if if_query:
        input('Query finished! Press Enter to continue.')
        print()
    else:
        input('Press Enter to continue.')
        print()
    query = input('Please select the query number. (Enter 0 to call help list)')
quit_sys()
