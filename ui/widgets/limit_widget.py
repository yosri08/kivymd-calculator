from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import CommonElevationBehavior

from logic.calculus_calculator import CalculusCalculatorLogic

Builder.load_string("""
<LimitWidget>:
    elevation: 3
    orientation: "vertical"
    size_hint_x: 1
    padding: dp(15)
    adaptive_height: True
    radius: dp(10)
    md_bg_color: "#AA77AA"
    spacing: dp(10)
    
    
    MDLabel:
        adaptive_height: True
        text: "Limit"
        halign: "left"
        font_name: "assets/fonts/NotoSansMath-Regular.ttf"
        font_size: "22sp"
        bold: True
        
        
    MDBoxLayout:
        adaptive_height: True
        orientation: "horizontal"
        spacing: dp(15)
        MDLabel:
            text: "x →"
            font_name: "assets/fonts/NotoSansMath-Regular.ttf"
            font_size: "30sp"
            adaptive_size: True
            valign: "center"
            
        MDTextField:
            id: point
            hint_text: "Enter point here..."
            size_hint_x: None
            width: dp(100)

    MDBoxLayout:
        adaptive_height: True
        orientation: "horizontal"
        spacing: dp(15)
        MDLabel:
            text: "Expression"
            font_name: "assets/fonts/NotoSansMath-Regular.ttf"
            font_size: "30sp"
            adaptive_size: True

        MDTextField:
            id: expression
            hint_text: "Enter expression here..."
            font_size: "25sp"

    MDFillRoundFlatButton:
        text: "Calculate"
        pos_hint: {"center_x": 0.5}
        font_name: "assets/fonts/NotoSansMath-Regular.ttf"
        font_size: "30sp"
        md_bg_color: self.theme_cls.primary_color
        on_press: root.calculate_limit()
    MDLabel:
        id: result
        halign: "center"
        font_name: "assets/fonts/NotoSansMath-Regular.ttf"
        font_size: "30sp"
        adaptive_height: True
    
"""
)

class LimitWidget(CommonElevationBehavior,MDBoxLayout):
    helper = CalculusCalculatorLogic()
    
    def calculate_limit(self):
        expression = self.ids.expression.text
        point = self.ids.point.text
        result_label = self.ids.result
        
        if (not expression) or (not point):
            result_label.text = "Make sure both expression and point are entered"
            return

        result = self.helper.limit(expression, point)
        result_label.text = f"result: {result}"
            
            
            