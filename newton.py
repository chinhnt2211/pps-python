import math
import horner
import global_function as gf

# Bảng tỉ sai phân


def BTSP(arr_y, arr_x):
    result = []
    result.append(arr_y)
    for i in range(1, len(arr_y)):
        result.append([])
        for j in range(len(result[i-1])-1):
            m = (result[i-1][j+1] - result[i-1][j])/(arr_x[j+i] - arr_x[j])
            result[i].append(m)
    return result


# Bảng tỉ sai phân cho newton cách đều
# 1 : Sai phân tiến | 0 : Sai phân lùi
def BTSP_equidistant(arr_y, type_btsp=1):
    result = []
    result.append(arr_y)
    if (type_btsp == 0):
        for i in range(1, len(arr_y)):
            result.append([])
            for j in range(len(result[i-1])-1):
                m = (result[i-1][j+1] - result[i-1][j])
                result[i].append(m)

    elif (type_btsp == 1):
        for i in range(1, len(arr_y)):
            result.append([])
            for j in range(1, len(result[i-1])):
                m = (result[i-1][j] - result[i-1][j-1])
                result[i].append(m)
    return result


# Newton tiến
def newton_up(arr_y, arr_x):
    arr_btsp = BTSP(arr_y, arr_x)
    print("----------")
    print("BTSP Newton tiến: ", arr_btsp)
    result = [arr_y[0]]
    for i in range(1, len(arr_btsp)):
        f = [arr_btsp[i][0]]
        for j in range(0, i):
            f = horner.multiplication(f, arr_x[j])
        result = gf.add_two_polynomial(result, f)
    return result


# Newton tiến cho trường hợp điểm nội suy cách đều
def newton_equidistant_up(arr_y, arr_x, h):
    arr_btsp = BTSP_equidistant(arr_y, 1)
    print("----------")
    print("BTSP Newton mốc cách đều tiến: ", arr_btsp)
    result = [arr_y[0]]
    for i in range(1, len(arr_btsp)):
        f = [arr_btsp[i][0] / (math.factorial(i) * h**i)
             ]  # delta y0 / i! * h^i
        for j in range(0, i):
            f = horner.multiplication(f, arr_x[j])
        result = gf.add_two_polynomial(result, f)
    return result


# Newton lùi
def newton_down(arr_y, arr_x):
    arr_btsp = BTSP(arr_y, arr_x)
    print("----------")
    print("BTSP Newton lùi: ", arr_btsp)
    len_x = len(arr_x)
    result = [arr_y[len(arr_y)-1]]
    for i in range(1, len(arr_btsp)):
        f = [arr_btsp[i][len(arr_btsp[i])-1]]
        for j in range(0, i):
            f = horner.multiplication(f, arr_x[len_x - j - 1])
        result = gf.add_two_polynomial(result, f)
    return result

# Newton lùi cho trường hợp điểm nội suy cách đều


def newton_equidistant_down(arr_y, arr_x, h):
    arr_btsp = BTSP_equidistant(arr_y, 0)
    print("----------")
    print("BTSP Newton mốc cách đều lùi: ", arr_btsp)
    result = [arr_y[0]]
    len_x = len(arr_x)
    result = [arr_y[len(arr_y)-1]]
    for i in range(1, len(arr_btsp)):
        # delta yn / i! * h^i
        f = [arr_btsp[i][len(arr_btsp[i])-1] / (math.factorial(i) * h**i)]
        for j in range(0, i):
            f = horner.multiplication(f, arr_x[len_x - j - 1])
        result = gf.add_two_polynomial(result, f)
    return result


def newton(arr_y, arr_x):
    if (gf.check_inter_point(arr_x)):
        d = arr_x[1] - arr_x[0]
        print("Newton tiến với mốc cách đều : ", gf.to_string_polynomial(
            newton_equidistant_up(arr_y, arr_x, d)))

        print("Newton lùi với mốc cách đều : ",
              gf.to_string_polynomial(newton_equidistant_down(arr_y, arr_x, d)))
    else:
        print("Newton tiến : ", gf.to_string_polynomial(
            newton_up(arr_y, arr_x)))

        print("Newton lùi : ",
              gf.to_string_polynomial(newton_down(arr_y, arr_x)))

if __name__ == "__main__":

    # Input
    # Y
    A = [25, 35, 245]
    # X
    B = [-2, 3, 9]

    newton(A, B)
