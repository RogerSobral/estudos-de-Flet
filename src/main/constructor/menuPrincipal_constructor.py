
from ...views.viewMenu import ViewMenu
from src.views.menuDrawerOption import MenuDrawerOption
from src.controllers.menuController import MenuMainController
def menuConstructor():
    barMenu=ViewMenu()
    menuoptionDrawer=MenuDrawerOption()
    barraMenuController=MenuMainController(barMenu,menuoptionDrawer)



    return barraMenuController