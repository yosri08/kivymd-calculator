import pytest
from logic.scientific_calculator import ScientificCalculatorLogic


helper = ScientificCalculatorLogic()



UPDATE_EXPRESSION_TEST_CASES = [
    ("0", "5", "5"),
    ("12", "3", "123"),
    ("5", "+", "5+"),
    ("5", "-", "5-"),
    ("5", "×", "5×"),
    ("5", "÷", "5÷"),
    ("0", "sin", "sin("),
    ("5+", "cos", "5+cos("),
    ("10×", "tan", "10×tan("),
    ("0", "log", "log("),
    ("0", "factorial", "factorial("),
    ("5+", "remain", "5+remain("),
    ("0", "π", "π"),
    ("5+", "π", "5+π"),
    ("0", "√", "√"),
    ("5+", "√", "5+√"),
    ("0", "(", "("),
    ("(", ")", "()"),
]

@pytest.mark.parametrize("expression, token, expected", UPDATE_EXPRESSION_TEST_CASES)
def test_update_expression(expression, token, expected):
    result = helper.update_expression(expression, token)

    assert result == expected, (
        f"\nExpression : {expression}"
        f"\nToken      : {token}"
        f"\nExpected   : {expected}"
        f"\nGot        : {result}"
    )
    
    
SOLVE_TEST_CASES = [
    ("π", "3.14159265"),
    ("2×π", "6.28318531"),
    ("sin(0)", "0"),
    ("sin(π÷2)", "1"),
    ("cos(0)", "1"),
    ("cos(π)", "-1"),
    ("tan(0)", "0"),
    ("tan(π÷4)", "1"),
    ("log(1)", "0"),
    ("log(2.71828183)", "1"),
    ("log(7.3890561)", "2"),
    ("factorial(0)", "1"),
    ("factorial(1)", "1"),
    ("factorial(5)", "120"),
    ("remain(10/3)", "1"),
    ("remain(15/5)", "0"),
    ("remain(7/4)", "3"),
    ("5²", "25"),
    ("0²", "0"),
    ("(-3)²", "9"),
    ("2^3", "8"),
    ("5^0", "1"),
    ("9^0.5", "3"),
    ("2+3×4", "14"),
    ("(2+3)×4", "20"),
    ("2^3^2", "512"),
    ("sin(π÷6)+5²", "25.5"),
    ("remain(120/9)", "3"),  
    ("log(7.3890561)×cos(0)+5", "7"),
    ("tan(π÷4)×remain(16/5)", "1")
]


@pytest.mark.parametrize("expression, expected", SOLVE_TEST_CASES)
def test_solve_expression(expression, expected):
    result = helper.solve_expression(expression)

    assert result == expected, (
        f"\nExpression : {expression}"
        f"\nExpected   : {expected}"
        f"\nGot        : {result}"
    )