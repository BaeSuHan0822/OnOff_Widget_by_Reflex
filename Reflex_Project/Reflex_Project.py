import reflex as rx
from week01 import text_practice,button_practice,\
    input_practice,radio_practice,total_practice,\
        checkbox_practice,switch_practice,\
            select_practice,slider_practice,todo_list,\
                level
                

app = rx.App()
app.add_page(text_practice.index,route = "/text")
app.add_page(button_practice.index,route = "/button")
app.add_page(input_practice.index,route = "/input")
app.add_page(radio_practice.index,route = "/radio")
app.add_page(total_practice.index,route = "/total")
app.add_page(checkbox_practice.index,route = "/checkbox")
app.add_page(switch_practice.index,route = "/switch")
app.add_page(select_practice.index,route = "/select")
app.add_page(slider_practice.index,route = "/slider")
app.add_page(todo_list.index,route = "/todo")
app.add_page(level.index,route = "/level")
# control + c : Reflex stop