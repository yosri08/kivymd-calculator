
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import CommonElevationBehavior

from logic.calculus_calculator import CalculusCalculatorLogic



Builder.load_string(
"""
<DerivativeWidget>:
    elevation: 3
    orientation: "vertical"
    size_hint_x: 1
    padding: dp(15)
    adaptive_height: True
    radius: dp(10)
    md_bg_color: app.theme_manager.theme_style["card_bg_color"]
    spacing: dp(10)
    
    
    MDLabel:
        adaptive_height: True
        text: "Derivative"
        halign: "left"
        font_name: "assets/fonts/NotoSansMath-Regular.ttf"
        font_size: "22sp"
        bold: True
        
        
    MDBoxLayout:
        adaptive_height: True
        orientation: "horizontal"
        spacing: dp(15)
        
        MDLabel:
            text: "Expression"
            font_name: "assets/fonts/NotoSansMath-Regular.ttf"
            font_size: "25sp"
            adaptive_size: True
            valign: "top"
            
        MDTextField:
            id: expression
            hint_text: "Enter Expression here..."
            
    MDBoxLayout:
        adaptive_height: True
        orientation: "horizontal"
        spacing: dp(15)
        
        MDLabel:
            text: "Point"
            font_name: "assets/fonts/NotoSansMath-Regular.ttf"
            font_size: "30sp"
            adaptive_size: True
            valign: "top"
            
        MDTextField:
            id: point
            hint_text: "Enter point here... (optional)"
            
            
    MDFillRoundFlatButton:
        text: "Calculate"
        pos_hint: {"center_x": 0.5}
        font_name: "assets/fonts/NotoSansMath-Regular.ttf"
        font_size: "30sp"
        md_bg_color: self.theme_cls.primary_color
        on_press: root.calculate_derivative()
        
        
    MDLabel:
        id: derivative_label
        halign: "center"
        font_name: "assets/fonts/NotoSansMath-Regular.ttf"
        adaptive_height: True
        font_size: "30sp"

    MDLabel:
        id: slope_label
        halign: "center"
        font_name: "assets/fonts/NotoSansMath-Regular.ttf"
        adaptive_height: True
        font_size: "30sp"
        

"""
)

class DerivativeWidget(CommonElevationBehavior,MDBoxLayout):
    helper = CalculusCalculatorLogic()
    
    def calculate_derivative(self):
        expression = self.ids.expression.text
        point = self.ids.point.text
        
        derivative_label = self.ids.derivative_label
        slope_label = self.ids.slope_label
        
        derivative_label.text = ""
        slope_label.text = ""
        
        
        if not expression:
            derivative_label.text = "Expression can't be empty"
        result = self.helper.differentiate(expression)
        derivative_label.text = result
        if point:
            
            if not self.is_number(point):
                slope_label.text = "Point must be a number"
                return
            slope = self.helper.evaluate(result, float(point))
            slope_label.text = f"Slope at x = {point}: {slope}"

    def is_number(self, num: str) -> bool:
        try:
            x = float(num)
            return True
        except ValueError:
            return False