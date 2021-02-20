def check_username(username):
    if username is None or username.isdigit():
        return False
    else:
        return True


def confirm_password(first_password, second_password):
    if first_password == second_password:
        return True
    else:
        return False
