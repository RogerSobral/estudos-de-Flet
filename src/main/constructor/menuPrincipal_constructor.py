
from ...views.viewMenu import ViewMenu
from src.views.menuDrawerOption import MenuDrawerOption
from src.controllers.menuController import MenuMainController
from src.main.constructor.cardIncomeConstructor import cardIncomeConstructor
def menuConstructor():
    barMenu=ViewMenu()
    menuoptionDrawer=MenuDrawerOption()
    barraMenuController=MenuMainController(barMenu,menuoptionDrawer)



    return barraMenuController