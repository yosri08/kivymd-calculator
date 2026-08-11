from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivy.uix.widget import Widget  # Bypass kivy 1.2 remove_widget theme bug

from logic.number_theory import gcf, lcm


class NumberWidget(MDBoxLayout):
    index = StringProperty()


class GCFLCMScreen(MDScreen):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_index = 1  # A and B are already present

    def add_number_widget(self):
        if self.letter_index >= len(self.alphabet) - 1:
            return

        self.letter_index += 1

        self.ids.nums_container.add_widget(
            NumberWidget(index=self.alphabet[self.letter_index])
        )

    def remove_number_widget(self):
        container = self.ids.nums_container

        if len(container.children) > 2:
            Widget.remove_widget(container, container.children[0])
            self.letter_index -= 1

    def solve(self):
        widgets = self.ids.nums_container.children

        if not all(
            widget.ids.value_field.text.isnumeric()
            for widget in widgets
        ):
            return

        nums = [
            int(widget.ids.value_field.text)
            for widget in widgets
        ]

        self.ids.gcf_label.right_text = str(gcf(nums))
        self.ids.lcm_label.right_text = str(lcm(nums))