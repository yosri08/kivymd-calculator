from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import (RectangularRippleBehavior, CommonElevationBehavior)
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (StringProperty, ListProperty, ColorProperty)



Builder.load_string("""
<CalcButton>:
    elevation: 0
    MDLabel:
        text: root.text
        halign: "center"
        font_size: root.font_size
""")
class CalcButton(
                RectangularRippleBehavior,
                CommonElevationBehavior,
                ButtonBehavior,
                MDBoxLayout):
    text = StringProperty()
    font_size = StringProperty("25sp")
