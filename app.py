# -*- coding: UTF-8 -*-
from flet import *
import datetime as dt
#import plotly.express as px
# pip install plotly-express
# pip install pytz
import pytz
from src.views.login import Login
from src.views.cardgeneral import CardGeneral
from src.views import ViewMenu
from src.views import CardEconomicMonths

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







def main(page: Page):
    page.title="Finanças"
    page.horizontal_alignment=MainAxisAlignment.CENTER
    page.window_center()
    page.window_height=800

    # Functions of open
    def show_nav_drawer(e):
        nav_drawer.open = True
        nav_drawer.update()

    # Views
    login=Login(page)
    appBar=ViewMenu()
    appBar.iconBtn.on_click=show_nav_drawer

    # Cards
    cardGeration=CardGeneral()
    cardEconomicMonths=CardEconomicMonths()



    quantidadePrestacoes=TextField(label="1 x Vez", suffix_text="x vezes", width=100)
    textoRespostaPrestacoes = TextField(color=colors.BLUE, visible=False, width=90, suffix_text="x vezes", disabled=True)
    descricaoReceita=TextField(label="Descrição")
    valorReceita=TextField(label="Valor R$")

    dtz = dt.datetime.now()
    print(dtz)
    print(dtz.tzname())
    timezone = pytz.timezone("America/Sao_Paulo")
    mtz=timezone.localize(dtz)
    print(mtz.tzinfo)


#criar a função de registrar, validando entradas
    def registerReceita(e):
        if not descricaoReceita.value:
            descricaoReceita.error_text="Digite a Descrição"
            descricaoReceita.update()
        else:
            descricaoReceita.error_text = ""
            descricaoReceita.update()

    def changeModalExpense(e):
        quantityParcelas.open = False
        textoRespostaPrestacoes.visible = True
        textoRespostaPrestacoes.value = quantidadePrestacoes.value


        page.update()

    def close_dlg(e):
        quantityParcelas.open = False
        page.update()

    quantityParcelas=AlertDialog(
        modal=True,
        title=Text("Parcelamento"),
        content=Text("Em quantas vezes pretende resceber"),
        actions=[
            quantidadePrestacoes,
            TextButton("Salvar", on_click=changeModalExpense)
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("cadastrado com sucesso"),
    )




    def changeRadioRecorrent(e):
        if radioRecorrente.value=="Parcelamento":
            quantityParcelas.open=True

            page.update()


#Fazer com o qual não  feche a tela anterior
    radioRecorrente = RadioGroup( content=Row([
        Radio(value="Não Recorrente", label="Não Recorrente"),
        Radio(value="Fixa", label="Fixa"),
        Radio(value="Parcelamento", label="Parcelamento")],
    alignment=MainAxisAlignment.SPACE_AROUND),
    on_change=changeRadioRecorrent)

    def show_bs(e):
        ViewReceita.open = True
        ViewReceita.update()

    def close_bs(e):
        ViewReceita.open = False
        ViewReceita.update()


    textData=Text("Hoje")
    def changeTextData(e):
        textData.value= f"{date_receita.value.day}/{date_receita.value.month}/{date_receita.value.year}"
        textData.update()

    date_receita = DatePicker(
        date_picker_entry_mode=DatePickerEntryMode.CALENDAR_ONLY,
        #Modificar para português as datas
        # locale=timezone.localize(),
        help_text="Selecione entrada",
        on_change=changeTextData,

        first_date=dt.datetime(1950, 10, 1),
        last_date=dt.datetime(2050, 10, 1),
    )

    cardGeration.iconReceita.on_click=show_bs

    optionsCategoryReceita=Dropdown(
        hint_text="Escolha uma categoria",

        options=[
            dropdown.Option("Outros"),
            dropdown.Option("Salário"),
            dropdown.Option("Mentoria"),
            dropdown.Option("Dividendos"),
        ],
    )

    optionsCategoryConta = Dropdown(
        hint_text="Escolha uma Conta",

        options=[
            dropdown.Option("Carteira"),
            dropdown.Option("Poupança Santander"),
            dropdown.Option("Poupança Nubank"),
            dropdown.Option("Corrente Bradesco"),
            dropdown.Option("Corrente Santander"),
        ],
    )


#Carde da receita
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

                        descricaoReceita,
                        valorReceita,
                        ResponsiveRow(controls=[Container(col=10,content=radioRecorrente,alignment=alignment.center),Container(col=2,content=textoRespostaPrestacoes,alignment=alignment.center)], alignment=MainAxisAlignment.SPACE_AROUND,vertical_alignment=CrossAxisAlignment.CENTER),quantityParcelas,

                        Divider(height=1, color="black"),
                        Row(
                            controls=[
                                Row(controls=[ IconButton(icons.CALENDAR_TODAY,on_click=
                                                          lambda _: date_receita.pick_date()),
                                Text("Data vencimento")]
                                ),
                                textData
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
                                            #Continuar modificar aqui
                                           optionsCategoryReceita,
                                            ]
                                        ),
                                        Icon(icons.ADD)
                                    ],
                                    alignment=MainAxisAlignment.SPACE_BETWEEN
                                ),

                            ]
                        ),

                        Divider(height=1, color="black"),

                        Column(
                            controls=[
                                Text("Conta"),
                                Row(
                                    controls=[
                                        Row(controls=[
                                            # Continuar modificar aqui
                                            optionsCategoryConta
                                        ]
                                        ),
                                        Icon(icons.ADD)
                                    ],
                                    alignment=MainAxisAlignment.SPACE_BETWEEN
                                ),

                            ]
                        ),
                        Divider(height=1, color="black"),

                        Container(content=Row(

                            controls=[
                            Icon(icons.SAVE),
                            Text("Salvar")
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        ),

                        bgcolor=colors.AMBER_500,
                        margin=2,
                        padding=3,
                        on_click= registerReceita
                        )





                    ],


                ),
                padding=20
            )
        )
    page.overlay.append(ViewReceita) # inserido a tela de receita vindo de baixo

    page.overlay.append(date_receita)

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

    # sei la




    def changePage(route):
        page.views.clear()

        page.views.append(
            View(
                "/",
                [
                    login
                ]
            )
        )
        if page.route=="/menu":

            page.views.append(

                View(
                    "/menu",
                    [

                        appBar
                        ,ElevatedButton("Logout", on_click=lambda e: page.go("/")),

                       cardGeration,
                       cardEconomicMonths,



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





app(target=main, assets_dir="assets")