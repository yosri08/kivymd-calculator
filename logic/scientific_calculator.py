import re
from asteval import Interpreter


class ScientificCalculatorLogic:
    """
    Handles scientific calculator expression building,
    normalization, and solving.
    """

    TRIG_FUNCTIONS = {"sin", "cos", "tan"}

    FUNCTIONS = {
        "log",
        "factorial",
        "remain",
    }

    SYMBOLS = {
        "÷": "/",
        "×": "*",
        "^": "**",
        "²": "**2",
        "π": "pi",
    }

    def __init__(self):
        self.aeval = Interpreter()

    def update_expression(self, expression: str, token: str) -> str:
        """
        Add a new token to the current expression
        """

        if token in self.TRIG_FUNCTIONS or token in self.FUNCTIONS:
            token += "("

        if expression == "0":
            return token

        return expression + token

    def normalize_expression(self, expression: str) -> str:
        """
        Convert calculator syntax into Python syntax
        """

        expression = self._replace_symbols(expression)
        expression = self._replace_square_roots(expression)
        expression = self._replace_remainder(expression)

        return expression

    def _replace_symbols(self, expression: str) -> str:
        for symbol, replacement in self.SYMBOLS.items():
            expression = expression.replace(symbol, replacement)

        return expression

    def _replace_square_roots(self, expression: str) -> str:
        """
        Convert √number into number**0.5
        """

        return re.sub(
            r"√(\d+\.?\d*)",
            r"\1**0.5",
            expression
        )

    def _replace_remainder(self, expression: str) -> str:
        """
        Convert remain(a/b) into a%b
        """

        return re.sub(
            r"remain\((\d+\.?\d*)/(\d+\.?\d*)\)",
            r"\1%\2",
            expression
        )

    def solve_expression(self, expression: str) -> str:
        """
        solves an expression and returns the result
        """

        try:
            handled_expression = self.normalize_expression(expression)

            self.aeval.error.clear()

            result = self.aeval(handled_expression)

            if self.aeval.error:
                exception = self.aeval.error[-1].exc

                if exception is ZeroDivisionError:
                    return "Error: Can't divide by zero."

                elif exception in (SyntaxError, NotImplementedError):
                    return "Error: Invalid syntax."
                else:
                    return f"Error: {exception}"

            if not isinstance(result, (int, float)):
                return "Error: Invalid expression."

            if isinstance(result, float) and result.is_integer(): #in case the result was 1.00 for example we only need the whole number not the decimals
                return str(int(result))

            return str(round(result, 8))

        except Exception as e:
            return f"Error: {e}"
