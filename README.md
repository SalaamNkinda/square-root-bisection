# Square Root Calculation using Bisection Method

This Python program calculates the square root of a given number using the **bisection method**. The bisection method is a numerical technique for finding the root of a function. In this case, it is used to find the square root of a number by iteratively narrowing down the search interval.

## Features
- Uses the **bisection method** for finding square roots.
- Handles edge cases (square root of 0 and 1).
- Includes error handling for invalid inputs.
- Provides an approximation within a specified tolerance (default is 1e-7).
  
## How It Works
The bisection method works by repeatedly narrowing down the range `[low, high]`:
1. Start with `low = 0` and `high = max(1, square_target)`.
2. Find the midpoint (`mid`) of this range.
3. Compare `mid**2` to the target value. If `mid**2` is close enough to the target value (within a defined tolerance), the algorithm stops.
4. Otherwise, adjust the bounds (`low` or `high`) based on whether `mid**2` is smaller or larger than the target value.

## Requirements
- Python 3.x or higher.

## Running the Program

1. Clone or download the repository.
2. Run the script using Python:

   ```bash
   python square_root_bisection.py
