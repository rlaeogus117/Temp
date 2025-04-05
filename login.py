import flet as ft
import time

def splash_screen(page: ft.Page):
    page.title = "ALLERT SIGN"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.WHITE

    logo = ft.Image(
        src="https://raw.githubusercontent.com/rlaeogus117/Temp/main/login_image.png",
        width=300,  # 2배 확대
        height=300
    )

    description = ft.Text(
        "당신의 알러지를 등록하고\n지금부터 관리해보세요!!",
        size=16,
        text_align=ft.TextAlign.CENTER,
        opacity=1.0
    )

    splash_view = ft.Column(
        [
            logo,
            ft.Container(height=10),
            description
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(splash_view)
    page.update()

    time.sleep(1.5)
    description.opacity = 0.0
    page.update()

    time.sleep(0.5)
    login_screen(page)

def login_screen(page: ft.Page):
    page.clean()

    logo = ft.Image(
        src="https://raw.githubusercontent.com/rlaeogus117/Temp/main/login_image.png",
        width=300,
        height=300
    )

    email_input = ft.TextField(label="이메일 주소", width=page.width * 0.8)
    password_input = ft.TextField(label="비밀번호", password=True, width=page.width * 0.8)

    login_button = ft.ElevatedButton(
        text="로그인",
        bgcolor=ft.colors.GREEN,
        color=ft.colors.WHITE,
        width=page.width * 0.8
    )

    forgot_password = ft.TextButton(
        "비밀번호가 생각나지 않으신가요?",
        on_click=lambda e: page.go("/find-password")
    )

    signup_text = ft.Text("Allert Sign이 처음이신가요?")
    signup_link = ft.TextButton(
        "회원가입",
        style=ft.ButtonStyle(color=ft.colors.GREEN),
        on_click=lambda e: page.go("/signup")
    )

    signup_row = ft.Row(
        [signup_text, signup_link],
        alignment=ft.MainAxisAlignment.CENTER
    )

    login_view = ft.Column(
        [
            ft.Column(  # 로그인 관련 위쪽 부분
                [
                    logo,
                    email_input,
                    password_input,
                    login_button,
                    forgot_password,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Container(height=30),  # 중간 공백
            ft.Container(
                content=signup_row,
                alignment=ft.alignment.bottom_center,
                padding=10
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # 위/아래로 분배
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(login_view)
    page.update()

def main(page: ft.Page):
    splash_screen(page)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
