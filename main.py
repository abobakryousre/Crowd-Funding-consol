from library import validator
import json

usr_information = {}


def display_main_menu():
    login = False

    while not login:
        print("1) Login")
        print("2) Sign Up ")
        print("3) Exit ")
        try:
            option = int(input("enter your option: "))
        except:
            print("Your option must be a number! ")
        else:
            if option == 1:
                load_login_page()
                login = True
            elif option == 2:
                load_sginup_page()
            elif option == 3:
                break
            else:
                print("You option not  in range 1 -> 3 !")


def load_sginup_page():
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
        username = input("email: ")
        password = input("Password: ")
        if not valid_user(username, password):
            print("Invalid Email or Password, Please try again..")
        else:
            logedin = True
            print(usr_information)
            load_project_pages()


def valid_user(username, password):
    valid = False
    global usr_information

    with open("users.txt", "r") as users:
        all_users = json.load(users)
        for user in all_users:
            if username == user.get("email"):
                if password == user.get("password"):
                    valid = True
                    usr_information = user
                    break

    if valid:
        return True
    else:
        return False


def load_project_pages():
    print("1) Create a new Project")
    print("2) View all projects ")
    print("3) Edit  project ")
    print("4) Delete  project")
    try:
        option = int(input("enter your option: "))
    except:
        print("Your option must be a number! ")
    else:
        if option == 1:
            create_project()
        elif option == 2:
            view_all_projects()
        elif option == 3:
            pass
        elif option == 4:
            pass
        else:
            print("You option not  in range 1 -> 4 !")


def create_project():
    created = False
    while not created:
        title = input("Enter project title: ")
        if not title.isalpha():
            print("Please enter  a valid title...")
            continue

        details = input("Project details: ")

        if not details.isalpha():
            print("Please enter  a valid title...")
            continue

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

        for projects in all_projects:
            for key in projects:
                print(f"{key} : {projects[key]}")


def edite_poject():
    pass


def delete_project():
    pass


def main():
    display_main_menu()


if __name__ == '__main__':
    main()
