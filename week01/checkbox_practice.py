import reflex as rx

class State(rx.State) :
    selected : list[str] = []
    
    @rx.event
    def toggle_item(self,item : str, checked : bool) :
        if checked : 
            self.selected.append(item)
        else :
            self.selected.remove(item)
            
    @rx.var
    def return_text(self) -> str:
        return ",".join(self.selected) if self.selected else "선택된 언어가 없음"
    
def index() :
    items = ["Python","JavaScript","Go","SQL"]
    
    return rx.vstack(
            *[
                rx.checkbox(
                    item,
                    on_change = State.toggle_item(item)
                )
                for item in items
            ],
            rx.text(State.return_text),
        height = "100vh",
        width = "100vw"
    )