from library import validator as v
import model as m
import json

class User:

    def __init__(self, first_name, last_name, email, password, mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self. password = password
        self.mobile = mobile




class Controller:
    def __init__(self, model):
        self.validator = v.Validator()
        self.model = model
        self.usr_information = None

    def valid_user(self, email, password):
        all_users = self.model.get_all_users()
        for user in all_users:
            user = json.loads(user)
            if email == user.get("email") and password == user.get("password"):
                self.usr_information = user
                return True

        return False

    def get_user_information(self):
        if self.usr_information:
            return self.usr_information

    def check_username(self, firstname):
        if self.validator.check_username(firstname):
            return True
        else:
            return False

    def confirm_password(self, first_password, second_password):

        if self.validator.confirm_password(first_password, second_password):
            return True
        else:
            return False

    def check_email(self, email):
        if self.validator.check_email(email):
            return True
        else:
            return False

    def check_mobile(self, mobile):
        if self.validator.check_mobile(mobile):
            return True
        else:
            return False

    def check_time_structure(self, start_time, end_time):
        if self.validator.check_time_structure(start_time, end_time):
            return True
        else:
            return False

    def add_new_user(self, first_name, last_name, email, password, mobile):
        new_usr = User(first_name, last_name, email, password, mobile)
        new_usr = json.dumps(new_usr.__dict__)  # convert class obj to string
        self.model.add_new_user(new_usr)

    def add_new_project(self, new_project):
        pass


