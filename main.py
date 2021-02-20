from library import validator
import json


def display_main_menu():
    logedin = False
    print("1) Login")
    print("2) Sign Up ")
    while not logedin:
        try:
            option = int(input("enter your option: "))
        except:
            print("Your option must be a number! ")
        else:
            if option == 1:
                load_login_page()
                logedin = True
            elif option == 2:
                load_sginup_page()


def load_login_page():
    pass


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
            print("1) Login")
            print("2) Sign Up ")
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


def main():
    display_main_menu()


if __name__ == '__main__':
    main()

