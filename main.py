from kivymd.app import MDApp
from kivy.lang import Builder





class CalculatorApp(MDApp):
    
    def build(self):
        return Builder.load_file("ui/main.kv")
        
    def on_start(self):
        self.root.current = "calculus_screen"
        self.main_screen = self.root.get_screen("main_screen")
        self.calculator_screen = self.root.get_screen("calculator_screen")
        self.scientific_screen = self.root.get_screen("scientific_screen")
        
        
    def darken(self):
        factor = 0.8
        color = self.theme_cls.primary_color
        return [c * factor for c in color[:4]]
        
    def darken2(self):
        factor = 0.5
        color = self.theme_cls.primary_color
        return [c * factor for c in color[:4]]
if __name__ == "__main__":
    CalculatorApp().run()