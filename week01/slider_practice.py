import reflex as rx

class State(rx.State) :
    volume : list= [50]
    
    @rx.event
    def set_volume(self,item : list[int | float]) :
        self.volume = item
        
def index() :
    return rx.center(
        rx.vstack(
        rx.slider(
            min = 0,
            max = 100,
            step = 1,
            default_value = 50,
            on_change = State.set_volume,
            width = "300px"
        ),
        rx.text(State.volume,
                width = "300px",
                text_align = "center"),
        ),
    height = "100vh",
    width = "100vw"
    )
