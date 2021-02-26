from library import validator
import json
usr_information = {}


def display_main_menu():
    while True:
        print("1) Login")
        print("2) Sign Up ")
        print("3) Exit ")
        try:
            option = int(input("enter your option: "))
        except ValueError:
            print("Your option must be a number! ")
        else:
            if option == 1:
                load_login_page()
            elif option == 2:
                load_signup_page()
            elif option == 3:
                break
            else:
                print("You option not  in range 1 -> 3 !")



def load_signup_page():
    signedup = False
    while not signedup:
        first_name = input("Enter your first name: ")
        if not validator.check_username(first_name):
            print("Invalid Name!")
            continue

        last_name = input("Enter your last name: ")
        if not validator.check_username(last_name):
            print("Invalid Name !")
            continue

        email = input("Enter your email: ")
        if not validator.check_email(email):
            print("Invalid Email !")
            continue
        password = input("Enter your password: ")
        confirm_password = input("Please Confirm your password: ")
        if not validator.confirm_password(password, confirm_password):
            print("Password Not match !")
            continue

        mobile = input("Enter your mobile phone: ")
        if not validator.check_mobile(mobile):
            print("Invalid Mobile number !")
            continue
        else:
            print("Sign up successfully ")
            add_new_user(first_name, last_name, email, password, mobile)
            signedup = True


def add_new_user(first_name, last_name, email, password, mobile):
    new_usr = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "mobile": mobile
    }

    with open("users.txt", "r") as users:
        all_user = json.load(users)
        usr_id = len(all_user) + 1
        new_usr["id"] = usr_id
        all_user.append(new_usr)

    with open("users.txt", "w") as users:
        json.dump(all_user, users)


def load_login_page():
    logedin = False
    while not logedin:
        email = input("email: ")
        password = input("Password: ")
        if not valid_user(email, password):
            print("Invalid Email or Password, Please try again..")
        else:
            logedin = True
            load_project_pages()


def valid_user(email, password):
    global usr_information

    with open("users.txt", "r") as users:
        all_users = json.load(users)
        for user in all_users:
            if email == user.get("email") and password == user.get("password"):
                usr_information = user
                return True

    return False


def load_project_pages():
    while True:
        print()
        print("1) Create a new Project")
        print("2) View all projects ")
        print("3) Edit  project ")
        print("4) Delete  project")
        print("5) Exit ")
        print()
        try:
            option = int(input("enter your option: "))
        except ValueError as ex:
            print("Your option must be a number! ")
        else:
            if option == 5:
                break
            elif option == 1:
                create_project()
            elif option == 2:
                view_all_projects()
            elif option == 3:
                load_edit_project_page()
            elif option == 4:
                load_delete_project_page()
            else:
                print("You option not  in range 1 -> 5 !")


def create_project():
    created = False
    while not created:
        title = input("Enter project title: ")
        if not title.isalpha():
            print("Invalid title name, the title should be contain only characters")
            continue

        details = input("Project details: ")

        target = input("Project total target: ")
        if not target.isdigit():
            print("Please enter a number for project target..")
            continue

        start_time = input("Start time: ")
        end_time = input("End time: ")

        if not validator.check_time_structure(start_time, end_time):
            print("Please enter a valid date structure, example( yyyy-mm-dd/ 2020-04-31 )")
            continue
        else:
            add_new_project(title, details, target, start_time, end_time)
            created = True


def add_new_project(title, details, target, start_time, end_time):
    new_project = {
        "title": title,
        "details": details,
        "target": target,
        "start_time": start_time,
        "end_time": end_time,
        "id": usr_information.get("id")
    }

    with open("projects.txt", "r") as projects:
        all_projects = json.load(projects)
        all_projects.append(new_project)

    with open("projects.txt", "w") as projects:
        json.dump(all_projects, projects)


def view_all_projects():
    with open("projects.txt", "r") as projects:
        all_projects = json.load(projects)
        if all_projects:
            for projects in all_projects:
                for key in projects:
                    print(f"{key} : {projects[key]}")
                print("--------------------------------")
        else:
            print("No project Created yet!")


def load_edit_project_page():
    correct_title = False
    while not correct_title:
        project_title = input("Enter project title or 'q' to exit: ")
        if project_title == "q":
            break
        elif not project_exist(project_title):
            print("This not exist in your projects.., please check it again")
        else:
            update_project(project_title)
            correct_title = True


def project_exist(project_title):
    exist = False
    with open("projects.txt", "r") as projects:
        all_projects = json.load(projects)
        for project in all_projects:
            if project.get("id") == usr_information.get("id") and project.get("title") == project_title:
                exist = True

    if not exist:
        return False
    else:
        return True


def update_project(project_title):
    updated = False

    while not updated:
        key = input(
            "Which section you would like to updated or enter 'q' to exit example(title, details, target, start_time, end_time): ")

        if key == "q":
            break

        elif key == "title" or key == "details" or key == "target" or key == "start_time" or key == "end_time":
            value = input("Enter the new value: ")
            if key == "title":
                if not value.isalpha():
                    print("Invalid title name, the title should be contain only characters")
                else:
                    updated = True

            elif key == "target":
                if not value.isdigit():
                    print("Invalid target.., please enter numbers for project target")
                else:
                    updated = True
            elif key == "start_time" or key == "end_time":
                if not validator.check_time_structure(key, key):
                    print("Invalid date structure, please try again..")
                else:
                    updated = True

        else:
            print("this section does not exist, please try again...")

        if updated:
            update_project_value(project_title, key, value)
            print("Project Updated successfully..")


def update_project_value(project_title, key, value):
    with open("projects.txt", "r") as projects:
        all_projects = json.load(projects)
        for project in all_projects:
            if project.get("title") == project_title:
                project[key] = value
                break


    with open("projects.txt", "w") as projects:
        json.dump(all_projects, projects)


def load_delete_project_page():
    correct_title = False
    while not correct_title:
        project_title = input("Enter project title: ")
        if not project_exist(project_title):
            print("This not exist in your projects.., please check it again")
        else:
            remove_project(project_title)
            correct_title = True
            print("The project Removed successfully....")


def remove_project(project_title):
    with open("projects.txt", "r") as projects:
        all_projects = json.load(projects)
        updated_projects = []
        for project in all_projects:
            if project.get("title") != project_title:
                updated_projects.append(project)

    with open("projects.txt", "w") as projects:
        json.dump(updated_projects, projects)


if __name__ == '__main__':
    display_main_menu()
