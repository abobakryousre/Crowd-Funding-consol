from library import validator


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
    pass


def main():
    display_main_menu()


if __name__ == '__main__':
    main()
