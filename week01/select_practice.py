import reflex as rx

class State(rx.State) :
    selected_fruit : str = ""
    
    @rx.event
    def fruit(self,value : str) :
        self.selected_fruit = value

def index() :
    return rx.vstack(
        rx.select(
            items = ["사과","바나나","포도"],
            placeholder = "과일을 선택하세요",
            on_change = State.fruit
        ),
        rx.text(f"선택한 과일 : {State.selected_fruit}")
    )