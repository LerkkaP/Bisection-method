import matplotlib.pyplot as plt
import numpy as np

counter = 0
function = input("Give a function: ")
quantity = int(input("Give the number of how many approximations are printed: "))
initial_value = int(input("Give an initial value: "))
final_value = int(input("Give a final value: "))
precision = int(input(": "))


def f(x):
    evaluation = eval(function)
    return evaluation

if f(initial_value) > 0 and f(final_value) < 0 or f(initial_value) < 0 and f(final_value) > 0:
    interval = f"]{initial_value}, {final_value}["
    print(f"Function has a solution in interval {interval}.")

    x = np.linspace(-6, 6, num=1000)
    y = f(x)

    fig, ax = plt.subplots()
    plt.grid()
    ax.plot(x,y, color="blue")
    ax.set_aspect('equal')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.set_xlim(-3, 5)
    ax.set_ylim(-3, 5)

    plt.plot(x, y, label="f(x)")
    plt.legend()
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    plt.title("Graph")
    plt.show()

    while counter <= quantity:
        midway = 0.5 * (initial_value + final_value)
        value_a = f(initial_value)
        value_c = f(midway)
        product_ac = value_a * value_c
        counter += 1
        if product_ac >= 0:
            initial_value = midway
        elif product_ac <= 0:
            final_value = midway
    print("c =", round(midway, precision))

else:
    interval = f"]{initial_value}, {final_value}["
    print(f"Function has no solution in interval {interval}.")

