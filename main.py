from kivymd.app import MDApp
from kivy.lang import Builder


from ui.main_screen import MainScreen
from ui.calculator_screen import CalculatorScreen

class CalculatorApp(MDApp):
    
    def build(self):
        return Builder.load_file("ui/main.kv")
        
    def on_start(self):
        
        self.root.current = "calculator_screen"
        
    def darken(self):
        factor = 0.7
        color = self.theme_cls.primary_color
        return [c * factor for c in color[:4]]
if __name__ == "__main__":
    CalculatorApp().run()