import reflex as rx

class State(rx.State) :
    dark_mode : bool = True
    
    @rx.event
    def make_dark(self,checked : bool) :
        self.dark_mode = checked
        
    @rx.var
    def mode_text(self) -> str :
        return "🌙" if self.dark_mode else "☀️"
        
    @rx.var
    def mode_bg(self) -> str :
        return "white" if not self.dark_mode else "black"
    
    
def index() :
    return rx.center(
        rx.vstack(
            rx.switch(
                "Dark mode",
                on_change = State.make_dark,
                default_checked = False
            ),
            rx.text(
                State.mode_text, 
                font_size = "50px",
                font_weight = "bold",
                style = {
                "position" : "absolute",
                "top" : "0px",
                "left" : "0px"
                },
                ),
            ),
        bg = State.mode_bg,
        color = rx.cond(
            State.dark_mode,
            "black",
            "white"
        ),
        height = "100vh",
        width = "100vw"
    )