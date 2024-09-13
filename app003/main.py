import flet as ft


def main(page: ft.Page):
    def main(page: ft.Page):
        page.title="Suma de dos números",
        page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
        page.vertical_alignment=ft.MainAxisAlignment.CENTER
        page.bgcolor="blue"

    lbl1=ft.Text("Suma de dos números",
                style=ft.TextStyle(size=40,weight="bold"))

    Img1=ft.Image(src="ta bien.jpg",width=200,height=200)

    btnSi=ft.ElevatedButton("Si",
                            color="green",
                            width=100,
                            height=50)

    btnNO=ft.ElevatedButton("No",
                            color="red",
                            width=100,
                            height=50)
    def no(e):
        btnSi.width+=30
        btnNO.height+=10
        page.update()
        
    def Si(e):
        Img1.src="ta mal.jpg"
        page.update()
        
        
        btnSi.on_click=Si
        btnNO.on_click=no
        
        
        
    page.add(
        ft.Column(
            [
                lbl1,
                Img1,
                ft.Row([btnSi,btnNO],
                        alignment=ft.MainAxisAlignment.CENTER,
                        )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )    
    

ft.app(main)