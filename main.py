import view
import controller
import model

usr_information = {}







def load_edit_project_page():
    correct_title = False
    while not correct_title:
        project_title = input("Enter project title or 'q' to exit: ")
        if project_title == "q":
            break
        elif not project_exist(project_title):
            print("This not exist in your projects.., please check it again")
        else:
            update_project(project_title)
            correct_title = True





def update_project(project_title):
    updated = False

    while not updated:
        key = input(
            "Which section you would like to updated or enter 'q' to exit example(title, details, target, start_time, end_time): ")

        if key == "q":
            break

        elif key == "title" or key == "details" or key == "target" or key == "start_time" or key == "end_time":
            value = input("Enter the new value: ")
            if key == "title":
                if not value.isalpha():
                    print("Invalid title name, the title should be contain only characters")
                else:
                    updated = True

            elif key == "target":
                if not value.isdigit():
                    print("Invalid target.., please enter numbers for project target")
                else:
                    updated = True
            elif key == "start_time" or key == "end_time":
                if not validator.check_time_structure(key, key):
                    print("Invalid date structure, please try again..")
                else:
                    updated = True

        else:
            print("this section does not exist, please try again...")

        if updated:
            update_project_value(project_title, key, value)
            print("Project Updated successfully..")


def update_project_value(project_title, key, value):
    with open("projects.txt", "r") as projects:
        all_projects = json.load(projects)
        for project in all_projects:
            if project.get("title") == project_title:
                project[key] = value
                break


    with open("projects.txt", "w") as projects:
        json.dump(all_projects, projects)


def load_delete_project_page():
    correct_title = False
    while not correct_title:
        project_title = input("Enter project title: ")
        if not project_exist(project_title):
            print("This not exist in your projects.., please check it again")
        else:
            remove_project(project_title)
            correct_title = True
            print("The project Removed successfully....")





if __name__ == '__main__':
    model_ = model.Model()
    controller_ = controller.Controller(model_)
    view_ = view.View(controller_)
    view_.display_main_menu()