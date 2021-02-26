
class View:

    def __init__(self, controller):
        self.controller = controller

    def display_main_menu(self):
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
                    self.load_login_page(self.controller)
                elif option == 2:
                    self.load_signup_page(self.controller)
                elif option == 3:
                    break
                else:
                    print("You option not  in range 1 -> 3 !")

    @staticmethod
    def load_login_page(controller):
        logedin = False
        while not logedin:
            print("enter 'q' to exit")
            email = input("email: ")
            if email == 'q':
                break
            else:
                password = input("Password: ")

                
            if not controller.valid_user(email, password):
                print("Invalid Email or Password, Please try again..")
            else:
                logedin = True
                View.load_project_pages(controller)

    @staticmethod
    def load_signup_page(controller):
        signedup = False
        while not signedup:
            first_name = input("Enter your first name: ")
            if not controller.check_username(first_name):
                print("Invalid Name!")
                continue

            last_name = input("Enter your last name: ")
            if not controller.check_username(last_name):
                print("Invalid Name !")
                continue

            email = input("Enter your email: ")
            if not controller.check_email(email):
                print("Invalid Email !")
                continue
            password = input("Enter your password: ")
            confirm_password = input("Please Confirm your password: ")
            if not controller.confirm_password(password, confirm_password):
                print("Password Not match !")
                continue

            mobile = input("Enter your mobile phone: ")
            if not controller.check_mobile(mobile):
                print("Invalid Mobile number !")
                continue
            else:
                print("Sign up successfully ")
                controller.add_new_user(first_name, last_name, email, password, mobile)
                signedup = True

    @staticmethod
    def load_project_pages(controller):
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
                    View.create_project(controller)
                elif option == 2:
                    View.view_all_projects(controller)
                elif option == 3:
                    View.load_edit_project_page(controller)
                elif option == 4:
                    View.load_delete_project_page(controller)
                else:
                    print("You option not  in range 1 -> 5 !")

    @staticmethod
    def create_project(controller):
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

            if not controller.check_time_structure(start_time, end_time):
                print("Please enter a valid date structure, example( yyyy-mm-dd/ 2020-04-31 )")
                continue
            else:
                controller.add_new_project(title, details, target, start_time, end_time)
                created = True
    @staticmethod
    def view_all_projects(controller):
        pass
    @staticmethod
    def load_edit_project_page(controller):
        pass
    @staticmethod
    def load_delete_project_page(controller):
        pass