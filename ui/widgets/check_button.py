
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import (StringProperty, ColorProperty)
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.lang import Builder





Builder.load_string(
"""
<CheckButton>: 
    radius: dp(15)
    adaptive_height:True
    orientation: "horizontal"
    padding: dp(10),0
    MDIcon:
        icon:root.icon
        pos_hint:{"center_y":0.5}
        size_hint:None,None
        size:"55dp","55dp"
    MDLabel: 
        text:root.text 
        adaptive_height:True 
        font_size:"20sp" 
        padding: dp(30),0
        pos_hint:{"center_y":0.5} 
    
    MDCheckbox:
        id:checkbox
        size_hint:None,None
        size:"48dp","48dp"
        pos_hint:{"center_y":0.5}
        color_active: self.theme_cls.primary_color
        color_inactive: self.theme_cls.primary_color
        disabled: True
        disabled_color: self.theme_cls.primary_color
"""
)

class CheckButton(RectangularRippleBehavior,                              ButtonBehavior, 
                  MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()