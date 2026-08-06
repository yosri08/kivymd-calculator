from kivy.lang import Builder
from kivymd.app import MDApp
KV = """
MDLabel:
    font_name: "NotoSansMath-Regular.ttf"
    text: "   ∫ → ∞ ≤ ≥ ≠ π hello world 123456AAbbCهايCç"
    
    
    """
    
class app(MDApp):
    def build(self):
        return Builder.load_string(KV)
        
app().run()