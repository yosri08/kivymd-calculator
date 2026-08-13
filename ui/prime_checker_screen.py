from kivymd.uix.screen import MDScreen

from logic.number_theory import check_prime, next_prime, prime_factors


MAX_VALUE = 10**15

SUPERSCRIPTS = str.maketrans(
    "0123456789",
    "⁰¹²³⁴⁵⁶⁷⁸⁹"
)


class PrimeCheckerScreen(MDScreen):

    def process_prime_factors(self, factors: dict) -> str:
        parts = []

        for n, repeat in factors.items():
            if repeat == 1:
                parts.append(str(n))
            else:
                exponent = str(repeat).translate(SUPERSCRIPTS)
                parts.append(f"{n}{exponent}")

        return "×".join(parts)

    def solve(self):
        value_str = self.ids.value_field.text

        if not value_str:
            return

        value = int(value_str)

        if value >= MAX_VALUE:
            return

        self.ids.is_prime_label.right_text = str(check_prime(value))
        self.ids.next_prime_label.right_text = str(next_prime(value))
        self.ids.prime_factors_label.right_text = (
            self.process_prime_factors(prime_factors(value))
        )