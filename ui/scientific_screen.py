from kivymd.uix.screen import MDScreen
from logic.scientific_calculator import ScientificCalculatorLogic
import re




class ScientificScreen(MDScreen):
    
    helper = ScientificCalculatorLogic()
    
    def update_expression(self, new_token):
        display = self.ids.display
        new_expression = self.helper.update_expression(display.text, new_token)
        display.text = new_expression
        
    def clear(self):
        display = self.ids.display
        display.text = "0"
        
    def solve(self):
        display = self.ids.display
        solution = self.helper.solve_expression(display.text)
        display.text = solution
        self.last_solution = solution
        
    def delete(self):
        display = self.ids.display
        current_text = display.text
        display.text = self.helper.delete(current_text)
        
        
    def change_angle_mode(self):
        btn = self.ids.angle_btn
        if btn.text == "Radians":
            self.helper.change_angle_mode("degrees")
            btn.text = "Degrees"
        else:
            self.helper.change_angle_mode("radians")
            btn.text = "Radians"
            
    def get_last_solution(self):
        if hasattr(self, "last_solution"):
            self.ids.display.text = self.last_solution
            
            
        
            
        
    