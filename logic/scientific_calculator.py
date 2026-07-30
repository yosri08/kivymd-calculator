import re
import math
from asteval import Interpreter




class ScientificCalculatorLogic:
    """
    Handles scientific calculator expression building,
    normalization, and solving.
    """

    TRIG_FUNCTIONS = {"sin", "cos", "tan"}
    OPERATORS = {"+", "-", "×", "÷"}
    NUMBER_SPLIT = re.compile(r"[+\-×÷]")
    FUNCTIONS = {"log10", "ln"}

    SYMBOLS = {
        "÷": "/",
        "×": "*",
        "^": "**",
        "²": "**2",
        "π": "pi",
        "mod": "%",
        "ln": "log"
    }

    SPECIALS = {"√x", "x!", "x²", "x³", "1/x", "x^y"}

    _SPECIAL_SUFFIXES = {
        "x!": "!",
        "x²": "^(2)",
        "x³": "^(3)",
        "1/x": "^(-1)",
        "x^y": "^(",
    }

    def __init__(self):
        self.aeval = Interpreter()
        self.aeval.symtable["sin"] = self._sin
        self.aeval.symtable["cos"] = self._cos
        self.aeval.symtable["tan"] = self._tan
        self.angle_mode = "radians"
    
    
    def delete(self, expression: str):
        """
        deletes the last character unless there's an edge case
        """
        FUNCTIONS = (
            "sin(",
            "cos(",
            "tan(",
            "log10(",
            "ln(",
            "mod",
            "^("
        )

        SINGLE_TOKENS = (
            "√",
            "π",
            "e",
            "!",
        )
        if expression == "0" or expression == "":
            return "0"

        for func in FUNCTIONS:
            if expression.endswith(func):
                return expression[:-len(func)]

        for token in SINGLE_TOKENS:
            if expression.endswith(token):
                return expression[:-1]
                
        return expression[: len(expression)-1]
        
        
    def update_expression(self, expression: str, token: str) -> str:
        """Return the updated expression after inserting a token."""

        if token in self.SPECIALS:
            return self._handle_specials(expression, token)

        if token in self.TRIG_FUNCTIONS or token in self.FUNCTIONS:
            return self._handle_function(expression, token)

        last_char = expression[-1] if expression else ""

        if expression == "0":
            return self._handle_leading_zero(token)

        if token == ".":
            return self._handle_decimal(expression, last_char)

        if token in self.OPERATORS:
            return self._handle_operator(expression, token, last_char)

        return expression + token

    def _handle_function(self, expression: str, token: str) -> str:
        token += "("

        if expression == "0":
            return self._handle_leading_zero(token)

        return expression + token

    def _handle_specials(self, expression: str, token: str) -> str:
        last_char = expression[-1] if expression else ""

        if token == "√x":
            if expression == "0":
                return "√"
            if last_char in self.OPERATORS:
                return expression + "√"
            return expression

        last_token = self.NUMBER_SPLIT.split(expression)[-1]
        if not last_token.isnumeric():
            return expression

        return expression + self._SPECIAL_SUFFIXES[token]

    def _handle_leading_zero(self, token: str) -> str:
        if token == "-":
            return "-"

        if token == "0" or token in self.OPERATORS:
            return "0"

        if token.isdigit():
            return token

        if token == ".":
            return "0."

        return token

    def _handle_decimal(self, expression: str, last_char: str) -> str:
        if last_char == ".":
            return expression

        if last_char in self.OPERATORS:
            return expression + "0."

        current_number = self.NUMBER_SPLIT.split(expression)[-1]

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

        if last_char in self.OPERATORS:
            return expression[:-1] + operator

        return expression + operator

    def normalize_expression(self, expression: str) -> str:
        """
        Convert calculator syntax into Python syntax
        """

        expression = self._replace_symbols(expression)
        expression = self._replace_square_roots(expression)
        expression = self._replace_factorials(expression)
        return expression

    def _replace_factorials(self, expr: str) -> str:
        pattern = re.compile(r'(\d+|\([^()]*\))!')

        while True:
            new_expr = pattern.sub(r'factorial(\1)', expr)
            if new_expr == expr:
                break
            expr = new_expr

        return expr
    def _replace_symbols(self, expression: str) -> str:
        for symbol, replacement in self.SYMBOLS.items():
            expression = expression.replace(symbol, replacement)

        return expression

    
        

    def _replace_square_roots(self, expr: str) -> str:
        """
        Convert √number into number**0.5
        """
        pattern = re.compile(r'√(\d+|\([^()]*\))')

        while True:
            new_expr = pattern.sub(r'(\1)**(1/2)', expr)
            if new_expr == expr:
                break
            expr = new_expr

        return expr

    

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
    def _sin(self, x):
        if self.angle_mode == "degrees":
            x = math.radians(x)
        return math.sin(x)
        
    def _cos(self, x):
        if self.angle_mode == "degrees":
            x = math.radians(x)
        return math.cos(x)
        
    def _tan(self, x):
        if self.angle_mode == "degrees":
            x = math.radians(x)
        return math.tan(x)

    def change_angle_mode(self, mode: str):
        self.angle_mode = mode
