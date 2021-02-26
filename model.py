import json
from builtins import dict


class Model:

    def get_all_users(self):
        with open("users.txt", "r") as users:
            all_users = json.load(users)
            return all_users

    def add_new_user(self, user):
        new_usr = user
        with open("users.txt", "r") as users:
            all_user = json.load(users)
            all_user.append(new_usr)
        with open("users.txt", "w") as users:
            json.dump(all_user, users)
