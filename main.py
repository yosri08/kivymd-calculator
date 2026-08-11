from kivymd.app import MDApp
from kivy.lang import Builder

from utils.theme_manager import ThemeManager




class CalculatorApp(MDApp):
    
    def build(self):
        
        self.theme_manager = ThemeManager(self)
        self.theme_cls.accent_palette = "Gray"
        return Builder.load_file("ui/main.kv")
        
    def on_start(self):
        self.root.current = "gcf_lcm_screen"
        self.main_screen = self.root.get_screen("main_screen")
        self.calculator_screen = self.root.get_screen("calculator_screen")
        self.scientific_screen = self.root.get_screen("scientific_screen")
        self.settings_screen = self.root.get_screen("settings_screen")
        self.gcf_lcm_screen = self.root.get_screen("gcf_lcm_screen")
        
        
    
if __name__ == "__main__":
    CalculatorApp().run()