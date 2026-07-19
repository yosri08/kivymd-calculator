import pytest
from sympy import simplify
from logic.calculus_calculator import CalculusCalculatorLogic


helper = CalculusCalculatorLogic()



LIMIT_TEST_CASES = [
    ("x", "0", "0"),
    ("x^2", "2", "4"),
    ("x+5", "10", "15"),
    ("1/x", "oo", "0"),
    ("1/x", "-oo", "0"),
    ("x^2", "oo", "oo"),
    ("sin(x)/x", "0", "1"),
    ("(x^2-1)/(x-1)", "1", "2"),
    ("5+", "0", "Error"),
]

@pytest.mark.parametrize("expression, point, expected", LIMIT_TEST_CASES)
def test_limit(expression, point, expected):
    result = helper.limit(expression, point)

    if expected.startswith("Error"):
        assert result.startswith("Error"), (
            f"\nExpression : {expression}"
            f"\nPoint      : {point}"
            f"\nExpected   : {expected}"
            f"\nGot        : {result}"
        )
    else:
        assert simplify(result) == simplify(expected), (
            f"\nExpression : {expression}"
            f"\nPoint      : {point}"
            f"\nExpected   : {expected}"
            f"\nGot        : {result}"
        )
        
        
DIFFERENTIATE_TEST_CASES = [
    ("5", "0"),
    ("x", "1"),
    ("x^2", "2*x"),
    ("x^3", "3*x**2"),
    ("x^2+2*x+1", "2*x + 2"),
    ("sin(x)", "cos(x)"),
    ("cos(x)", "-sin(x)"),
    ("tan(x)", "tan(x)**2 + 1"),
    ("log(x)", "1/x"),
    ("exp(x)", "exp(x)"),
    ("5+", "Error"),
]

@pytest.mark.parametrize("expression, expected", DIFFERENTIATE_TEST_CASES)
def test_differentiate(expression, expected):
    result = helper.differentiate(expression)

    if expected.startswith("Error"):
        assert result.startswith("Error"), (
            f"\nExpression : {expression}"
            f"\nExpected   : {expected}"
            f"\nGot        : {result}"
        )
    else:
        assert simplify(result) == simplify(expected), (
            f"\nExpression : {expression}"
            f"\nExpected   : {expected}"
            f"\nGot        : {result}"
        )
        
        
INTEGRATE_TEST_CASES = [
    ("5", "5*x"),
    ("x", "x**2/2"),
    ("2*x", "x**2"),
    ("3*x^2", "x**3"),
    ("cos(x)", "sin(x)"),
    ("sin(x)", "-cos(x)"),
    ("1/x", "log(x)"),
    ("exp(x)", "exp(x)"),
    ("5+", "Error"),
]

@pytest.mark.parametrize("expression, expected", INTEGRATE_TEST_CASES)
def test_integrate(expression, expected):
    result = helper.integrate(expression)

    if expected.startswith("Error"):
        assert result.startswith("Error"), (
            f"\nExpression : {expression}"
            f"\nExpected   : {expected}"
            f"\nGot        : {result}"
        )
    else:
        assert simplify(result) == simplify(expected), (
            f"\nExpression : {expression}"
            f"\nExpected   : {expected}"
            f"\nGot        : {result}"
        )
        
        
        
        
DEFINITE_INTEGRAL_TEST_CASES = [
    ("x", 0, 2, "2"),
    ("x^2", 0, 1, "1/3"),
    ("sin(x)", 0, "pi", "2"),
    ("cos(x)", 0, 0, "0"),
    ("5", 0, 10, "50"),
]

@pytest.mark.parametrize("expression, lower, upper, expected", DEFINITE_INTEGRAL_TEST_CASES)
def test_definite_integral(expression, lower, upper,  expected):
    result = helper.definite_integral(expression, lower, upper)

    if expected.startswith("Error"):
        assert result.startswith("Error"), (
            f"\nExpression : {expression}"
            f"\nLOWER_LIMIT: {lower}"
            f"\nUPPER_LIMIT: {upper}"
            f"\nExpected   : {expected}"
            f"\nGot        : {result}"
        )
    else:
        assert simplify(result) == simplify(expected), (
            f"\nExpression : {expression}"
            f"\nLOWER_LIMIT: {lower}"
            f"\nUPPER_LIMIT: {upper}"
            f"\nExpected   : {expected}"
            f"\nGot        : {result}"
        )