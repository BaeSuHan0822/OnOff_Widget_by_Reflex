import reflex as rx
from week01 import text_practice,button_practice

app = rx.App()
app.add_page(text_practice.index,route = "/text")
app.add_page(button_practice.index,route = "/button")
# control + c : Reflex stop