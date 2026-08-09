
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.lang import Builder

Builder.load_string(
"""
<LongButton>:
    radius: dp(15)
    size_hint_y: None
    size: 0, dp(48)
    padding: dp(10),dp(5)
    spacing: dp(5)
    orientation: "horizontal"
    MDIcon:
        icon: root.icon
        pos_hint: {"center_y":0.5}
        size_hint: None, None
        size: "48dp", "48dp"
        font_size: "30sp"
        
    MDLabel:
        text: root.text
        adaptive_height:True 
        font_size:"20sp" 
        padding: dp(15),0
        pos_hint:{"center_y":0.5}
"""
)

class LongButton(RectangularRippleBehavior,
                 ButtonBehavior, 
                 MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()