from flet import (NavigationDrawer,NavigationDrawerDestination,
                  Container,Icon,icons,colors,Divider)

class MenuDrawerOption(NavigationDrawer):
    def __init__(self):
        super().__init__()
        self.controls=[
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
            NavigationDrawerDestination(
                icon_content=Icon(icons.SUPERVISED_USER_CIRCLE_SHARP, color=colors.BLACK),
                label="Compartilhar",
                selected_icon=icons.SUPERVISED_USER_CIRCLE_OUTLINED,
            ),

            NavigationDrawerDestination(
                icon_content=Icon(icons.CLOSE, color=colors.BLACK),
                label="Sair",
                selected_icon=icons.CLOSE,
            ),
        ]

