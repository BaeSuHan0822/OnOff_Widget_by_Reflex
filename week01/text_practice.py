import reflex as rx

def index() :
    return rx.text(
        "안녕하세요 Reflex입니다.",
        font_size = "20",
        color = "blue",
        font_weight = "900",
        text_align = "center",
        
    )