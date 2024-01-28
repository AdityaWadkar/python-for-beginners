try:
    # Some code that might raise an exception
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    
    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    # Handling division by zero exception
    print("Oops! Denominator cannot be zero. Please try again.")

except ValueError:
    # Handling invalid input (non-integer) exception
    print("Oops! Please enter valid integers. Please try again.")

except Exception as e:
    # Catching any other unexpected exceptions
    print("Oops! Something went wrong:", e)

else:
    # Executed if no exception is raised
    print("No exceptions occurred. Great job!")

finally:
    # Always executed, whether an exception occurred or not
    print("This block always runs. Thanks for using the program!")
