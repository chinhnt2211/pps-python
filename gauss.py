import math
import horner
import global_function as gf


def BSP_gauss(arr_y):
    result = []
    result.append(arr_y)
    for i in range(1, len(arr_y)):
        result.append([])
        for j in range(len(result[i-1])-1):
            m = (result[i-1][j+1] - result[i-1][j])
            result[i].append(m)
    return result


def gauss_1(arr_x, arr_y):
    h = arr_x[1] - arr_x[0]
    n = len(arr_y)
    mid_point = int((n-1) / 2)
    arr_bsp = BSP_gauss(arr_y)
    result = [arr_y[mid_point]]
    for i in range(1, len(arr_bsp)):
        mid_btsp = math.floor(len(arr_bsp[i]) / 2)
        f = [arr_bsp[i][mid_btsp] / (math.factorial(i) * h**i)]

        # a1 * (x - x0)
        f = horner.multiplication(f, arr_x[mid_point])

        j_up = math.floor(i / 2) + 1
        j_down = math.floor((i - 1) / 2) + 1

        # print(i , j_down, j_up, mid_btsp)
        # Phần tiến  
        for j in range(1, j_up):
            f = horner.multiplication(f, arr_x[mid_point + j])
        # Phần lùi
        for j in range(1, j_down):
            f = horner.multiplication(f, arr_x[mid_point - j])

        result = gf.add_two_polynomial(result, f)
    return result


def gauss_2(arr_x, arr_y):
    h = arr_x[1] - arr_x[0]
    n = len(arr_y)
    mid_point = int((n-1) / 2)
    arr_bsp = BSP_gauss(arr_y)
    result = [arr_y[mid_point]]
    for i in range(1, len(arr_bsp)):

        mid_btsp = math.floor((len(arr_bsp[i]) - 1) / 2)

        # delta - y(-1)
        f = [arr_bsp[i][mid_btsp] / (math.factorial(i) * h**i)]

        # a1 * (x - x0)
        f = horner.multiplication(f, arr_x[mid_point])

        j_up =  math.floor((i - 1) / 2) + 1
        j_down = math.floor(i / 2) + 1

        # print(i ,  j_up, j_down, mid_btsp)
        # Phần tiến  
        for j in range(1, j_up):
            f = horner.multiplication(f, arr_x[mid_point + j])
        # Phần lùi
        for j in range(1, j_down):
            f = horner.multiplication(f, arr_x[mid_point - j])

        result = gf.add_two_polynomial(result, f)
    return result

if __name__ == "__main__":

    A = [ 0, 1, 2, 3 , 4]
    # X
    B = [ 0.5, 0.731058, 0.880797, 0.952574, 0.982013]
    # B = [1, 2 , 3, 4, 5]

    print(gauss_1(A, B))
    print(horner.value(gauss_1(A,B), 1.5))
    print()
    print(horner.value(gauss_2(A,B), 1.5))
