from UI import ui

@ui.route('/')
def home():
    return "Hello, World!"