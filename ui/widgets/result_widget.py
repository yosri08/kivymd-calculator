
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

       
Builder.load_string(
"""       
<ResultWidget>:
    orientation: "horizontal"
    size_hint_y: None
    height: dp(75)
    radius: dp(10)
    spacing: dp(5)
    padding: dp(5)
    md_bg_color: app.theme_manager.theme_color["light"]
    MDIcon:
        icon: root.icon
        padding: dp(15),0
        adaptive_size: True
        font_size: "35sp"
        pos_hint: {"center_y":0.5}
    MDLabel:
        id: left_text
        adaptive_height: True
        text: root.left_text
        font_size: "30sp"
        halign: "left"
        pos_hint: {"center_y":0.5}
    MDLabel:
        id: right_text
        adaptive_height: True
        text: root.right_text
        font_size: "30sp"
        halign: "right"
        pos_hint: {"center_y":0.5}
"""
)

class ResultWidget(MDBoxLayout):
    icon = StringProperty()
    left_text = StringProperty()
    right_text = StringProperty()