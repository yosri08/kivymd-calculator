import pytest
from logic.scientific_calculator import ScientificCalculatorLogic


UPDATE_EXPRESSION_TEST_CASES = [
    # Numbers
    ("0", "5", "5"),
    ("12", "3", "123"),

    # Operators
    ("5", "+", "5+"),
    ("5", "-", "5-"),
    ("5", "×", "5×"),
    ("5", "÷", "5÷"),

    # Trig functions
    ("0", "sin", "sin("),
    ("5+", "cos", "5+cos("),
    ("10×", "tan", "10×tan("),

    # Other functions
    ("0", "log", "log("),
    ("0", "factorial", "factorial("),
    ("5+", "remain", "5+remain("),

    # Constants
    ("0", "π", "π"),
    ("5+", "π", "5+π"),

    # Roots
    ("0", "√", "√"),
    ("5+", "√", "5+√"),

    # Parentheses
    ("0", "(", "("),
    ("(", ")", "()"),
]
helper = ScientificCalculatorLogic()
@pytest.mark.parametrize("expression, token, expected", UPDATE_EXPRESSION_TEST_CASES)
def test_add_expression(expression, token, expected):
    result = helper.update_expression(expression, token)

    assert result == expected, (
        f"\nExpression : {expression}"
        f"\nToken      : {token}"
        f"\nExpected   : {expected}"
        f"\nGot        : {result}"
    )