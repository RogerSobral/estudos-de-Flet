from flet import *
import datetime as dt
class CardIncomeView(BottomSheet):
    def __init__(self):
        super().__init__()
        self.descricaoReceita = TextField(label="Descrição")
        self.valorReceita = TextField(label="Valor R$")
        self.quantidadePrestacoes = TextField(label="1 x Vez", suffix_text="x vezes", width=100)
        self.textoRespostaPrestacoes = TextField(color=colors.BLUE, visible=False, width=90, suffix_text="x vezes",
                                            disabled=True)
        self.date_receita = DatePicker(
            date_picker_entry_mode=DatePickerEntryMode.CALENDAR_ONLY,
            # Modificar para português as datas
            # locale=timezone.localize(),
            help_text="Selecione entrada",
           # on_change=changeTextData,

            first_date=dt.datetime(1950, 10, 1),
            last_date=dt.datetime(2050, 10, 1),
        )

        self.optionsCategoryReceita = Dropdown(
            hint_text="Escolha uma categoria",

            options=[
                dropdown.Option("Outros"),
                dropdown.Option("Salário"),
                dropdown.Option("Mentoria"),
                dropdown.Option("Dividendos"),
            ],
        )

        self.optionsCategoryConta = Dropdown(
            hint_text="Escolha uma Conta",

            options=[
                dropdown.Option("Carteira"),
                dropdown.Option("Poupança Santander"),
                dropdown.Option("Poupança Nubank"),
                dropdown.Option("Corrente Bradesco"),
                dropdown.Option("Corrente Santander"),
            ],
        )

        self.textData=Text("Hoje")
        self.radioRecorrente = RadioGroup(content=Row([
            Radio(value="Não Recorrente", label="Não Recorrente"),
            Radio(value="Fixa", label="Fixa"),
            Radio(value="Parcelamento", label="Parcelamento")],
            alignment=MainAxisAlignment.SPACE_AROUND))
        self.quantityParcelas = AlertDialog(
            modal=True,
            title=Text("Parcelamento"),
            content=Text("Em quantas vezes pretende resceber"),
            actions=[
                self.quantidadePrestacoes,
                TextButton("Salvar")
            ],
            actions_alignment=MainAxisAlignment.END,
            on_dismiss=lambda e: print("cadastrado com sucesso"),
        )
        self.dismissible = False,
        self.is_scroll_controlled = True
        self.content=Container(
                content=Column(
                    [
                        Row(controls=[Text("Cadastro de Receita", size=18, weight=FontWeight.BOLD),
                            IconButton(icons.CLOSE_ROUNDED)],
                            alignment=MainAxisAlignment.SPACE_BETWEEN
                        ),
                        self.descricaoReceita,
                        self.valorReceita,
                        ResponsiveRow(controls=[Container(col=10,content=self.radioRecorrente,
                                                          alignment=alignment.center),
                                                Container(col=2,content=self.textoRespostaPrestacoes,
                                                          alignment=alignment.center)],
                                      alignment=MainAxisAlignment.SPACE_AROUND,
                                      vertical_alignment=CrossAxisAlignment.CENTER),self.quantityParcelas,

                        Divider(height=1, color="black"),
                        Row(
                            controls=[
                                Row(controls=[ IconButton(icons.CALENDAR_TODAY,on_click=
                                                          lambda _: self.date_receita.pick_date()),
                                Text("Data vencimento")]
                                ),
                                self.textData
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
                                           self.optionsCategoryReceita,
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
                                            self.optionsCategoryConta
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
                        #on_click= registerReceita
                        )





                    ],


                ),
                padding=20
            )



