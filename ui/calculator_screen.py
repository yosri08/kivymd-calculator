from kivymd.uix.screen import MDScreen
from logic.normal_calculator import NormalCalculatorLogic

class CalculatorScreen(MDScreen):
    helper = NormalCalculatorLogic()
    
    def update_expression(self, new_token: str):
        display = self.ids.display
        new_expression = self.helper.update_expression(display.text, new_token)
        display.text = new_expression
        
    def clear(self):
        self.ids.display.text = "0"
        
    def solve(self):
        display = self.ids.display
        result = self.helper.solve_expression(display.text)
        display.text = result
        
    def delete(self):
        display = self.ids.display
        display.text = display.text[:len(display.text)-1]
    pass