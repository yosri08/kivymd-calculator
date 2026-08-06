
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import CommonElevationBehavior

from logic.calculus_calculator import CalculusCalculatorLogic


Builder.load_string(
"""
<IntegralWidget>:
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
        text: "Integral"
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
        spacing: dp(10)
        MDLabel:
            text: "Upper limit"
            font_name: "assets/fonts/NotoSansMath-Regular.ttf"
            font_size: "20sp"
            adaptive_size: True
            
        MDTextField:
            id: upper_limit
            hint_text: "*optional"
        MDSeparator:
            orientation: "vertical"
            
        MDLabel:
            text: "Down limit"
            font_name: "assets/fonts/NotoSansMath-Regular.ttf"
            font_size: "20sp"
            adaptive_size: True
            
        MDTextField:
            id: down_limit
            hint_text: "*optional"
            
            
    MDFillRoundFlatButton:
        text: "Calculate"
        pos_hint: {"center_x": 0.5}
        font_name: "assets/fonts/NotoSansMath-Regular.ttf"
        font_size: "30sp"
        md_bg_color: self.theme_cls.primary_color
        on_press: root.calculate_integral()
        
        
    MDLabel:
        id: result
        halign: "center"
        font_name: "assets/fonts/NotoSansMath-Regular.ttf"
        adaptive_height: True
        font_size: "30sp"
    MDLabel:
        id: area
        halign: "center"
        font_name: "assets/fonts/NotoSansMath-Regular.ttf"
        adaptive_height: True
        font_size: "30sp"
        
""")


class IntegralWidget(CommonElevationBehavior,MDBoxLayout):
    helper = CalculusCalculatorLogic()
    
    def calculate_integral(self):
        expression = self.ids.expression.text
        upper_limit = self.ids.upper_limit.text
        down_limit = self.ids.down_limit.text
        
        result_label = self.ids.result
        area_label = self.ids.area
        
        result_label.text = ""
        result_label.text = ""
        
        
        if not expression:
            result_label.text = "Expression can't be empty"
            return
        result = self.helper.integrate(expression)
        result_label.text = result
        
        if (upper_limit != "" and down_limit != ""):
            if not (self.is_number(upper_limit) and self.is_number(down_limit)):
                area_label.text = "Both upper limit and down limit should be numbers"
                return
            area = self.helper.definite_integral(expression, float(upper_limit), float(down_limit))
            area_label.text = area
        
        
    def is_number(self, num: str) -> bool:
        try:
            x = float(num)
            return True
        except ValueError:
            return False
        