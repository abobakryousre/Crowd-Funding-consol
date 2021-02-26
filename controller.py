from library import validator as v
import json


class User:

    def __init__(self, first_name, last_name, email, password, mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self. password = password
        self.mobile = mobile


class Project:

    def __init__(self, title, details, target, start_time, end_time, owner_email):
        self.title = title
        self.details = details
        self.target = target
        self.start_time = start_time
        self.end_time = end_time
        self.owner_email = owner_email


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
        new_usr = json.dumps(new_usr.__dict__)  # convert class obj to json string
        self.model.add_new_user(new_usr)

    def add_new_project(self, title, details, target, start_time, end_time):
        owner = self.get_user_information()
        new_project = Project(title, details, target, start_time, end_time, owner.get("email"))
        new_project = json.dumps(new_project.__dict__)  # convert class obj to json string
        self.model.add_new_project(new_project)

    def get_all_projects(self):
        all_projects = self.model.get_all_projects()
        tmp_list = [] # convert the json string to objects
        for project in all_projects:
            tmp_list.append(json.loads(project))

        return tmp_list

    def project_exist(self, project_title):
        owner = self.get_user_information()
        all_projects = self.model.get_all_projects()
        for project in all_projects:
            project = json.loads(project)
            if project.get("owner_email") == owner.get("email") and project.get("title") == project_title:
                return True

        return False

    def remove_project(self, project_title):
        self.model.remove_project(project_title)

    def update_project_value(self, project_title, key, value):
        self.model.update_project(project_title, key, value)

