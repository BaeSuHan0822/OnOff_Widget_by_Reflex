'''
🎯 퀴즈 미션: 슬라이더 기반 난이도 표시기

사용자가 0부터 100까지 조절할 수 있는 슬라이더를 움직인다.
슬라이더 값에 따라 아래 문구가 조건적으로 변한다:
0 ~ 30: "😌 쉬운 문제"
31 ~ 70: "🤔 보통 문제"
71 ~ 100: "🔥 어려운 문제"
화면 정중앙에 배치하고 보기 좋게 정렬!
⛳️ 제한 사항
rx.slider, rx.text, rx.cond, rx.State, rx.event, rx.var 등을 적절히 써야 함.
slider는 상태로 연결되어야 함 (State 내에서 관리)
조건 분기는 State 내부에서 분기 처리해도 되고, rx.cond를 중첩해도 됨 (네 스타일대로!)
'''

import reflex as rx

class State(rx.State) :
    level : list[int] = [0]
    difficulty : str = ""
    
    @rx.event
    def set_level(self,item : list[int | float]) :
        self.level = item
    
    @rx.var
    def set_difficulty(self) -> str :
        if 0 <= self.level[0] <= 30 :
            return "low"
        elif 31 <= self.level[0] <= 70 :
            return "middle"
        else :
            return "high"
    
        
def index() :
    return rx.center(
        rx.vstack(
            rx.slider(
                min = 0,
                max = 100,
                step = 1,
                default_value = 50,
                on_change = State.set_level,
                width = "300px"
            ),
            rx.cond(
                State.set_difficulty == "low",
                rx.text(
                    "😌 쉬운 문제",
                    font_size = "50px",
                    font_weight = "bold",
                    text_align = "center"
                ),
                rx.cond(
                    State.set_difficulty == "middle",
                    rx.text(
                        "🤔 보통 문제",
                        font_size = "50px",
                        font_weight = "bold",
                        text_align = "center"
                    ),
                    rx.text(
                        "🔥 어려운 문제",
                        font_size = "50px",
                        font_weight = "bold",
                        text_align = "center"
                    )
                )
            )
        ),
        height = "100vh",
        width = "100vw"
    )
