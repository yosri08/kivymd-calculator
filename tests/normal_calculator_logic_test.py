import pytest
from logic.normal_calculator import NormalCalculatorLogic


helper = NormalCalculatorLogic()


UPDATE_EXPRESSION_TEST_CASES = [
    ("0", "0", "0"),
    ("0", "1", "1"),
    ("0", "5", "5"),
    ("0", "-", "-"),
    ("0", "+", "0"),
    ("0", "×", "0"),
    ("0", "÷", "0"),
    ("0", ".", "0."),
    ("1", "2", "12"),
    ("12", "3", "123"),
    ("999", "9", "9999"),
    ("5", "+", "5+"),
    ("5", "-", "5-"),
    ("5", "×", "5×"),
    ("5", "÷", "5÷"),
    ("5+", "+", "5+"),
    ("5+", "-", "5-"),
    ("5+", "×", "5×"),
    ("5+", "÷", "5÷"),
    ("5-", "+", "5+"),
    ("5-", "-", "5-"),
    ("5-", "×", "5×"),
    ("5-", "÷", "5÷"),
    ("5×", "+", "5+"),
    ("5×", "-", "5×-"),
    ("5×", "×", "5×"),
    ("5×", "÷", "5÷"),
    ("5÷", "+", "5+"),
    ("5÷", "-", "5÷-"),
    ("5÷", "×", "5×"),
    ("5÷", "÷", "5÷"),
    ("-", "5", "-5"),
    ("5×-", "3", "5×-3"),
    ("5÷-", "2", "5÷-2"),
    ("1", ".", "1."),
    ("1.", ".", "1."),
    ("5+", ".", "5+0."),
    ("5+0.", ".", "5+0."),
    ("5×", ".", "5×0."),
    ("5÷", ".", "5÷0."),
    ("5+", "0", "5+0"),
    ("5-", "0", "5-0"),
    ("5×", "0", "5×0"),
    ("5÷", "0", "5÷0"),
    ("-5", "-", "-5-"),
    ("-5+", "-", "-5-"),
    ("-5×", "-", "-5×-"),
    ("0", "+", "0"),
    ("0", "-", "-")
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
    ("1+2", "3"),
    ("5-2", "3"),
    ("3×4", "12"),
    ("8÷2", "4"),
    ("2+3×4", "14"),
    ("10-6÷2", "7"),
    ("2×3+4", "10"),
    ("(2+3)×4", "20"),
    ("10÷(2+3)", "2"),
    ("-5+2", "-3"),
    ("5×-3", "-15"),
    ("-5×-3", "15"),
    ("0.1+0.2", "0.3"),
    ("5÷2", "2.5"),
    ("3.5×2", "7"),
    ("999999×999999", "999998000001"),
    ("5÷0", "Error: Can't divide by zero."),
    ("5+", "Error: Invalid syntax."),
    ("×5", "Error: Invalid syntax."),
    
]


@pytest.mark.parametrize("expression, expected", SOLVE_TEST_CASES)
def test_solve_expression(expression, expected):
    result = helper.solve_expression(expression)

    assert result == expected, (
        f"\nExpression : {expression}"
        f"\nExpected   : {expected}"
        f"\nGot        : {result}"
    )