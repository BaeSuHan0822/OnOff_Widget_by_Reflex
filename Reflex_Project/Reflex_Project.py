import reflex as rx
from week01 import text_practice,button_practice,input_practice

app = rx.App()
app.add_page(text_practice.index,route = "/text")
app.add_page(button_practice.index,route = "/button")
app.add_page(input_practice.index,route = "/input")
# control + c : Reflex stop