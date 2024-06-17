"""_summary
Notes:
Error handling in python it helps t handle unexpected situations and errors

1.Try: contains code that might throw an exception
NB: if an exception occurs , the rest of the code in the try block is skipped or ignored 

2.Except: catches and handles the exceptions
NB: You can specify different handlers for different exception types 

3.Else : the code runs if no exception occurs 
if no exceptions are raised in the try block it runs.

4.Finally: it runs whether an exception is raised/ocurred or not 
NB: Used for cleaning up actions that 



"""
#Example 1: Handle exceptions with division by zero.
try:
    number=int(input("Enter a number: "))
    result=20/number
except ValueError:
    print("Invalid number! Please enter a valid number")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed")
else:
    print(f"Result is {result}") 
finally:
    print("Execution completed successfully")
    # Exercise: Write a function that converts a string to an integer and handle both valueError
    #If a string cannot be converted to an integer and the TypeError if the input is not a string
    #Use multiple except block to handle these exceptions
          
def convert_to_integer():
    try:
        input_value = input("Enter string value: ")
        number = int(input_value)
    except ValueError as valueError:
        print("Invalid number input! Please enter a valid number.")
        print(f"ValueError: {valueError}")
    except TypeError as typeError:
        print("Please enter a string")
        print(f"TypeError: {typeError}")
    else:
        print(f"Result is {number}")

convert_to_integer()


#Example 2: Exception raised for error in the input,if funds are insufficient
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {self.amount} with only {self.balance} in account."
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# Custom exceptions handling
try:
    balance = 20000
    amount_to_withdraw = 100000
    new_balance = withdraw(balance, amount_to_withdraw)
except InsufficientFundsError as e:
    print(f"Error: {e.message}")
else:
    print(f"New balance is {new_balance}")
finally:
    print("Transaction completed")

#Note
"""
Summary

Defining a custom exception
Class Custom(Exception):
    # Custom exception for specific error cases
    
  def init(self, message):
    self.message = message
    super().init(self.message)
    
#  rasing a custom exception
def check_value(value):
    if value is < or value:
        raise CustomError('Value can't be negative')
    return value
    
# Handle exceptions with try, except, else and finally

try:
    result = check_value(-10)
except CustomError as e
    print(f"Custom error caught: {e.message}")
"""


#Exercise 2:Create a custom exception InvalidAgeError and write a function that raises
#this exception if the given age is negative .Handle this custom exception when calling the function


class InvalidAgeError(Exception):
    class InvalidAgeError(Exception):
        def __init__(self, age):
            self.age = age
            self.message = f"Invalid age {self.age}. Enter a valid age input."
            super().__init__(self.message)
        # Super()
        # calling
        
    
def check_age(age):
    if age < 0 or age > 120:  # Assuming valid age is between 0 and 120
        raise InvalidAgeError(age)
    return f"Age {age} is valid."

# Example usage
try:
    age_input = -5  # An invalid age example
    result = check_age(age_input)
    print(result)
except InvalidAgeError as e:
    print(e)