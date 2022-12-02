import numpy as np
import matplotlib.pyplot as plt

import horner
import global_function as gf

# Chuyển w(x) sang dạng an*x^n + .. + a1*x + b
def find_w(arr):
    result = [1, -arr[0]]
    for i in range(1, len(arr)):
        # result = result * (x - arr[i])
        result = horner.multiplication(result, arr[i])
    return result


def lagrange(arr_x, arr_y, f):
    n = len(arr_x)
    result = [0 for i in range(n)]

    for i in range(n):
        der_f = horner.derivative(f, arr_x[i], 1)
        (arr, r) = horner.division(f, arr_x[i])
        arr = gf.multi_constant(arr, arr_y[i]/der_f)
        result = gf.add_two_polynomial(result, arr)
    return result


if __name__ == "__main__":
    A = [0, 1, 2, -1, -2, 4, 5, -3]
    B = [8, 18, 172, 16, -84, 16536, 78358, -2098]
    A.sort()
    B.sort()
    w = find_w(A)

    lagrange_arr = lagrange(A, B, w)
    print(lagrange_arr)
    print()

    range_x = np.linspace(min(A), max(A))
    plt.plot(range_x, [horner.value(lagrange_arr, range_x[i]) for i in range(len(range_x))] , 'ro-',  label = 'Larange')
    plt.plot(A, B,'go-', label= 'Dau vao')
    plt.legend(loc = 'best')
    plt.savefig("lagrange.png")
    # plt.show()
