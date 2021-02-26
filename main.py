import view
import controller
import model


if __name__ == '__main__':
    model_ = model.Model()
    controller_ = controller.Controller(model_)
    view_ = view.View(controller_)
    view_.display_main_menu()