def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """
    Calculate the square root of a number using the bisection method.

    Args:
    square_target (float): The number for which the square root is to be calculated.
    tolerance (float): The acceptable tolerance for error. Default is 1e-7.
    max_iterations (int): The maximum number of iterations before termination. Default is 100.

    Returns:
    float: The approximated square root of square_target.
    """
    # Handle edge cases
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 0:
        print(f'The square root of {square_target} is 0')
        return 0
    if square_target == 1:
        print(f'The square root of {square_target} is 1')
        return 1

    # Initialize bounds for bisection method
    low = 0
    high = max(1, square_target)
    root = None

    # Bisection method to approximate the square root
    for _ in range(max_iterations):
        mid = (low + high) / 2
        square_mid = mid ** 2

        # Check if the result is within the acceptable tolerance
        if abs(square_mid - square_target) < tolerance:
            root = mid
            break
        # Adjust bounds based on the comparison
        elif square_mid < square_target:
            low = mid
        else:
            high = mid

    # Output the result or failure to converge
    if root is None:
        print(f"Failed to converge within {max_iterations} iterations.")
    else:
        print(f'The square root of {square_target} is approximately {root}')

    return root


if __name__ == "__main__":
    try:
        # Get user input and validate it
        N = float(input("Enter a number to find the square root: "))
        square_root_bisection(N)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
