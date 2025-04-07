import reflex as rx
from week01 import text_practice

app = rx.App()
app.add_page(text_practice.index,route = "/text")

app._compile()
