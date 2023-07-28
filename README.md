# Bisection Method
## <span style="font-size: smaller;">How It Works</span>
The Bisection Method relies on the intermediate value theorem to find roots within a specified interval. The algorithm repeatedly divides the interval in half and checks whether the function changes sign between the interval boundaries. If the function changes sign, it means there is at least one root within that interval. The process continues until the desired precision is achieved.

## <span style="font-size: smaller;">Usage</span>
Run the program and provide the required inputs:

**Function**: Enter the function whose roots you want to find (e.g., "x**2 - 4").
**Quantity**: Enter the maximum number of roots to find within the interval (an approximation).
**Initial value**: Enter the starting point of the interval where roots might exist.
**Final value**: Enter the endpoint of the interval where roots might exist.
**Precision**: Enter the desired level of precision for the root approximation.

The program will then validate whether the function has at least one root within the provided interval. If there are roots, it will display the interval and plot the function's graph using Matplotlib.

Next, the program will apply the Bisection Method to find the roots of the function within the specified interval. It will return an approximation of the solutions with the desired precision. It's important to note that the bisection method implemented in the program may find only one root within the provided interval, even if there are multiple possible roots. The program will return an approximation of the solution with the desired precision.

## <span style="font-size: smaller;">Example</span>

Let's find a root of the function x**3 - 2*x - 5 within the interval [1, 3], with a precision of 5 decimal places. N.B:

**Function**: x**3 - 2*x - 5
**Quantity**: 20
**Initial value**: 1
**Final value**: 3
**Precision**: 5

The program will display the interval ]1, 3[ and plot the graph of the function. Finally, it will output the root it found:
![Figure 1](Figure%201.png)

```bash
Function has a solution in interval ]1, 3[.
The root is: c = 2.09455
```

## <span style="font-size: smaller;">Dependencies</span>
This program requires the following Python libraries:

- Matplotlib: For plotting the function's graph.
- NumPy: For numerical calculations and generating arrays.
- SymPy: For evaluating symbolic functions.

You can install these libraries using pip:

```bash
pip install matplotlib numpy sympy
```




