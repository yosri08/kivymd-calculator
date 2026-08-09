from kivy.properties import DictProperty
from kivy.event import EventDispatcher

class ThemeManager(EventDispatcher):  
      
    THEME_COLORS = {  
        "Indigo": {
            "dark": "#818CF8",
            "light": "#4F46E5"
        },  
        "Teal": {
            "dark": "#2DD4BF",
            "light": "#0F766E"
        },  
        "Amber": {
            "dark": "#FBBF24",
            "light": "#B45309"
        },  
        "Blue": {
            "dark": "#60A5FA",
            "light": "#2563EB"
        }  
    }  
          
    THEME_STYLES = {  
        "Light": {
            "bg_color": "#F8FAFC",
            "card_bg_color": "#FFFFFF",
            "surface_bg_color": "#F1F5F9"
        },  
        "Dark": {
            "bg_color": "#020617",
            "card_bg_color": "#0F172A",
            "surface_bg_color": "#1E293B" 
        }  
    }  
    
    theme_color = DictProperty()
    theme_style = DictProperty()
    def __init__(self, app, **kwargs):  
        super().__init__(**kwargs)
        self.app = app
        # app starts with light mode and blue theme color
        self.theme_color = self.THEME_COLORS["Blue"]
        self.theme_style = self.THEME_STYLES["Light"]
        
    def change_theme_color(self, theme):
        self.app.theme_cls.primary_palette = theme
        self.theme_color = self.THEME_COLORS[theme]
        
    def change_theme_style(self, theme):
        self.app.theme_cls.theme_style = theme
        self.theme_style = self.THEME_STYLES[theme]
        
        