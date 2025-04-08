import reflex as rx

class State(rx.State) :
    choice : str = ""
    
    def set_choice(self,value : str) :
        self.choice = value
        
def index():
    return rx.center(
        rx.vstack(
        rx.heading("🎛️ 라디오 버튼 예제"),
        rx.radio(
            items = ["Python","JavaScript","Go"],
            on_change = State.set_choice
        ),
        rx.text(
            rx.cond(
                State.choice == "Python",
                rx.text("파이썬 최고 !🥰"),
                rx.cond(
                    State.choice == "JavaScript",
                    rx.text("자바스크립트가 최고 !😍"),
                    rx.text("Go가 최고지 !😃")
                )
            )
        )
        ),
        height = "100vh",
        width = "100vm"
    )