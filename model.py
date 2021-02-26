import json
from builtins import dict


class Model:

    def get_all_users(self):
        with open("users.txt", "r") as users:
            all_users = json.load(users)
            return all_users

    def add_new_user(self, user):
        with open("users.txt", "r") as users:
            all_user = json.load(users)
            all_user.append(user)
        with open("users.txt", "w") as users:
            json.dump(all_user, users)

    def add_new_project(self, new_project):
        all_projects = self.get_all_projects()
        all_projects.append(new_project)
        with open("projects.txt", "w") as projects:
            json.dump(all_projects, projects)



    def get_all_projects(self):
        with open("projects.txt", "r") as projects:
            all_projects = json.load(projects)
            return all_projects

    def remove_project(self, project_title):
        all_projects = self.get_all_projects()
        updated_projects = []
        for project in all_projects:
            project = json.loads(project)
            if project.get("title") != project_title:
                updated_projects.append(project)

        with open("projects.txt", "w") as projects:
            json.dump(updated_projects, projects)

    def update_project(self, project_title, key, value):
        all_projects = self.get_all_projects()
        updated_projects = []
        for project in all_projects:
            tmp_project = json.loads(project)
            if tmp_project.get("title") == project_title:
                tmp_project[key] = value
                new_updated_project = json.dumps(tmp_project)
                updated_projects.append(new_updated_project)
                break
            else:
                updated_projects.append(project)

        with open("projects.txt", "w") as projects:
            print(updated_projects)
            json.dump(updated_projects, projects)
