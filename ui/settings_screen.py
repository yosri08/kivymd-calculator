from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

from ui.widgets.theme_selection_widget import ThemeButton

class SettingsScreen(MDScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
    
    
    def change_theme_style(self, button):
     
        if self.app.theme_cls.theme_style == "Dark":
            self.app.theme_manager.change_theme_style("Light")
        else:
            self.app.theme_manager.change_theme_style("Dark")
            
        button.ids.checkbox.active = not button.ids.checkbox.active
        button.ids.checkbox.disabled_color = self.app.theme_cls.primary_color
        
        
    def change_theme_color(self, color):
        print(f"change theme color activated by {color}")
       # self.app.theme_manager.change_theme_color(color)
        if self.app.theme_cls.primary_palette != color:
            self.app.theme_manager.change_theme_color(color)
            container = self.ids.buttons_container
            for button in container.children:
                if isinstance(button, ThemeButton):
                    if button.theme == color:
                        button.ids._icon.icon = "check"
                    else:
                        button.ids._icon.icon = ""
            
        
        