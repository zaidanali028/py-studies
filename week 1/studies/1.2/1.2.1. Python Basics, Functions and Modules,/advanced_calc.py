# Advanced Calculator Project ()
# ----------------------------------------

# TODO:
# 1. Create a virtual environment for this project:
#    Command: python -m venv myenv

# Importing a custom calculator module (calculator_module) for basic calculations
import calculator_module as basic_calc

def advanced_calc():
    """
    Performs advanced calculations using basic functions from the calculator_module.

    Operations:
    - Addition of 1 and 2
    - Subtraction of 1 from 2
    - Multiplication of 1 and 2

    Prints:
    The results of the addition, subtraction, and multiplication operations.
    """
    # Using functions from calculator_module for basic arithmetic
    addition_solution = basic_calc.addition(1, 2)       # Adds 1 + 2
    sub_solution = basic_calc.sub(1, 2)                 # Subtracts 2 - 1
    multiplication_solution = basic_calc.multiply(1, 2) # Multiplies 1 * 2

    # Printing the results of each operation
    print(f"Addition: {addition_solution}, Subtraction: {sub_solution}, Multiplication: {multiplication_solution}")

# Calling the function to execute advanced calculations
advanced_calc()