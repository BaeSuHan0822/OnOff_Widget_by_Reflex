'''
🎯 요구사항 (퀴즈 스타일)

너는 지금 할 일 목록 미니앱을 만든다.

📝 기본적으로 할 일 3개가 자동으로 리스트에 들어있어야 한다.
📃 할 일 리스트는 화면에 한 줄씩 표시된다.
❌ 할 일이 하나도 없을 경우, 대신 "오늘은 쉴 수 있어요! ☕️" 라는 메시지가 가운데에 떠야 한다.
✅ 반복 렌더링과 조건 렌더링을 적절히 함께 사용해야 한다.
'''
import reflex as rx

class State(rx.State) :
    todo_list : list[str] = ["공부하기","밥 먹기", "확랜 복습하기"]
    

def index() :
    return rx.center(
        rx.vstack(
            rx.heading("📝 오늘의 할 일", size="5"),
            
            rx.cond(
                State.todo_list,
                rx.foreach(
                    State.todo_list,
                    lambda item : rx.text(item)
                ),
                rx.text("오늘은 쉴 수 있어요! ☕️")
            )
        ),
        height = "100vh",
        width = "100vw"
    )