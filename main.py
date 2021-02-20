from library import validator
import json

usr_information = {}


def display_main_menu():
    login = False

    while not login:
        print("1) Login")
        print("2) Sign Up ")
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
            print("Invalid Username or Password, Please try again..")
        else:
            logedin = True
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
    pass


def main():
    display_main_menu()


if __name__ == '__main__':
    main()
