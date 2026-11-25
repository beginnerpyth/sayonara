
from dataclasses import field

import flet as ft


@ft.control
class CalcButton(ft.Button):
    expand: int = field(default_factory=lambda: 1)


@ft.control
class DigitButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.WHITE_24
    color: ft.Colors = ft.Colors.WHITE


@ft.control
class ActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.ORANGE
    color: ft.Colors = ft.Colors.WHITE


@ft.control
class ExtraActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
    color: ft.Colors = ft.Colors.BLACK


@ft.control
class CalcApp(ft.Container):
    def init(self):
        self.reset()
        self.width = 1250
        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.BorderRadius.all(40)
        self.padding = 20
        self.result = ft.Text(value="0", size=40, color=ft.Colors.WHITE)
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment=ft.MainAxisAlignment.END),
                ft.Row(
                    controls=[
                        ExtraActionButton(content="AC"),
                        ExtraActionButton(content="+/-"),
                        ExtraActionButton(content="%"),
                        ActionButton(content="/"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="7"),
                        DigitButton(content="8"),
                        DigitButton(content="9"),
                        ActionButton(content="*"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="4"),
                        DigitButton(content="5"),
                        DigitButton(content="6"),
                        ActionButton(content="-"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="1"),
                        DigitButton(content="2"),
                        DigitButton(content="3"),
                        ActionButton(content="+"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="0", expand=2),
                        DigitButton(content="."),
                        ActionButton(content="="),
                    ]
                ),
            ]
        )

    def reset(self):
        hogehoge = 0


def main(page: ft.Page):
    page.title = "Apple calculator"

    calc = CalcApp()

    page.add(calc)


if __name__ == "__main__":
    ft.run(main)
	