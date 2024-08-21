def my_function(parameter1, parameter2):
    """
    Brief description of the function.

    Definition:
        we are adding parameter 1 and 2 together and returning parameter 3

    Args:
        parameter1 (float): this is a data point for a model
        parameter2 (float): this is an additional data point

    Returns:
        float: the sum of parameter1 and parameter2

    Raises:
        ErrorType: Description of the exception raised, if any.

    Examples:
        x = my_function(1, 2)

    Note:
        Any additional notes about the function.
    """
    # Function code here
    parameter3 = parameter2 + parameter1
    return parameter3

if __name__ == "__main__":
    parameter1 = 2
    parameter2 = 3

    print(my_function(parameter1, parameter2))