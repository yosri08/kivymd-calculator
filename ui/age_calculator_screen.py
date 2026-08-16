
from kivymd.uix.screen import MDScreen
from logic.birthday_calculator import calculate_age, days_to_months
from datetime import date
class AgeCalculatorScreen(MDScreen):
    
    def calculate_age(self, birth_date):
        current_age_label = self.ids.current_age_label
        next_birthday_label = self.ids.next_birthday_label
        
        data = calculate_age(birth_date)
        age = data["age"]
        months, days = data["time_till_birthday"]
        current_age_label.right_text = str(age)
        print(months, days)
        if (months > 0) and (days > 0):
            next_birthday_label.right_text = f"{months} months and {days} days"
        elif months < 0:
            next_birthday_label.right_text = f"{days} days"
        elif days < 0:
            next_bithday_label.right_text = f"{months} months"
        else:
            next_birthday_label.right_text = "It's your birthday!"
        