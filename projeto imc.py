import flet as ft

def main(page: ft.Page):
    page.title = "🎓 Galeria de Alunos"
    page.bgcolor = "#f4f4f4"
    page.scroll = "auto"

    alunos = [
        {"nome": "Ana Clara", "curso": "Engenharia de Software", "foto": "https://i.pravatar.cc/150?img=1"},
        {"nome": "João Pedro", "curso": "Ciência da Computação", "foto": "https://i.pravatar.cc/150?img=2"},
        {"nome": "Mariana Silva", "curso": "Design Digital", "foto": "https://i.pravatar.cc/150?img=3"},
        {"nome": "Lucas Almeida", "curso": "Sistemas de Informação", "foto": "https://i.pravatar.cc/150?img=4"},
    ]

    cards = []
    for aluno in alunos:
        card = ft.Card(
            content=ft.Container(
                width=220,
                padding=10,
                bgcolor="white",
                border_radius=10,
                content=ft.Column(
                    controls=[
                        ft.Image(src=aluno["foto"], width=200, height=200, border_radius=10),
                        ft.Text(aluno["nome"], size=16, weight="bold", color="#1e88e5"),
                        ft.Text(aluno["curso"], size=14, color="#555"),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        )
        cards.append(card)

    page.add(
        ft.Column(
            [
                ft.Text("🎓 Galeria de Alunos", size=26, weight="bold", color="#333"),
                ft.Row(cards, wrap=True, alignment=ft.MainAxisAlignment.CENTER, spacing=20)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)