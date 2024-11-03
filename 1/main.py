# Importing the datetime module to work with dates and times
from datetime import datetime

def your_age_in_the_future(age, year):
    """
    Calculates your current age based on your birth year and predicts your age in 10 years.
    
    Parameters:
    age (int): The current age you are asking about.
    year (int): The year of birth.

    Returns:
    str: A message about your current age and how old you will be in 10 years.
    """
    current_year = datetime.now().year  # Get the current year from the system
    real_age = current_year - year  # Calculate the actual age based on birth year

    # Check if the user is yet to be born based on provided year and age
    if real_age < age:
        return 'You are not born yet'
    
    # Check if the current age matches the provided age
    elif real_age == age:
        age_in_ten_years = real_age + 10  # Calculate age in 10 years
        return f'You are now {age} years old and you will be {age_in_ten_years} years old in 10 years'
    
    # Otherwise, return the calculated actual age
    else:
        return f'You are {real_age} years old'

    return age  # This return is unreachable but can be used for debugging or modifications


def school_age_calculator(age, name):
    """
    Determines if a child is ready to start school based on their age.
    
    Parameters:
    age (int): The age of the child.
    name (str): The name of the child.

    Returns:
    str: A message about school readiness based on the child's age.
    """
    # Check if the child is too young to start school
    if age < 5:
        return f'Enjoy the time, {name} is too young to go to school at age {age}'
    
    # Check if the child is exactly 5 years old and ready for school
    elif age == 5:
        return f'Congratulations! {name} is now 5 years old and can start school'
    
    # For children older than 5, confirm they can go to school
    else:
        return f'{name} is {age} years old and can go to school'


# Example usage of the functions:
# Uncomment to test the functions with different values
# print(school_age_calculator(4, "Ali Usman Zaidan"))
print(your_age_in_the_future(24, 2000))
