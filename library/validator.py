import re


class Validator:
    def check_username(self, username):
        if username is None or username.isdigit():
            return False
        else:
            return True

    def confirm_password(self, first_password, second_password):
        if first_password == second_password:
            return True
        else:
            return False

    def check_email(self, email):
        regex = '^[a-z][a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.match(regex, email):
            return True
        else:
            return False

    def check_mobile(self, mobile):
        if re.match(r"(01)[0-9]{9}", mobile):
            return True
        else:
            return False

    def check_time_structure(self, start_time, end_time):
        time_regex = r'^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])$'
        if re.match(time_regex, start_time) and re.match(time_regex, end_time):
            return True
        else:
            return False
