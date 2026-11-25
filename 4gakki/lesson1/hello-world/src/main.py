import flet as ft


def main(page: ft.Page):


    hello_world = ft.Text('Hello_World',size=69)

    counter = ft.Text("0", size=50, data=0)

    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.value = str(counter.data)

    def subtractin_click(b:ft.Event[ft.FloatingActionButton]):
        counter.data -= 1
        counter.value = str(counter.data)

    page.floating_action_button = ft.Row([ft.FloatingActionButton(
        icon=ft.Icons.ADD, key="increment", on_click=increment_click , 
    ),
    
    ft.FloatingActionButton(icon=ft.Icons.REMOVE, key="decrement", on_click=subtractin_click, 
         )])
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(

                content=ft.Row(controls=[hello_world,counter],
                alignment=ft.MainAxisAlignment.CENTER),

                alignment=ft.Alignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
