import sys
sys.path.append('calculator')
from pkg.calculator import Calculator

calculator = Calculator()
result = calculator.evaluate("3 + 7 * 2")
print(f"3 + 7 * 2 = {result}")
print(f"Expected: 17, Got: {result}")
print(f"Bug confirmed: {result == 20}") 