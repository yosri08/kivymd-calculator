from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.pickers import MDDatePicker

Builder.load_string(
"""
#: import datetime datetime
<CustomDatePicker>:
    md_bg_color: app.theme_manager.theme_color['light']
    orientation: "horizontal"
    size_hint: 1, None
    height: dp(90)
    spacing: dp(25)
    padding: dp(25)
    radius: dp(7)
    MDIcon:
        pos_hint: {"center_y":0.5}
        icon: "calendar-month"
        font_size: "60sp"
        adaptive_size: True
    MDLabel:
        id: date_label
        pos_hint: {"center_y":0.5}
        font_size: "30sp"
        adaptive_size: True
        text: datetime.date.today().strftime("%B %d,%Y")
"""
)

class CustomDatePicker(RectangularRippleBehavior,
                       ButtonBehavior, 
                       MDBoxLayout):
    def on_press(self):
        print("hello world")
        picker = MDDatePicker()
        picker.bind(on_save=self.on_date_selected)
        picker.open()

    def on_date_selected(self, instance, value, date_range):
        self.ids.date_label.text = value.strftime("%B %d, %Y")
        app = MDApp.get_running_app()
        app.age_calculator_screen.calculate_age(value)