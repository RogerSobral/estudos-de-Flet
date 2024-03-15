from flet import *

class Login(UserControl):

    def __init__(self, evento):
        super().__init__()
        self.evento=evento
        self.name=TextField(label="Digite o seu nome")
        self.password = TextField(label="Digite sua senha", password=True)
        self.recoverPassWord=TextButton(text="Recuperar Senha",
                                        style=ButtonStyle(
                                            bgcolor={
                                                     MaterialState.DEFAULT: colors.TRANSPARENT,
                                                     MaterialState.HOVERED:colors.TRANSPARENT},
                                            color={
                                                   MaterialState.DEFAULT: "#65469b",
                                                   MaterialState.HOVERED:"#7e57c2"}
                                        ))
        self.iconGoogle=Image(src="icons/google.png")
        self.btn_enter=ElevatedButton("Entrar",
                                expand=True,
                                 style=ButtonStyle(
                                     bgcolor={MaterialState.DEFAULT:"#65469b",
                                              MaterialState.HOVERED:"#7e57c2"},
                                     shape={
                                        MaterialState.DEFAULT: RoundedRectangleBorder(radius=0)

                                    },
                                     color="#ffffff"
                                 ),

                                 on_click=lambda  e: self.evento.go("/menu"),

                                 )

    def build(self):

        img_top=Image("img_login.png")
        lineBntRegister=Row(col={"xs": 6,"sm":2,"md":3},controls=[self.btn_enter])
        lineIcons=Row(controls=[self.iconGoogle, self.recoverPassWord],alignment=MainAxisAlignment.SPACE_AROUND)
        line_img = ResponsiveRow([

                        Column(col={"xs": 10, "sm":8, "md":6,"lg":4}, controls=[

                            Column(col={"xs": 6,"sm":2,"md":3}, controls=[img_top],alignment=alignment.center),

                            Column(col={"sm": 12, "md": 8},
                                   controls=[
                                       self.name,
                                       self.password,
                                       lineBntRegister,
                                       lineIcons
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
