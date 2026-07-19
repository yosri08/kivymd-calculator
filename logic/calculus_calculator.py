from sympy import (
    symbols,
    sympify,
    limit,
    diff,
    integrate,
    oo,
)


class CalculusCalculatorLogic:
    """
    Handles calculus operations using SymPy.
    """

    def __init__(self):
        self.x = symbols("x")

    def normalize_expression(self, expression: str) -> str:
        """
        Convert calculator symbols into SymPy syntax.
        """

        return (
            expression
            .replace("×", "*")
            .replace("÷", "/")
            .replace("^", "**")
            .replace("π", "pi")
            .replace("√", "sqrt")
        )

    def parse_expression(self, expression: str):
        """
        Convert a calculator expression into a SymPy expression.
        """

        normalized = self.normalize_expression(expression)
        return sympify(normalized)

    def limit(self, expression: str, point: str) -> str:
        """
    Calculate the limit of an expression.
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
        Differentiate an expression with respect to x.
        """

        try:
            expression = self.parse_expression(expression)
            result = diff(expression, self.x)
            return str(result)

        except Exception as e:
            return f"Error: {e}"

    def integrate(self, expression: str) -> str:
        """
        Compute the indefinite integral.
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
        Compute a definite integral.
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
