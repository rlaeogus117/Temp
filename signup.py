import flet as ft

def signup_screen(page: ft.Page):
    def back_to_login(e):
        page.go("/login")

    email = ft.TextField(
        hint_text="이메일을 입력하세요.",
        width=page.width * 0.9,
        border_radius=10
    )
    password = ft.TextField(
        hint_text="비밀번호 입력",
        password=True,
        width=page.width * 0.9,
        border_radius=10
    )
    confirm_password = ft.TextField(
        hint_text="비밀번호 확인",
        password=True,
        width=page.width * 0.9,
        border_radius=10
    )
    birth = ft.TextField(
        hint_text="YYYY-MM-DD",
        width=page.width * 0.9,
        border_radius=10
    )

    gender_toggle = ft.SegmentedButton(
        segments=[
            ft.Segment(value="female", label=ft.Text("여성")),
            ft.Segment(value="male", label=ft.Text("남성"))
        ],
        selected=["female"],
        allow_multiple_selection=False,
        width=page.width * 0.9
    )

    # 약관 체크박스들 선언
    terms_all = ft.Checkbox(label="필수약관 모두 동의")
    terms1 = ft.Checkbox(label="(필수) Allert Sign 이용약관")
    terms2 = ft.Checkbox(label="(필수) Allert Sign 개인정보 수집 및 이용에 대한 동의")
    terms3 = ft.Checkbox(label="(필수) Allert Sign 알레르기 정보 제공 및 면책 조항")

    # 전체 약관 체크 상태 변경 시 실행될 함수
    def terms_all_changed(e):
        terms1.value = terms_all.value
        terms2.value = terms_all.value
        terms3.value = terms_all.value
        page.update()

    # 개별 약관 변경 시 전체 체크박스 상태 업데이트
    def update_terms_all_state(e):
        terms_all.value = terms1.value and terms2.value and terms3.value
        page.update()

    # 이벤트 핸들러 연결
    terms_all.on_change = terms_all_changed
    terms1.on_change = update_terms_all_state
    terms2.on_change = update_terms_all_state
    terms3.on_change = update_terms_all_state

    # '보기' 버튼과 함께 Row로 구성
    terms1_row = ft.Row(
        [
            terms1,
            ft.TextButton("보기", on_click=lambda e: page.go("/terms1"))
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    terms2_row = ft.Row(
        [
            terms2,
            ft.TextButton("보기", on_click=lambda e: page.go("/terms2"))
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    terms3_row = ft.Row(
        [
            terms3,
            ft.TextButton("보기", on_click=lambda e: page.go("/terms3"))
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    register_button = ft.ElevatedButton(
        text="다 음",
        bgcolor=ft.Colors.GREEN,
        color=ft.Colors.WHITE,
        width=page.width * 0.9,
        height=50
    )

    return ft.View(
        "/signup",
        controls=[
            ft.AppBar(
                title=ft.Text("회원가입"),
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=back_to_login),
                bgcolor=ft.Colors.WHITE
            ),
            ft.Column(
                [
                    email,
                    password,
                    confirm_password,
                    birth,
                    gender_toggle,
                    ft.Text("ALLERT SIGN", size=14, weight="bold", color=ft.Colors.GREEN),
                    ft.Text("약관동의가 필요해요.", size=16, weight="bold"),
                    terms_all,
                    ft.Container(content=terms1_row, padding=ft.padding.only(left=20)),
                    ft.Container(content=terms2_row, padding=ft.padding.only(left=20)),
                    ft.Container(content=terms3_row, padding=ft.padding.only(left=20)),
                    ft.Container(height=30),
                    register_button
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO
            )
        ]
    )
