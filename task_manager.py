

# Import modules
import textwrap
from datetime import datetime

# Global variables
user_pass_dict = {}
task_list_all = []
username = ""


# Create function to read user_TEST.txt and return a dictionary
def read_user_file():
    with open("user_TEST.txt", "r") as f:
        user_pass_dict = {}
        for line in f:

            # Splitting the line using multiple assignment of variables and making
            # sure there are no trailing whitespaces
            username, password = line.strip().split(", ")

            # Add key-value pair to dictionary
            user_pass_dict[username] = password
    return user_pass_dict



# Create function to read tasks_TEST.txt and return a list of lists
def read_task_file():
        with open("tasks_TEST.txt", "r") as f:
            
            task_list_all = []
            for line in f:

                # Splitting the line using multiple assignment of variables
                (task_username, task_title, task_description, current_date,
                due_date, task_status) = line.strip().split(", ")

                # Save details of each task as list in the list task_list_all
                task_list_all.append([task_username, task_title, 
                task_description, current_date, due_date, task_status])
        return task_list_all


# Create function to display menu for admin
def display_admin_menu():

        # Ask for choice and make menu input case insensitive
        menu = input('''Please select one of the following options:
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    gr - generate reports
    ds - display statistics
    e - Exit
    : ''').lower()
        print()
        return menu



# Create function to display menu for regular user
def display_user_menu():

        # Ask for choice and make menu input case insensitive
        menu = input('''Please select one of the following options:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()
        print()
        return menu



# Create reg_user function
def reg_user():
    
        if username == "admin":
            
            # Ask the user to enter a new username and make it case insensitive
            new_username = input("Enter a new username: ")
            new_username = new_username.lower()

            # Check if new entry already exist
            if new_username not in user_pass_dict:

                # Ask the user to enter a new password and confirm it      
                new_password = input("Enter a new password: ")
                confirm_password = input("Confirm the password: ")

                # Check if new password and confirm password match
                if new_password == confirm_password:

                    # Add new username and password to dictionary
                    user_pass_dict[new_username] = new_password

                    # Add new username in lower case and password to user_TEST.txt
                    with open("user_TEST.txt", "a") as f:
                        f.write("\n" + f"{new_username}, {new_password}")
                        print("New username and password registered!" + "\n")
                else:
                    print("Passwords do not match. Please try again." + "\n")
            
            # If new user name is already taken, print message 
            else:
                print("Username already in use. Please, try again.\n")

        # If user enters "r" by mistake, decline action
        else:
            print("Invalid entry. Please, try again.\n")



# Create add_task function
def add_task():

    while True:

        # Check if user is a registered user
        assign_user = input("Assign username to new task: ")

        # Make user name case insensitive
        assign_user = assign_user.lower()

        # Ask for task details and make user name case insensitive
        if assign_user in user_pass_dict:
            task_title = input("Enter a title for the new task: ")
            task_description = input("Enter a short description for the "+
            "new task: ")

            # Get the current date using datetime module
            current_date = datetime.now()

            while True:

                # Parse input to valid datetime object in correct format or raise exception
                try:
                    due_date_input = input("Enter the due date for the "+
                    "new task (dd Mon yyyy): ")
                    due_date = datetime.strptime(due_date_input, "%d %b %Y")

                    # Check if due date is in the past and handle error
                    if due_date < current_date:
                        raise ValueError("Error: The entered date is in "+
                        "the past")

                    else:
                        break

                # Checking for ValueError    
                except ValueError as e:
                    print(e)
                    print("Please enter the date again in the format "+
                    "(dd Mon yyyy)")

                # Checking for any other general errors with modules etc
                except Exception as e:
                    print(f"Error: {e}")
                    print("Please enter the date again in the format "+
                    "(dd Mon yyyy)")

            break

        else:    
            print("Error: Invalid username.")
            print("Please enter a valid username or register as a new user")
            print()

    # Format the current_date and due_date as strings
    current_date_str = current_date.strftime("%d %b %Y")
    due_date_str = due_date.strftime("%d %b %Y")

    # Add the data and user name in lower case to the task.txt file 
    with open("tasks_TEST.txt", "a") as f:
        f.write(
            "\n" + f"{assign_user}, {task_title}, {task_description}, "
            f"{current_date_str}, {due_date_str}, No"
        )
    print("New task registered!")



# Create view_all_tasks function
def view_all_tasks():

    # Call read_task_file() to get the latest data from the file
    read_task_file()
    
    # Print out details for each task
    for pos, task in enumerate(task_list_all, start = 1):
        pos_str = str(pos)
        pos_title = "Task number " + pos_str

        # Output task details in a table format
        print(pos_title.center(60, "\u2500") + "\n")
        print(f"{'Task:':<20}{task[1]}")
        print(f"{'Assigned to:':<20}{task[0]}")
        print(f"{'Date assigned:':<20}{task[3]}")
        print(f"{'Due date:':<20}{task[4]}")
        print(f"{'Task Complete?':<20}{task[5]}")      
        print(f"{'Task description:':<20}")
        
        # Make description fit in defined width over multiple lines
        wrapped_description = (textwrap.fill(task[2], width = 58, 
        initial_indent = "  ", subsequent_indent = "  "))
        print(wrapped_description)
        print("\u2500" * 60)
        print()



# Create view_my_tasks function
def view_my_tasks():

    # Call read_task_file() to get task_list_all
    read_task_file()

    # Initialaize user_task_list
    user_task_list = []

    # Check if user has any tasks assigned to them
    username_in_task_data = False

    for task in task_list_all:

        if username == task[0]:
            
            # Add the task to the user_task_list and set username_in_task_data to True
            user_task_list.append(task)
            username_in_task_data = True
            
    # If user has no tasks assigned to them, print message
    if not username_in_task_data:
        print("You have no tasks assigned to you."+ "\n")
    
    else:
        for pos, user_task in enumerate(user_task_list, start = 1):
            
            # Add number of the task as an index of user_task_list
            

            # Print out details for each task
            pos_str = str(pos)
            pos_title = "Task number " + pos_str

            # Output task details in a table format
            print(pos_title.center(60, "\u2500") + "\n")
            print(f"{'Task:':<20}{user_task[1]}")
            print(f"{'Assigned to:':<20}{user_task[0]}")
            print(f"{'Date assigned:':<20}{user_task[3]}")
            print(f"{'Due date:':<20}{user_task[4]}")
            print(f"{'Task Complete?':<20}{user_task[5]}")      
            print(f"{'Task description:':<20}")
            
            # Make description fit in defined width over multiple lines
            wrapped_description = (textwrap.fill(user_task[2], width = 58, 
            initial_indent = "  ", subsequent_indent = "  "))
            print(wrapped_description)
            print("\u2500" * 60)
            print()

    return user_task_list



def edit_task():

    # Call read_task_file() to get task_list_all
    read_task_file()

    task_list_all_numbered = []

    # Interate over task_list_all and add index at the end of each task with the number for that task
    for index, task in enumerate(task_list_all):
        task.append(index+1)
        task_list_all_numbered.append(task)

    user_task_list_numbered = []

    # iterate over user_task_list and add index at the end of each task with the number for that task
    for pos, user_task in enumerate(task_list_all_numbered):
        if username == user_task[0]:
            user_task.append(pos+1)
            user_task_list_numbered.append(user_task)
    
    # Ask user to enter the number of the task they want to edit or enter -1 to return to the main menu
    while True:
        try:
            task_number = int(input("Enter the number of the task you want to edit or enter -1 to return to the main menu: "))
            if task_number == -1:
                break
            elif task_number < -1 or task_number > len(user_task_list_numbered):
                print("Error: Invalid task number.")
                print()
            else:
                break
        except ValueError:
            print("Error: Invalid task number.")
            print()
    # Display the task details for the task the user wants to edit
    if task_number != -1:
        task_number_title = "You have chosen to edit task number " + str(task_number)
        for user_task in user_task_list_numbered:
            if task_number == user_task[7]:
                print(task_number_title.center(60, "\u2500") + "\n")
                print(f"{'Task:':<20}{user_task[1]}")
                print(f"{'Assigned to:':<20}{user_task[0]}")
                print(f"{'Date assigned:':<20}{user_task[3]}")
                print(f"{'Due date:':<20}{user_task[4]}")
                print(f"{'Task Complete?':<20}{user_task[5]}")      
                print(f"{'Task description:':<20}")
                
                # Make description fit in defined width over multiple lines
                wrapped_description = (textwrap.fill(user_task[2], width = 58, 
                initial_indent = "  ", subsequent_indent = "  "))
                print(wrapped_description)
                print("\u2500" * 60)
                print()

    # Ask the user if they want to edit the task or mark it as complete or enter -1 to return to the main menu
    if task_number != -1:
        while True:
            try:
                edit_task = int(input("Enter 1 to edit the task, 2 to mark it as complete or -1 to return to the main menu: "))
                if edit_task == -1:
                    break
                elif edit_task < -1 or edit_task > 2:
                    print("Error: Invalid option.")
                    print()
                else:
                    break
            except ValueError:
                print("Error: Invalid option.")
                print()
    
    # Edit due date and check that the due date is not in the past
    if edit_task == 1:
        while True:
            try:
                due_date = input("Enter the new due date (dd mmm yyyy): ")
                due_date = datetime.strptime(due_date, "%d %b %Y")
                if due_date < datetime.now():
                    print("Error: Due date cannot be in the past.")
                    print()
                else:
                    break
            except ValueError:
                print("Error: Invalid due date.")
                print()

        # Edit task_list_all_numbered
        for user_task in user_task_list_numbered:
            if task_number == user_task[7]:
                user_task[4] = due_date.strftime("%d %b %Y")
                break

        # Edit task_list_all by using index 6 in user_task_list_numbered to identify the task in task_list_all
        for task in task_list_all_numbered:
            if task[6] == user_task[6]:
                task[4] = due_date.strftime("%d %b %Y")
                break
    
    # Mark task as complete
    elif edit_task == 2:
        for user_task in user_task_list_numbered:
            if task_number == user_task[7]:
                user_task[5] = "Yes"
                break

        for task in task_list_all_numbered:
            if task[6] == user_task[6]:
                task[5] = "Yes"
                break
    
    # Write index 0-5 from task_list_all_numbered to tasks_TEST.txt using seek and truncate
    with open("tasks_TEST.txt", "r+") as task_file:
        task_file.seek(0, 2)
        pos = task_file.tell()
        for task in task_list_all_numbered:
            task_file.write("\n"+f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {task[5]}")
            if pos > 0 and task_file.read() != "\n":
                task_file.seek(pos)
                task_file.truncate()

    # Return to main menu
    if edit_task == -1:
        return




# Create function to generate reports
def gen_reports():
    # Call read_task_file() to get task_list_all
    read_task_file()
    
    # Call read_user_file() to get user_pass_dict
    read_user_file()

    # Initialise variables
    overdue_tasks = 0
    incomplete_tasks = 0
    complete_tasks = 0
    total_tasks = 0

    # Loop through task_list_all to count tasks
    for task in task_list_all:

        # Check if task is complete
        if task[5].lower() == "yes":
            complete_tasks += 1
        else:
            incomplete_tasks += 1

        # Check if task is overdue
        due_date = datetime.strptime(task[4], "%d %b %Y")
        current_date = datetime.now()
        if due_date < current_date:
            overdue_tasks += 1
        
        # Count total tasks
        total_tasks += 1

    # Calculate percentaage of incomplete tasks
    incomplete_tasks_percent = round((incomplete_tasks / total_tasks) * 100)
    # Calculate percentaage of overdue tasks
    overdue_tasks_percent = round((overdue_tasks / total_tasks) * 100)

    # Write results to file in and easy to read format
    task_overview = "TASK OVERVIEW"
    with open("task_overview_TEST.txt", "w") as file:
        file.write(task_overview.center(60, "\u2500") + "\n")
        file.write(f"{'Total number of tasks:':<30}{total_tasks:>10}" + "\n")
        file.write(f"{'Completed tasks:':<30}{complete_tasks:>10}" + "\n")
        file.write(f"{'Incomplete tasks:':<30}{incomplete_tasks:>10}" + "\n")
        file.write(f"{'Incomplete tasks (%):':<30}{incomplete_tasks_percent:>10}%" + "\n")
        file.write(f"{'Overdue tasks:':<30}{overdue_tasks:>10}" + "\n")
        file.write(f"{'Overdue tasks (%):':<30}{overdue_tasks_percent:>10}%" + "\n")
        file.write("\u2500" * 60 + "\n")



    # Open user_overview.txt in write mode
    with open("user_overview_TEST.txt", "w") as file:
        
        # Calculate number of users
        number_of_users = len(user_pass_dict)

        # Write results to file in and easy to read format
        task_overview = "USER OVERVIEW"
        file.write(task_overview.center(60, "\u2500") + "\n")
        file.write(f"{'Number of users:':<30}{number_of_users:>10}" + "\n")
        file.write(f"{'Total number of tasks:':<30}{total_tasks:>10}" + "\n")
        file.write("\u2500" * 60 + "\n")

        for user in user_pass_dict:
            # Initialize variables
            overdue_tasks_user = 0
            incomplete_tasks_user = 0
            complete_tasks_user = 0
            total_tasks_user = 0

            # Loop through task_list_all to count tasks
            for task in task_list_all:
                if task[0] == user:
                    # Check if task is complete
                    if task[5].lower() == "yes":
                        complete_tasks_user += 1
                    else:
                        incomplete_tasks_user += 1

                    # Check if task is overdue
                    due_date = datetime.strptime(task[4], "%d %b %Y")
                    current_date = datetime.now()
                    if due_date < current_date:
                        overdue_tasks_user += 1

                    # Count total tasks
                    total_tasks_user += 1

            # Check if the user has any tasks
            if total_tasks_user > 0:

                # The percentage of the total number of tasks that have been assigned to that user
                percent_of_total = round((total_tasks_user / total_tasks) * 100)

                # The percentage of the tasks assigned to that user that have been completed
                percent_complete = round((complete_tasks_user / total_tasks_user) * 100)

                # The percentage of the tasks assigned to that user that must still be completed
                percent_incomplete = round((incomplete_tasks_user / total_tasks_user) * 100)

                # The percentage of the tasks assigned to that user that have not yet been completed and are overdue
                percent_overdue = round((overdue_tasks_user / total_tasks_user) * 100)

            else:
                incomplete_tasks_percent = 0
                overdue_tasks_percent = 0

            # Write results to file       
            task_overview = f"USER OVERVIEW - {user}"
            file.write(task_overview.center(60, "\u2500") + "\n")
            file.write(f"{'User tasks:':<30}{total_tasks_user:>10}" + "\n")
            file.write(f"{'User portion of all tasks:':<30}{percent_of_total:>10}%" + "\n")
            file.write(f"{'Completed user tasks:':<30}{percent_complete:>10}%" + "\n")
            file.write(f"{'Incomplete user tasks:':<30}{percent_incomplete:>10}%" + "\n")
            file.write(f"{'Overdue user tasks:':<30}{percent_overdue:>10}%" + "\n")
            file.write("\u2500" * 60 + "\n")




# Create function to display statistics from task_overview.txt and user_overview.txt
def display_stats():

    # First generate the reports
    gen_reports()

    # Open task_overview.txt in read mode
    with open("task_overview_TEST.txt", "r") as file:
        # Read the file line by line
        for line in file:
            # Print each line
            print(line, end="")
    print()

    # Open user_overview.txt in read mode
    with open("user_overview_TEST.txt", "r") as file:
        # Read the file line by line
        for line in file:
            # Print each line
            print(line, end="")
    print()











# MAIN PROGRAM


# Call functions to read files and save data in variables
user_pass_dict = read_user_file()
task_list_all = read_task_file()

# Ask the user to enter a username and password
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Make username case insensitive
    username = username.lower()

    # Check if username is in dictionary and if password is matching username
    if username in user_pass_dict and user_pass_dict[username] == password:
        print("You have successfully logged in!" + "\n")
        break
    else:
        print("Error: Invalid username or password.")
        print("Please enter a valid username and password." + "\n")



# Display the menu
while True:
    if username == "admin":
        choice = display_admin_menu()
    else:
        choice = display_user_menu()

    # Register new user
    if choice == 'r':
        # Call reg_user function
        reg_user()

    # Assign task
    elif choice == 'a':
        # Call add_task function
        add_task()

    # View all tasks
    elif choice == 'va':
        # Call view_all_tasks function
        view_all_tasks()

    # View all tasks for logged in user
    elif choice == 'vm':

        # Call view_my_tasks function
        view_my_tasks()
        edit_task()



    # Generate reports
    elif choice == 'gr':
        # Call gen_reports function
        gen_reports()
        print()
        print("\u2500" * 60)
        # Print confirmation message
        print("Task overview report has been generated successfully!")
        # Print confirmation message
        print("User overview report has been generated successfully!")
        print("\u2500" * 60)
        print()

    # Display statistics
    elif choice == 'ds':
        # Call display_stats function
        display_stats()

    # Exit program
    elif choice == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("Invalid entry, Please Try again." + "\n")

