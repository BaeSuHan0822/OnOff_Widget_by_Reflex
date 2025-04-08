import reflex as rx

class State(rx.State):
    name: str = ""
    introduction: str = ""
    language: str = ""
    submit: bool = False

    def clear_state(self):
        self.name = ""
        self.introduction = ""
        self.language = ""
        self.submit = False

    def set_name(self, value: str):
        self.name = value

    def set_introduction(self, value: str):
        self.introduction = value

    def set_language(self, value: str):
        self.language = value

    def set_submit(self):
        self.submit = True

def index():
    return rx.center(
            rx.vstack(
                rx.input(
                    placeholder="이름을 입력하세요 !",
                    on_change=State.set_name
                ),
                rx.text_area(
                    placeholder="자기소개서를 작성하세요 !",
                    on_change=State.set_introduction
                ),
                rx.radio(
                    items=["Python", "C++", "GO", "SQL"],
                    on_change=State.set_language
                ),
                rx.button(
                    "제출하기",
                    color="white",
                    bg="black",
                    size="3",
                    variant="surface",
                    radius="large",
                    on_click=State.set_submit
                ),
                rx.cond(
                    State.submit,
                    rx.center(
                        rx.vstack(
                            rx.text(
                                State.name,
                                font_size="50px",
                                font_weight="bold"
                            ),
                            rx.text(
                                State.introduction,
                                font_size="30px",
                                font_weight="bold"
                            ),
                            rx.text(
                                State.language,
                                font_size="30px",
                                font_weight="bold"
                            )
                        )
                    )
                )
            ),
            height="100vh",
            align_items="center",
            justify_content="center"
        )
