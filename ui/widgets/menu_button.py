from kivymd.uix.widget import MDWidget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior


Builder.load_string("""
<MenuButton>:
    orientation: "vertical"
    size_hint: None,None
    size: dp(125), dp(125)
    md_bg_color: self.theme_cls.primary_color
    spacing: dp(5)
    padding: dp(10)
    radius: dp(7)
    
    MDIcon:
        pos_hint: {"center_x": 0.5}
        font_size: "75sp"
        icon: root.icon
        
    MDLabel:
        halign: "center"
        size_hint: 1, None
        font_size: "25sp"
        text: root.text
""")


class MenuButton(RectangularRippleBehavior,
                 ButtonBehavior,
                 MDBoxLayout):
                     
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    icon = StringProperty()
    text = StringProperty()