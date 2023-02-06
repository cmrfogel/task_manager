


# Import modules
import textwrap
from datetime import datetime

# Global variables
user_pass_dict = {}
task_list_all = []
username = ""


# A function to read user.txt and return a dictionary of users + passwords
def read_user_file():
    
    with open("user.txt", "r") as f:
        user_pass_dict = {}
        for line in f:
            username, password = line.strip().split(", ")
            user_pass_dict[username] = password
    return user_pass_dict


# A function to read tasks.txt and return a list of lists
def read_task_file():
    
        with open("tasks.txt", "r") as f:
            
            task_list_all = []
            for line in f:
                
                # Splitting the line using multiple assignment of variables
                (task_username, task_title, task_description, current_date,
                due_date, task_status) = line.strip().split(", ")
                
                # Save details of each task as list in the list task_list_all
                task_list_all.append([task_username, task_title, 
                task_description, current_date, due_date, task_status])
        return task_list_all


# A function to display menu for admin
def display_admin_menu():

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


# A function to display menu for regular user
def display_user_menu():

        menu = input('''Please select one of the following options:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()
        print()
        return menu


# A function to register a new user
def reg_user():
    
    if username == "admin":
        
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
                
                # Add new username in lower case and password to user.txt
                with open("user.txt", "a") as f:
                    f.write("\n" + f"{new_username}, {new_password}")
                    print("New username and password registered!\n")
            else:
                print("Passwords do not match. Please try again.\n")
        else:
            print("Username already in use. Please, try again.\n")
    else:
        print("Invalid entry. Please, try again.\n")


# A function to add a new task
def add_task():
    
    while True:
        
        assign_user = input("Assign username to new task: ")
        assign_user = assign_user.lower()
        
        # Check if user is a registered user
        if assign_user in user_pass_dict:
            task_title = input("Enter a title for the new task: ")
            task_description = input("Enter a short description for the "+
            "new task: ")
            
            # Get the current date
            current_date = datetime.now()
            
            while True:
                
                # Parse input to datetime object or raise exception
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
                except ValueError as e:
                    print(e)
                    print("Please enter the date again in the format "+
                    "(dd Mon yyyy)")
                    
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
    with open("tasks.txt", "a") as f:
        f.write(
            "\n" + f"{assign_user}, {task_title}, {task_description}, "
            f"{current_date_str}, {due_date_str}, No"
        )
    print("New task registered!")


# A function to view all tasks
def view_all():
    
    # Call read_task_file() to get the latest data from the file
    read_task_file()
    
    # Print out details for each task
    for pos, task in enumerate(task_list_all, start = 1):
        pos_str = str(pos)
        pos_title = "Task number " + pos_str
        print(pos_title.center(60, "\u2500") + "\n")
        print(f"{'Task:':<20}{task[1]}")
        print(f"{'Assigned to:':<20}{task[0]}")
        print(f"{'Date assigned:':<20}{task[3]}")
        print(f"{'Due date:':<20}{task[4]}")
        print(f"{'Task Complete?':<20}{task[5]}")      
        print(f"{'Task description:':<20}")
        wrapped_description = (textwrap.fill(task[2], width = 58, 
        initial_indent = "  ", subsequent_indent = "  "))
        print(wrapped_description)
        print("\u2500" * 60)
        print()


# A function to view tasks assigned to the user and return user_task_list
def view_mine():
    
    # Call read_task_file() to get task_list_all
    read_task_file()
    
    user_task_list = []
    
    # Check if user has any tasks assigned to them
    username_in_task_data = False
    
    for task in task_list_all:
        
        if username == task[0]:
            
            # Add the task to user_task_list + set username_in_task_data to True
            user_task_list.append(task)
            username_in_task_data = True
            
    # If user has no tasks assigned to them, print message
    if not username_in_task_data:
        print("You have no tasks assigned to you."+ "\n")
        
    # Add number to each task in the list and print out details for each task
    else:
        for pos, user_task in enumerate(user_task_list, start = 1):
            pos_str = str(pos)
            pos_title = "Task number " + pos_str
            print(pos_title.center(60, "\u2500") + "\n")
            print(f"{'Task:':<20}{user_task[1]}")
            print(f"{'Assigned to:':<20}{user_task[0]}")
            print(f"{'Date assigned:':<20}{user_task[3]}")
            print(f"{'Due date:':<20}{user_task[4]}")
            print(f"{'Task Complete?':<20}{user_task[5]}")      
            print(f"{'Task description:':<20}")
            wrapped_description = (textwrap.fill(user_task[2], width = 58, 
            initial_indent = "  ", subsequent_indent = "  "))
            print(wrapped_description)
            print("\u2500" * 60)
            print()
            
    return user_task_list


# A function to edit a task
def edit_task():
    
    # Call read_task_file() to get task_list_all
    read_task_file()
    
    # Interate over task_list_all and add numbered index at the end of each task
    task_list_all_numbered = []
    
    for index, task in enumerate(task_list_all):
        task.append(index+1)
        task_list_all_numbered.append(task)
        
    # Iterate over user_task_list and add numbered index at the end of each task
    user_task_list_numbered = []
    user_task_index = 0
    
    for task in task_list_all_numbered:
        if username == task[0]:
            task.append(user_task_index + 1)
            user_task_list_numbered.append(task)
            user_task_index += 1
            
    # Enter task number to edit or enter -1 to return to the main menu
    while True:
        try:
            task_number = int(input("Enter the number of the task you want to "+
            "edit or enter -1 to return to the main menu: "))
            if task_number == -1:
                break
            elif (task_number < -1 or task_number == 0
            or task_number > len(user_task_list_numbered)):
                print("Error: Invalid task number.")
                print()
                
            # Check if task is already completed
            elif user_task_list_numbered[task_number - 1][5].lower() == "yes":
                print("Error: You cannot edit a completed task.")
                print()
            else:
                break
        except ValueError:
            print("Error: Invalid task number.")
            print()
            
    # Return to the main menu
    if task_number == -1:
        return
    
    # Display the task details for the task the user wants to edit
    if task_number != -1:
        
        task_number_title = ("You have chosen to edit task number "
                            + str(task_number))
                            
        for user_task in user_task_list_numbered:
            if task_number == user_task[7]:
                print()
                print(task_number_title.center(60, "\u2500") + "\n")
                print(f"{'Task:':<20}{user_task[1]}")
                print(f"{'Assigned to:':<20}{user_task[0]}")
                print(f"{'Date assigned:':<20}{user_task[3]}")
                print(f"{'Due date:':<20}{user_task[4]}")
                print(f"{'Task Complete?':<20}{user_task[5]}")      
                print(f"{'Task description:':<20}")
                wrapped_description = (textwrap.fill(user_task[2], width = 58, 
                initial_indent = "  ", subsequent_indent = "  "))
                print(wrapped_description)
                print("\u2500" * 60)
                print()
                
    # Choose to edit the task OR mark it as complete
    while True:
        try:
            edit_choice = int(input("Enter 1 to edit task, 2 to mark "+
                "it as complete, or -1 to return to the main menu: "))
            if edit_choice == -1:
                break
            elif edit_choice < -1 or edit_choice == 0 or edit_choice > 2:
                print("Error: Invalid option.")
                print()
            else:
                break
        except ValueError:
            print("Error: Invalid option.")
            print()
                
    # Choose to edit assigned user OR due date
    if edit_choice == 1:
        
        while True:
            try:
                edit_type = int(input("Enter 1 to edit assigned user, "+
                "2 to edit due date, or -1 to return to the main menu: "))
                if edit_type == -1:
                    break
                elif edit_type < -1 or edit_type == 0 or edit_type > 2:
                    print("Error: Invalid option.")
                    print()
                else:
                    break
            except ValueError:
                print("Error: Invalid option.")
                print()
                
        # Edit assigned user
        if edit_type == 1:
            while True:
                try:
                    assigned_user = input("Enter the new assigned user: ")
                    if assigned_user.lower() not in user_pass_dict:
                        print("Error: User does not exist.")
                        print()
                    else:
                        break
                except ValueError:
                    print("Error: Invalid entry.")
                    print()
                    
            # Edit user_task identified by index 7 in user_task_list_numbered
            for user_task in user_task_list_numbered:
                if task_number == user_task[7]:
                    user_task[0] = assigned_user
                    
            # Edit task identified by index 6 in both task lists
            for task in task_list_all_numbered:
                if task[6] == user_task[6]:
                    task[0] = assigned_user
            print("\nAssigned user updated!")
            print()
        
        # Edit due date
        if edit_type == 2:
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
                    
            # Edit user_task identified by index 7 in user_task_list_numbered
            for user_task in user_task_list_numbered:
                if task_number == user_task[7]:
                    user_task[4] = due_date.strftime("%d %b %Y")
                    
            # Edit task identified by index 6 in both task lists
            for task in task_list_all_numbered:
                if task[6] == user_task[6]:
                    task[4] = due_date.strftime("%d %b %Y")
            print("\nDue date updated!")
            print()
            
        # Write index 0-5 from task_list_all_numbered to tasks.txt
        with open("tasks.txt", "w") as task_file:
            for task in task_list_all_numbered:
                task_file.write(
                    f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, "
                    f"{task[5]}\n")
        
        # Return to the main menu
        if edit_type == -1:
            return
    
    # Mark task as complete - identified by index 7 in user_task_list_numbered
    elif edit_choice == 2:
        for user_task in user_task_list_numbered:
            if task_number == user_task[7]:
                user_task[5] = "Yes"
                
        # Edit task identified by index 6 in both task lists
        for task in task_list_all_numbered:
            if task[6] == user_task[6]:
                task[5] = "Yes"
        print("\nTask marked as complete!")
        print()
            
    # Write index 0-5 from task_list_all_numbered to tasks.txt
    with open("tasks.txt", "w") as task_file:
        for task in task_list_all_numbered:
            task_file.write(
                f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, "
                f"{task[5]}\n")
        
    # Return to main menu
    if edit_choice == -1:
        return


# A function to generate reports
def gen_reports():
    # Call read_task_file() to get task_list_all
    read_task_file()
    
    # Call read_user_file() to get user_pass_dict
    read_user_file()
    
    # Initialise variables
    incomplete_tasks = 0
    incomplete_and_over = 0
    complete_tasks = 0
    total_tasks = 0
    
    # Loop through task_list_all to count tasks
    for task in task_list_all:
        
        # Check if task is complete
        if task[5].lower() == "yes":
            complete_tasks += 1
        else:
            incomplete_tasks += 1
            
        # Check if task is overdue and incomplete
        due_date = datetime.strptime(task[4], "%d %b %Y")
        current_date = datetime.now()
        if due_date < current_date and task[5].lower() == "no":
            incomplete_and_over += 1
            
        # Count total tasks
        total_tasks += 1
        
    # Calculate percentaage of incomplete tasks
    incomplete_tasks_percent = round((incomplete_tasks / total_tasks) * 100)
    # Calculate percentaage of overdue tasks
    incomplete_and_over_percent = round((incomplete_and_over / total_tasks)* 100)
    
    # Write results to file in and easy to read format
    task_overview = "TASK OVERVIEW"
    with open("task_overview.txt", "w") as file:
        file.write(task_overview.center(60, "\u2500") + "\n")
        file.write(f"{'Total number of tasks:':<30}{total_tasks:>10}" + "\n")
        file.write(f"{'Completed tasks:':<30}{complete_tasks:>10}" + "\n")
        file.write(f"{'Incomplete tasks:':<30}{incomplete_tasks:>10}" + "\n")
        file.write(f"{'Incomplete tasks (%):':<30}"
        f"{incomplete_tasks_percent:>10}%" + "\n")
        file.write(f"{'Incomplete and Overdue:':<30}{incomplete_and_over:>10}"+"\n")
        file.write(f"{'Incomplete and Overdue (%):':<30}"
        f"{incomplete_and_over_percent:>10}%" + "\n")
        file.write("\u2500" * 60 + "\n")
        
    # Open user_overview.txt in write mode
    with open("user_overview.txt", "w") as file:
        
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
            incomplete_user = 0
            incomplete_and_over_user = 0
            complete_user = 0
            total_user = 0
            
            # Loop through task_list_all to count tasks for each user
            for task in task_list_all:
                if task[0] == user:
                    
                    total_user += 1
                    
                    # Check if task is complete or not
                    if task[5].lower() == "yes":
                        complete_user += 1
                    else:
                        incomplete_user += 1
                        
                    # Check if task is overdue
                    due_date = datetime.strptime(task[4], "%d %b %Y")
                    current_date = datetime.now()
                    if due_date < current_date and task[5].lower() == "no":
                        incomplete_and_over_user += 1
                        
            # Check if the user has any tasks or not and calculate percentages
            if total_user > 0:
                
                # % of tasks that have been assigned to user
                percent_of_total = round(
                    (total_user / total_tasks) * 100)
                    
                # % of the tasks assigned to user that have been completed
                percent_complete = round(
                    (complete_user / total_user) * 100)
                    
                # % of the tasks assigned to user still to be completed
                percent_incomplete = round(
                    (incomplete_user / total_user) * 100)
                    
                # % of the tasks assigned to user not yet completed and overdue
                percent_overdue = round(
                    (incomplete_and_over_user / total_user) * 100)
                    
            else:
                total_user = 0
                percent_of_total = 0
                percent_complete = 0
                percent_incomplete = 0
                percent_overdue = 0
                
            # Write results to file       
            task_overview = f"USER OVERVIEW - {user}"
            file.write(task_overview.center(60, "\u2500") + "\n")
            file.write(f"{'User tasks:':<30}{total_user:>10}" + "\n")
            file.write(f"{'User portion of all tasks:':<30}"
            f"{percent_of_total:>10}%" + "\n")
            file.write(f"{'Completed user tasks:':<30}"
            f"{percent_complete:>10}%" + "\n")
            file.write(f"{'Incomplete user tasks:':<30}"
            f"{percent_incomplete:>10}%" + "\n")
            file.write(f"{'Incomplete and Overdue:':<30}"
            f"{percent_overdue:>10}%" + "\n")
            file.write("\u2500" * 60 + "\n")


# A function to display statistics from task_overview.txt and user_overview.txt
def display_stats():
    
    # First generate the reports
    gen_reports()
    
    # Open task_overview.txt in read mode and print each line
    with open("task_overview.txt", "r") as file:
        for line in file:
            print(line, end="")
    print()
    
    # Open user_overview.txt in read mode and print each line
    with open("user_overview.txt", "r") as file:
        for line in file:
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
    username = username.lower()
    
    # Check if username is in dictionary and if password is matching username
    if username in user_pass_dict and user_pass_dict[username] == password:
        print("\nYou have successfully logged in!" + "\n")
        break
    else:
        print("\nError: Invalid username or password.")
        print("Please enter a valid username and password." + "\n")


# Display the menu by calling the function for the user type
while True:
    if username == "admin":
        choice = display_admin_menu()
    else:
        choice = display_user_menu()
        
    # Register new user - call reg_user function
    if choice == 'r':
        reg_user()
        
    # Assign new task - call assign_task function
    elif choice == 'a':
        add_task()
        
    # View all tasks - call view_all function
    elif choice == 'va':
        view_all()
        
    # View and edit tasks for user - call view_mine and edit_task functions
    elif choice == 'vm':
        view_mine()
        edit_task()
        
    # Generate reports - call gen_reports function and display confirmation
    elif choice == 'gr':
        gen_reports()
        print()
        print("\u2500" * 60)
        print("Task overview report has been generated successfully!")
        print("User overview report has been generated successfully!")
        print("\u2500" * 60)
        print()
        
    # Display statistics - call display_stats function
    elif choice == 'ds':
        display_stats()
        
    # Exit program
    elif choice == 'e':
        print('Goodbye!!!')
        exit()
        
    else:
        print("Invalid entry, Please Try again." + "\n")
