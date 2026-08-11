
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

       
Builder.load_string(
"""       
<ResultWidget>:
    orientation: "horizontal"
    adaptive_height: True
    radius: dp(10)
    spacing: dp(5)
    padding: dp(5)
    md_bg_color: app.theme_manager.theme_color["light"]
    MDIcon:
        icon: root.icon
        adaptive_size: True
        font_size: "35sp"
        pos_hint: {"center_y":0.5}
    MDLabel:
        id: left_text
        adaptive_height: True
        text: root.left_text
        font_size: "40sp"
        halign: "left"
    MDLabel:
        id: right_text
        adaptive_height: True
        text: root.right_text
        font_size: "40sp"
        halign: "right"
"""
)

class ResultWidget(MDBoxLayout):
    icon = StringProperty()
    left_text = StringProperty()
    right_text = StringProperty()