from flet import *

class ViewMenu(AppBar):

    def __init__(self):
        super().__init__()

        self.iconBtn=IconButton(icons.MENU, icon_color=colors.WHITE)
        self.leading=self.iconBtn
        self.leading_width=40
        self.bgcolor = "#65469b"
        self.title=Row(controls=[
                IconButton(icons.ARROW_BACK_IOS, icon_color=colors.WHITE),
                Text("Janeiro", color=colors.WHITE),
                IconButton(icons.ARROW_FORWARD_IOS, icon_color=colors.WHITE),
            ], alignment=MainAxisAlignment.SPACE_AROUND)
        self.center_title = False
        self.color=colors.WHITE
        self.actions=[

                PopupMenuButton(

                    items=[
                        PopupMenuItem(text="Despesas"),
                        PopupMenuItem(text="Receitas"),  # divider

                    ]

                ),

            ]


