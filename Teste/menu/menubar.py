import flet as ft

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title="Menu"

    cont = ft.Container(
        bgcolor="#E3B168",
        expand=True,
        width=page.width,
        height=page.height,
        animate_opacity=300,
        data="seila1"
    )
    cont2 = ft.Container(
        bgcolor="#B14FDB",
        expand=True,
        width=page.width,
        height=page.height,
        animate_opacity=300,
        content=ft.Text("Pagina 2"),
        data="seila"

    )
    def handle_menu_item_click(e):
        cont.opacity = 0 if cont.opacity == 1 else 1
        cont.update()

    def handle_menu_item_click2(e):
        print(e.control.data)
        cont2.opacity = 0 if cont2.opacity == 1 else 1
        cont2.update()




    menu_bar= ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.colors.AMBER_500,
            mouse_cursor={
                ft.MaterialState.HOVERED:ft.MouseCursor.CLICK,
                ft.MaterialState.DEFAULT:ft.MouseCursor.ZOOM_OUT,
            }
        ), # final do style
        controls=[
            ft.MenuItemButton(
            content=ft.Text("home"), # texto que vai no menu
            leading= ft.Icon(ft.icons.INFO), # icone que vai no menu
            style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.AMBER_200}),
            on_click=handle_menu_item_click,

        ),
            ft.MenuItemButton(
                content=ft.Text("Serviços"),  # texto que vai no menu
                leading=ft.Icon(ft.icons.INFO),  # icone que vai no menu
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.AMBER_200}),
                on_click=handle_menu_item_click2,

            ),
        ] # final do controls

    )

    linha1=ft.Row(controls=[menu_bar])
    linha2=ft.Row(controls=[cont2])
    page.add(ft.Column(controls=[linha1,linha2]))
    page.update()


ft.app(target=main)