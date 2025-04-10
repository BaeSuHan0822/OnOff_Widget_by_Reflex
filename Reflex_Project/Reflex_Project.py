import reflex as rx
from week01 import text_practice,button_practice,input_practice,radio_practice,total_practice,checkbox_practice,switch_practice

app = rx.App()
app.add_page(text_practice.index,route = "/text")
app.add_page(button_practice.index,route = "/button")
app.add_page(input_practice.index,route = "/input")
app.add_page(radio_practice.index,route = "/radio")
app.add_page(total_practice.index,route = "/total")
app.add_page(checkbox_practice.index,route = "/checkbox")
app.add_page(switch_practice.index,route = "/switch")
# control + c : Reflex stop