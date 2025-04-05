# main.py

import flet as ft
from login import splash_screen
from signup import signup_screen

def main(page: ft.Page):
    page.title = "ALLERT SIGN"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.WHITE

    # 📌 페이지 경로가 바뀔 때마다 해당 뷰 불러오는 함수
    def route_change(e):
        page.views.clear()  # 기존 화면 제거

        if page.route == "/signup":
            signup_screen(page)
        else:
            splash_screen(page)

    # 📌 라우트 변경 감지 연결
    page.on_route_change = route_change

    # 📌 앱 시작 시 splash → login 화면으로 자동 이동
    page.go("/")

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
