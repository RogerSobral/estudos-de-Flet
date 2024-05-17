from flet import *


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
