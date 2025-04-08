import reflex as rx

class State(rx.State) :
    name : str = ""
    intro : str = ""
    agree : bool = False
    email_notification : bool = False
    
    def set_name(self,value : str) :
        self.name = value
        
    def set_intro(self,value : str) :
        self.intro = value
        
    def set_agree(self,value : bool) :
        self.agree = value
        
    def set_notify(self,value : bool) :
        self.email_notification = value
        
def index() :
    return rx.center(
        rx.vstack(
        rx.heading("👋 이름 입력 연습", size="5"),
        rx.input(
            placeholder = "이름을 입력하세요.",
            on_change = State.set_name
        ),
        rx.text_area(
            placeholder = "자기소개를 입력하세요.",
            on_change = State.set_intro
        ),
        rx.checkbox(
            "약관에 동의합니다.",
            on_change = State.set_agree
        ),
        rx.switch("이메일 수신 받기",
                  on_change = State.set_notify),
        rx.text(State.name),
        rx.text(State.intro),
        rx.text(State.agree),
        rx.cond(
            State.email_notification,
            rx.text("📨"),
            rx.text("❌")
        )
        ),
        height = "100vh",
        width = "100vm"
    )