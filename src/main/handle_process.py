from flet import *
from .constructor.login_contructor import loginConstructo
from .constructor.menuPrincipal_constructor import menuConstructor

def main(page: Page):
    page.title="Finanças"
    page.horizontal_alignment=MainAxisAlignment.CENTER
    page.window_center()

    page.window_min_width=320



    def changePage(route):
        page.views.clear()

        page.views.append(
            View(
                "/",
                [
                   loginConstructo()
                ]
            )
        )
        if page.route=="/menu":

            page.views.append(

                View(
                    "/menu",
                    [


                            menuConstructor()


                       ],
                    # Aqui começa o drawer


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


