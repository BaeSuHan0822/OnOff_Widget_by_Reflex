import reflex as rx

class State(rx.State) :
    count = 0
    
    def increase(self) :
        self.count += 1
        
    def decrease(self) :
        self.count -= 1
        
def index():
    return rx.center(
        rx.button(
            "Decrease",
            color = "white",
            bg = "red",
            size = "3",
            variant = "soft",
            radius = "large",
            on_click = State.decrease
        ),
        rx.text(f"Clicked : {State.count}",
                font_size = "50px",
                font_weight = "bold",
                ),
        rx.button(
            "Increase",
            color = "white",
            bg = "blue",
            size = "3",
            variant = "soft",
            radius = "large",
            on_click = State.increase),
        height = "100vh",
        width = "100vm"
    )