import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def input_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_function():
    return input("Function: ")

def validate_interval(a, b, func, num_segments=100):
    x_values = np.linspace(a, b, num=num_segments)
    y_values = [func(x) for x in x_values]

    for i in range(len(y_values) - 1):
        if y_values[i] * y_values[i + 1] <= 0:
            return True

    return False

def bisection_method(func, a, b, tolerance):
    roots = []
    while a < b:
        if func(a) == 0:
            roots.append(a)
            break
        if func(b) == 0:
            roots.append(b)
            break

        c = (a + b) / 2
        value_a = func(a)
        value_c = func(c)
        product_ac = value_a * value_c
        if np.abs(value_c) < tolerance:
            roots.append(c)
            a = c
        elif product_ac < 0:
            b = c
        else:
            a = c

    return roots

if __name__ == "__main__":
    function = input_function()
    quantity = input_integer("Quantity: ")
    initial_value = input_integer("Initial value: ")
    final_value = input_integer("Final value: ")
    precision = input_integer("Precision: ")

    x = np.linspace(initial_value, final_value, num=1000)
    f = sp.lambdify(sp.Symbol('x'), sp.sympify(function))

    if validate_interval(initial_value, final_value, f):
        interval = f"]{initial_value}, {final_value}["
        print(f"Function has a solution in interval {interval}.")

        y = f(x)

        plt.plot(x, y, label="f(x)")
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.grid(True, which='both')
        plt.legend()
        plt.xlabel("x - axis")
        plt.ylabel("y - axis")
        plt.title("Graph")
        plt.show()

        roots = bisection_method(f, initial_value, final_value, 1e-6)
        print("The root is:", ", ".join(f"c = {round(root, precision)}" for root in roots))

    else:
        interval = f"]{initial_value}, {final_value}["
        print(f"Function has no solution in interval {interval}.")
