
from src.views.viewMenu import ViewMenu
from src.views.menuDrawerOption import MenuDrawerOption
class MenuMainController:
    
    def __init__(self,viewMenu:ViewMenu,drawerOption:MenuDrawerOption):
        self.drawerOptionController=drawerOption
        self.barMenuController=viewMenu
        self.barMenuController.iconBtn.on_click=self.openDrawerMenu

    def openDrawerMenu(self,e):
        self.drawerOptionController.open=True
        self.drawerOptionController.update()





