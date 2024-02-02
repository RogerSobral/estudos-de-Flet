from flet import *
import datetime as dt
#import plotly.express as px
# pip install plotly-express
class Login(UserControl):

    def __init__(self, evento):
        super().__init__()
        self.evento=evento

    def build(self):

        img_top=Image("/img/login.svg")

        name=TextField(label="Digite o seu nome")
        password = TextField(label="Digite sua senha",password=True)
        btn_enter=ElevatedButton("Entrar",
                                 style=ButtonStyle(
                                     bgcolor=colors.GREEN_50,
                                     shape={
                                        MaterialState.DEFAULT: RoundedRectangleBorder(radius=0)

                                    },
                                 ),
                                 width=360,
                                 on_click=lambda  e: self.evento.go("/menu"),

                                 )

        line_img = ResponsiveRow([
                        Column( col={"xs": 12, "sm":12, "md":8}, controls=[

                            Column(col={"sm": 12,"md":8}, controls=[img_top],alignment=alignment.center),

                            Column(col={"sm": 12, "md": 8},
                                   controls=[
                                       name,
                                       password,
                                       Row(controls=[btn_enter],alignment=MainAxisAlignment.CENTER,)

                                   ],
                                   spacing=15


                            )
                        ],
                        alignment=MainAxisAlignment.CENTER
                        ), # final do responsivo
            ],
            alignment=MainAxisAlignment.CENTER
        )
        return line_img


class Graphics(UserControl):

    def build(self):
        self.line1=LineChartData(
            data_points=[
                LineChartDataPoint(1, 1),
                LineChartDataPoint(3, 1.5),
                LineChartDataPoint(5, 1.4),
                LineChartDataPoint(7, 3.4),
                LineChartDataPoint(10, 2),
                LineChartDataPoint(12, 2.2),
                LineChartDataPoint(13, 1.8),
            ],
            stroke_width=8,
            color=colors.LIGHT_GREEN,
            curved=True,
            stroke_cap_round=True,
        ),

        return None


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

class CardEconomicMonths(UserControl):

    def __init__(self):
        super().__init__()
        self.card=Card()


    def build(self):

        self.card.content=Container(
            margin=10,
            alignment=alignment.center,
            content=Row(
                controls=[
                  Row(controls=[
                      Column(
                          controls=[
                                   Text("Balanço Mensal", size=18, weight=FontWeight.BOLD),
                                   Text("R$0.00", size=18, weight=FontWeight.W_500),
                                   Text("Valor em Caixa")

                          ]
                      ),
                      Column(
                          controls=[
                              Text("Receita Consideradas", size=12, weight=FontWeight.BOLD),
                              Text("R$0,00", size=10, color=colors.BLUE),
                              Text("Despesas Consideradas ", size=12, weight=FontWeight.BOLD),
                              Text("R$0,00", size=10, color=colors.RED)

                          ]

                      )
                   ],
                      alignment=MainAxisAlignment.SPACE_BETWEEN
                  )
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            ),# finish of content
            # Here I go config paraters
            padding=10,

        )

        return self.card


def main(page: Page):
    page.title="Finanças"
    page.horizontal_alignment=MainAxisAlignment.CENTER
    page.window_center()
    page.window_height=800
    cardGeration=CardGeneral()

    radioRecorrente = RadioGroup(content=Row([
        Radio(value="Não Recorrente", label="Não Recorrente"),
        Radio(value="Fixa", label="Fixa"),
        Radio(value="Parcelamento", label="Parcelamento")],
    alignment=MainAxisAlignment.SPACE_AROUND))

    def show_bs(e):
        ViewReceita.open = True
        ViewReceita.update()

    def close_bs(e):
        ViewReceita.open = False
        ViewReceita.update()

    def show_date(e):
        date_receita.open=True
        date_receita.update()

    date_receita = DatePicker(
        first_date=dt.datetime(1950, 10, 1),
        last_date=dt.datetime(2050, 10, 1),
    )

    cardGeration.iconReceita.on_click=show_bs




    ViewReceita=BottomSheet(

        dismissible=False,
        is_scroll_controlled=True,
            content=Container(
                content=Column(
                    [
                        Row(controls=[Text("Cadastro de Receita", size=18, weight=FontWeight.BOLD),
                            IconButton(icons.CLOSE_ROUNDED, on_click=close_bs)],
                            alignment=MainAxisAlignment.SPACE_BETWEEN
                        ),

                        TextField(label="Descrição"),
                        TextField(label="Valor R$"),
                        radioRecorrente,
                        Divider(height=1, color="black"),
                        Row(
                            controls=[
                                Row(controls=[ Icon(icons.DATE_RANGE),
                                Text("Data vencimento")]
                                ),
                                Text("Hoje")
                            ],
                            alignment=MainAxisAlignment.SPACE_BETWEEN
                        ),
                        Divider(height=1, color="black"),
                        Row(
                            controls=[
                                Row(controls=[
                                    Icon(icons.CHECK_CIRCLE_OUTLINED),
                                    Text("Realizada")
                                ]),
                                Switch( value=False)
                            ],
                            alignment=MainAxisAlignment.SPACE_BETWEEN
                        ),
                        Divider(height=1, color="black"),
                        Column(
                            controls=[
                                Text("Categoria"),
                                Row(
                                    controls=[
                                        Row(controls=[
                                            Icon(icons.CATEGORY),
                                            Text("Outros"),]
                                        ),
                                        Icon(icons.ADD)
                                    ],
                                    alignment=MainAxisAlignment.SPACE_BETWEEN
                                )
                            ]
                        )




                    ],


                ),
                padding=20
            )
        )
    page.overlay.append(ViewReceita) # inserido a tela de receita vindo de baixo

    nav_drawer = NavigationDrawer(controls=[
            Container(height=12),
            NavigationDrawerDestination(

                label="Resumo",
                icon=icons.BAR_CHART,
                selected_icon_content=Icon(icons.SIGNAL_CELLULAR_ALT_2_BAR, color=colors.BLACK),
            ),
            Divider(thickness=2),
            NavigationDrawerDestination(
                icon_content=Icon(icons.WALLET_SHARP, color=colors.BLACK),
                label="Contas",
                selected_icon=icons.WALLET,
            ),
            NavigationDrawerDestination(
                icon_content=Icon(icons.PAYMENTS_OUTLINED, color=colors.BLACK),
                label="Transações",
                selected_icon=icons.PAYMENTS_ROUNDED,
            ),

            NavigationDrawerDestination(
                icon_content=Icon(icons.CREDIT_CARD, color=colors.BLACK),
                label="Cartões de Credito",
                selected_icon=icons.CREDIT_CARD_ROUNDED,
            ),
        ],
    )



    def show_nav_drawer(e):
        nav_drawer.open=True
        nav_drawer.update()


    def changePage(route):
        page.views.clear()

        page.views.append(
            View(
                "/",
                [
                    Login(page)
                ]
            )
        )
        if page.route=="/menu":

            page.views.append(

                View(

                    "/menu",
                    [
                        AppBar(
                            leading=IconButton(icons.MENU, icon_color=colors.WHITE, on_click=show_nav_drawer),
                            leading_width=40,
                            bgcolor=colors.BLACK,
                            title=Row(controls=[
                                IconButton(icons.ARROW_BACK_IOS, icon_color=colors.WHITE),
                                Text("Janeiro", color=colors.WHITE),
                                IconButton(icons.ARROW_FORWARD_IOS, icon_color=colors.WHITE),
                            ], alignment=MainAxisAlignment.SPACE_AROUND),
                            center_title=False,
                            color=colors.WHITE,

                            actions=[

                                PopupMenuButton(

                                    items=[
                                        PopupMenuItem(text="Despesas"),
                                        PopupMenuItem(text="Receitas"),  # divider

                                    ]

                                ),

                            ],
                        )

                        ,ElevatedButton("Voltar", on_click=lambda e: page.go("/")),


                       cardGeration,
                       CardEconomicMonths(),



                       ],
                    # Aqui começa o drawer
                    drawer=nav_drawer,


                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Carregar o alerta



    page.on_route_change = changePage
    page.on_view_pop = view_pop
    page.go(page.route)





app(target=main,assets_dir="assets")