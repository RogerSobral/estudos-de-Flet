from flet import *

class ViewMenu(AppBar):

    def __init__(self):
        super().__init__()

        self.iconBtn=IconButton(icons.MENU, icon_color=colors.WHITE)
        self.leading=self.iconBtn
        self.leading_width=40
        self.bgcolor = "#65469b"
        self.month=Text("Janeiro", color=colors.WHITE)
        self.backMonth=IconButton(icons.ARROW_BACK_IOS, icon_color=colors.WHITE)
        self.nextMonth=IconButton(icons.ARROW_FORWARD_IOS, icon_color=colors.WHITE)

        self.title=Row(controls=[
                self.backMonth,
                self.month,
                self.nextMonth
            ], alignment=MainAxisAlignment.SPACE_AROUND)
        self.center_title = False
        self.color=colors.WHITE
        self.actions=[
                PopupMenuButton(
                    items=[
                        PopupMenuItem(text="Arquivos"),
                        PopupMenuItem(text="Configurações")  # divider
                    ]

                ),

            ]


