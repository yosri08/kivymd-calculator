from kivymd.app import MDApp
from kivy.lang import Builder


from ui.main_screen import MainScreen


class CalculatorApp(MDApp):
    
    def build(self):
        return Builder.load_file("ui/main.kv")
        
        
if __name__ == "__main__":
    CalculatorApp().run()