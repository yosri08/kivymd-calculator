import re
from asteval import Interpreter


class NormalCalculatorLogic:
    

    aeval = Interpreter()
    operators = {"+", "-", "×", "÷"}
    number_split = re.compile(r"[+\-×÷]")
    
    def delete(self, expression: str) -> str:
        return "0" if (expression == "" or expression == "0") else expression[:len(expression)-1]

    def update_expression(self, expression: str, token: str) -> str:
        """Return the updated expression after inserting a token"""

        last_char = expression[-1] if expression else ""

        if expression == "0":
            return self._handle_leading_zero(token)

        if token == ".":
            return self._handle_decimal(expression, last_char)

        if token in self.operators:
            return self._handle_operator(expression, token, last_char)

        return expression + token

    def _handle_leading_zero(self, token: str) -> str:
        if token == "-":
            return "-"

        if token == "0" or token in self.operators:
            return "0"

        if token.isdigit():
            return token

        if token == ".":
            return "0."

        return token

    def _handle_decimal(self, expression: str, last_char: str) -> str:
        if last_char == ".":
            return expression

        if last_char in self.operators:
            return expression + "0."

        current_number = self.number_split.split(expression)[-1]

        if "." in current_number:
            return expression

        return expression + "."

    def _handle_operator(
        self,
        expression: str,
        operator: str,
        last_char: str,
    ) -> str:

        if operator == "-" and last_char in {"×", "÷"}:
            return expression + operator

        if last_char in self.operators:
            return expression[:-1] + operator

        return expression + operator

    @staticmethod
    def normalize_expression(expression: str) -> str:
        """Convert calculator symbols into python symbols"""
        return expression.replace("×", "*").replace("÷", "/")

    def solve_expression(self, expression: str) -> str:
        """
        solves an expression and returns the result
        """
        try:
            self.aeval.error.clear()
            normalaized_expression = self.normalize_expression(expression)
            result = self.aeval(normalaized_expression)

            if self.aeval.error:
                exception = self.aeval.error[-1].exc

                if exception is ZeroDivisionError:
                    return "Error: Can't divide by zero."

                if exception is SyntaxError or exception is NotImplementedError:
                    return "Error: Invalid syntax."

                return f"Error: {exception}"

            if isinstance(result, float) and result.is_integer():
                return str(int(result))

            return str(round(result, 8))

        except Exception as e:
            return f"Error: {e}"