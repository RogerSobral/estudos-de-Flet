from flet import *

class CardGeneral(UserControl):
    def __init__(self):
        super().__init__()
        self.card=Card()
        self.iconReceita=IconButton(icons.ADD, icon_color=colors.BLUE)


    def build(self):

        self.card.content = Container(
            content=Column(controls=[
                            Row(
                                controls=[
                                    Container(content=Text("Visão Geral", size=20,weight=FontWeight.BOLD),padding=10)
                                    ,
                                          PopupMenuButton(

                                              items=[
                                                  PopupMenuItem(content=Checkbox(label="Receitas", value=False)),
                                                  PopupMenuItem(content=Checkbox(label="Despesas", value=False)),
                                                  PopupMenuItem(content=Checkbox(label="Contas", value=False)),
                                                  PopupMenuItem(content=Checkbox(label="Cartões", value=False)),
                                              ]
                                          ),

                                ],
                                alignment=MainAxisAlignment.SPACE_BETWEEN

                            ),# finish of first line

                Row(controls=[# second of first line
                    Container(
                        content=Row([
                                self.iconReceita,
                                Column(controls=[
                                    Text("Receita", size=18, weight=FontWeight.BOLD),
                                    Text("Previsto", size=12)
                                ])
                            ]
                        ),
                        padding=10
                    ),
                    Container(content=Column(
                        controls=[
                        Text("R$ 0,00", size=16, weight=FontWeight.BOLD),
                        Text("R$ 0,00", size=12)
                         ],

                    ),
                        padding=10
                    )


                ],
                 alignment = MainAxisAlignment.SPACE_BETWEEN,

                ), #finish of second line

                Row(controls=[  #  third line
                    Container(
                        content=Row(
                            controls=[
                                IconButton(icons.REMOVE_CIRCLE, icon_color=colors.RED),
                                Column(controls=[
                                    Text("Despesa", size=18, weight=FontWeight.BOLD),
                                    Text("Previsto", size=12)
                                ])
                            ]
                        ),
                        padding=10
                    ),
                    Container(content=Column(
                        controls=[
                            Text("R$ 0,00", size=16, weight=FontWeight.BOLD),
                            Text("R$ 0,00", size=12)
                        ],

                    ),
                        padding=10
                    )

                ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,

                ),  # finish of third line

                Row(controls=[  # forth   line
                    Container(
                        content=Row(
                            controls=[
                                IconButton(icons.WALLET, icon_color=colors.PURPLE),
                                Column(controls=[
                                    Text("Conta", size=18, weight=FontWeight.BOLD),
                                    Text("Previsto", size=12)
                                ])
                            ]
                        ),
                        padding=10
                    ),
                    Container(content=Column(
                        controls=[
                            Text("R$ 0,00", size=16, weight=FontWeight.BOLD),
                            Text("R$ 0,00", size=12)
                        ],

                    ),
                        padding=10
                    )

                ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,

                ),  # finish of forth line

                Row(controls=[  # fifth line
                    Container(
                        content=Row(
                            controls=[
                                IconButton(icons.CREDIT_CARD, icon_color=colors.GREEN_400),
                                Column(controls=[
                                    Text("Cartão de Credito", size=18, weight=FontWeight.BOLD),
                                    Text("Previsto", size=12)
                                ])
                            ]
                        ),
                        padding=10
                    ),
                    Container(content=Column(
                        controls=[
                            Text("R$ 0,00", size=16, weight=FontWeight.BOLD),
                            Text("R$ 0,00", size=12)
                        ],

                    ),
                        padding=10
                    )

                ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,

                )  # finish of forth line

            ]

            ))


        return self.card