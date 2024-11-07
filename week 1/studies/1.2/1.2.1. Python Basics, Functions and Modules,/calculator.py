# My Calculator (Version 1)
# --------------------------
# This script provides basic arithmetic operations and a placeholder function for an S3 bucket example.

def addition(num_1, num_2):
    """
    Prints the result of adding two numbers.

    Parameters:
    num_1 (int or float): The first number.
    num_2 (int or float): The second number.
    """
    add = num_1 + num_2
    print(f"Addition result: {add}")

def sub(num_1, num_2):
    """
    Prints the result of subtracting the second number from the first.

    Parameters:
    num_1 (int or float): The number to subtract from.
    num_2 (int or float): The number to subtract.
    """
    sub = num_1 - num_2
    print(f"Subtraction result: {sub}")

def multiply(num_1, num_2):
    """
    Prints the result of multiplying two numbers.

    Parameters:
    num_1 (int or float): The first number.
    num_2 (int or float): The second number.
    """
    mul = num_1 * num_2
    print(f"Multiplication result: {mul}")

def s3_bucket():
    """
    Placeholder function for S3 bucket operation.
    
    Prints a message indicating an S3 bucket-related operation.
    """
    print("S3 bucket operation placeholder")
