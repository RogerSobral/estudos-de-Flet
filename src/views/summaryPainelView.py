from flet import *

class SummaryPainelView(UserControl):

    def __init__(self):
        super().__init__()
        self.cardGraphic=Card()
        self.card = Card()
        self.optionHide= PopupMenuButton(
                            items=[
                                PopupMenuItem(content=Checkbox(label="Receitas", value=False)),
                                PopupMenuItem(content=Checkbox(label="Despesas", value=False)),
                                PopupMenuItem(content=Checkbox(label="Contas", value=False)),
                                PopupMenuItem(content=Checkbox(label="Cartões", value=False)),
                            ]
                        )
        self.receitaReal=Text("R$ 0,00", size=16, weight=FontWeight.BOLD)
        self.receitaPrevista =Text("R$ 0,00", size=12)
        self.despesaReal = Text("R$ 0,00", size=16, weight=FontWeight.BOLD)
        self.despesaPrevista = Text("R$ 0,00", size=12)
        self.contaReal = Text("R$ 0,00", size=16, weight=FontWeight.BOLD)
        self.contaPrevista = Text("R$ 0,00", size=12)
        self.cataoReal = Text("R$ 0,00", size=16, weight=FontWeight.BOLD)
        self.cartaoPrevisto = Text("R$ 0,00", size=12)
        self.valorCaixa=Text("R$0.00", size=18, weight=FontWeight.W_500)
        self.receitasConsideradas=Text("R$0,00", size=10, color=colors.BLUE)
        self.despesasConsideradas = Text("R$0,00", size=10, color=colors.BLUE)

        self.card2=Card()
        self.iconReceita = IconButton(icons.ADD, icon_color=colors.BLUE)
        self.scroll=Column(scroll=ScrollMode.ADAPTIVE)

    def build(self):
        self.cardGraphic.content=Container(margin=10,
                                           content=Column(controls=[
                                               Row(controls=[Text("Balanço Mensal", size=18, weight=FontWeight.BOLD)]),
                                           #Grafico vem aqui
                                               Text("Grafico")
                                           ])
                                           )
        self.card.content = Container(
            content=Column(controls=[
                Row(
                    controls=[
                        Container(content=Text("Visão Geral", size=20, weight=FontWeight.BOLD), padding=10)
                        ,
                    self.optionHide
                       ,

                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN

                ),  # finish of first line

                Row(controls=[  # second of first line
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
                            self.receitaReal,
                            self.receitaPrevista
                        ],

                    ),
                        padding=10
                    )

                ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,

                ),  # finish of second line

                Row(controls=[  # third line
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
                            self.despesaReal,
                            self.despesaPrevista
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
                            self.contaReal,
                            self.contaPrevista
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
                            self.cataoReal,
                            self.cartaoPrevisto
                        ],

                    ),
                        padding=10
                    )

                ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,

                )  # finish of forth line

            ]
            ))

        self.card2.content=Container(
            margin=10,
            content=Column(controls=[Row(controls=[Text("Balanço Mensal", size=18, weight=FontWeight.BOLD)]),
                                     Row(controls=[
                                         Column(controls=[
                                             Column(controls=[
                                                 self.valorCaixa,
                                                 Text("Valor em Caixa")]),

                                         ], ),

                                         Column(
                                             controls=[
                                                 Text("Receita Consideradas", size=12, weight=FontWeight.BOLD),
                                                 self.receitasConsideradas,
                                                 Text("Despesas Consideradas ", size=12, weight=FontWeight.BOLD),
                                                 self.despesasConsideradas

                                             ]

                                         )

                                     ],
                                         alignment=MainAxisAlignment.SPACE_BETWEEN
                                     )

                                     ])
        )




        self.scroll.controls.append(self.cardGraphic)
        self.scroll.controls.append(self.card)
        self.scroll.controls.append(self.card2)
        return self.scroll

