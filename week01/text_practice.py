import reflex as rx


class State(rx.State) :
    count = 0
    
    def increase(self) :
        self.count += 1
    
    def decrease(self) :
        self.count -= 1
    
def index() :
    return rx.center(
        rx.hstack(
            rx.text(
                "증가시키기",
                font_size = "30px",
                font_weight = "bold",
                text_align = "center",
                on_click = State.increase),
            rx.text(State.count,
                    font_size = "50px",
                    font_weight = "bold",
                    text_align = "center"),
            rx.text("감소시키기",
                    font_size = "30px",
                    font_weight = "bold",
                    text_align = "center",
                    on_click = State.decrease)
        ),
    height = "100vh",         # vh: 뷰포트 높이의 1% (100vh는 화면 세로 전체)
    width = "100vw"           # vw: 뷰포트 너비의 1% (100vw는 화면 가로 전체)
    )