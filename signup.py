# signup.py

import flet as ft

def signup_screen(page: ft.Page):
    def back_to_login(e):
        page.go("/")

    email = ft.TextField(
        hint_text="이메일을 입력하세요.",
        width=page.width * 0.9,
        border_radius=10
    )

    password = ft.TextField(
        hint_text="비밀번호 입력",
        password=True,
        width=page.width * 0.9,
        border_radius=10,
        suffix_icon=ft.icons.INFO_OUTLINE
    )

    confirm_password = ft.TextField(
        hint_text="비밀번호 확인",
        width=page.width * 0.9,
        helper_text="비밀번호를 한번 더 입력해주세요.",
        border_radius=10,
        password=True
    )

    birth = ft.TextField(
        hint_text="YYYY-MM-DD",
        width=page.width * 0.9,
        helper_text="EX) 1997-05-23",
        border_radius=10
    )

    gender_toggle = ft.SegmentedButton(
        segments=[
            ft.Segment(text="여성"),
            ft.Segment(text="남성")
        ],
        selected_index=0,
        width=page.width * 0.9
    )

    terms_all = ft.Checkbox(label="필수약관 모두 동의")
    terms_1 = ft.Checkbox(label="(필수) Allert Sign 이용약관")
    terms_2 = ft.Checkbox(label="(필수) Allert Sign 개인정보 수집 및 이용에 대한 동의")
    terms_3 = ft.Checkbox(label="(필수) Allert Sign 위치기반 서비스 이용 동의")

    register_button = ft.ElevatedButton(
        text="다 음",
        bgcolor=ft.colors.GREEN,
        color=ft.colors.WHITE,
        width=page.width * 0.9,
        height=50
    )

    page.views.append(
        ft.View(
            "/signup",
            controls=[
                ft.AppBar(
                    title=ft.Text("회원가입"),
                    leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=back_to_login),
                    bgcolor=ft.colors.WHITE
                ),
                ft.Column(
                    [
                        email,
                        password,
                        confirm_password,
                        birth,
                        gender_toggle,
                        ft.Container(height=20),
                        ft.Text("ALLERT SIGN", size=14, weight="bold", color=ft.colors.GREEN),
                        ft.Text("약관동의가 필요해요.", size=16, weight="bold"),
                        ft.Container(height=10),
                        terms_all,
                        ft.Container(content=terms_1, padding=ft.padding.only(left=20)),
                        ft.Container(content=terms_2, padding=ft.padding.only(left=20)),
                        ft.Container(content=terms_3, padding=ft.padding.only(left=20)),
                        ft.Container(height=30),
                        register_button
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                    expand=True,
                    scroll=ft.ScrollMode.AUTO
                )
            ]
        )
    )
    page.update()
