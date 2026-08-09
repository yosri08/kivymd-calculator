from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ColorProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.lang import Builder

Builder.load_string(
"""
<ThemeButton>:
    size_hint: None,None
    size: dp(40), dp(40)
    md_bg_color: root.bg_color
    radius: dp(7)
    on_press: app.settings_screen.change_theme_color(self.theme)
    MDIcon:
        id: _icon
        font_size: "35sp"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        icon: ""
<ThemeSelectionWidget>:
    radius: dp(15)
    adaptive_height: True
    padding: dp(10),dp(5)
    spacing: dp(5)
    orientation: "horizontal"
    MDIcon:
        icon: "format-color-fill"
        pos_hint: {"center_y":0.5}
        size_hint: None, None
        size: "48dp", "48dp"
        font_size: "30sp"
        
    MDLabel:
        text: "Theme Color"
        adaptive_height:True 
        font_size:"20sp" 
        padding: dp(15),0
        pos_hint:{"center_y":0.5}
        
    ThemeButton:
        bg_color: "#4b0082"
        theme: "Indigo"
    ThemeButton:
        bg_color: "#008080"
        theme: "Teal"
    ThemeButton:
        bg_color: "#ffbf00"
        theme: "Amber"
    ThemeButton:
        bg_color: "#0000ff"
        theme: "Blue"
""")

class ThemeButton(RectangularRippleBehavior,
                  ButtonBehavior,
                  MDBoxLayout):
    bg_color = ColorProperty()
    
class ThemeSelectionWidget(MDBoxLayout):
    pass