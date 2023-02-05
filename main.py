import flet as ft


def main(page: ft.Page):
    page.title = "Flet Counter App"
    page.theme_mode = "light"

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def increment_counter(e):
        """Increments the value of the counter_text object by 1"""
        counter_text.value = str(int(counter_text.value) + 1)
        page.update()

    # the app's FAB
    page.floating_action_button = ft.FloatingActionButton(
        content=ft.Icon(ft.icons.ADD, color=ft.colors.WHITE), shape=ft.CircleBorder(),
        on_click=increment_counter, tooltip="Increment", bgcolor=ft.colors.BLUE
    )

    # the app's appbar
    page.appbar = ft.AppBar(
        title=ft.Text("Flet Demo Home Page", color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE, center_title=True
    )

    # contains the number to be incremented
    counter_text = ft.Text("0", style=ft.TextThemeStyle.DISPLAY_LARGE)

    page.add(
        ft.Column(
            controls=[
                ft.Text("You have pushed the button this many times:"),
                counter_text
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


ft.app(target=main, view=ft.WEB_BROWSER)
