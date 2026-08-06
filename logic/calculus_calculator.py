from sympy import (
    symbols,
    sympify,
    limit,
    diff,
    integrate,
    oo,
    Integer
)


class CalculusCalculatorLogic:
    """
    Handles calculus operations using sympy
    """

    def __init__(self):
        self.x = symbols("x")

    def normalize_expression(self, expression: str) -> str:
        """
        Convert calculator symbols into SymPy syntax
        """

        return (
            expression
            .replace("×", "*")
            .replace("÷", "/")
            .replace("^", "**")
            .replace("π", "pi")
        )

    def parse_expression(self, expression: str):
        """
        Convert a calculator expression into a sympy expression
        """

        normalized = self.normalize_expression(expression)
        return sympify(normalized)

    def limit(self, expression: str, point: str) -> str:
        """
    Calculate the limit of an expression
        """

        try:
            expression = self.parse_expression(expression)

            if point in ("oo", "∞"):
                point = oo
            elif point in ("-oo", "-∞"):
                point = -oo
            else:
                point = sympify(point)

            result = limit(expression, self.x, point)
            return str(result)

        except Exception as e:
            return f"Error: {e}"

    def differentiate(self, expression: str) -> str:
        """
        Differentiate an expression with respect to x
        """

        try:
            expression = self.parse_expression(expression)
            result = diff(expression, self.x)
            return str(result)

        except Exception as e:
            return f"Error: {e}"

    def integrate(self, expression: str) -> str:
        """
        Integrates an expression with respect to x
        """

        try:
            expression = self.parse_expression(expression)
            result = integrate(expression, self.x)
            return str(result)

        except Exception as e:
            return f"Error: {e}"

    def definite_integral(
        self,
        expression: str,
        lower: float,
        upper: float,
    ) -> str:
        """
        Compute a definite integral with respect to x
        """

        try:
            expression = self.parse_expression(expression)

            result = integrate(
                expression,
                (self.x, lower, upper),
            )

            return str(result)

        except Exception as e:
            return f"Error: {e}"
            
    def evaluate(self, expression: str, point: float) -> str:
        try:
            expr = sympify(expression)
            result = expr.subs(self.x, point)
            if float(result) == int(result):
                return str(int(result))
            return str(result)
        except ValueError:
            return "Error: Value error"
        except Exception as e:
            return f"Error: {e}"
