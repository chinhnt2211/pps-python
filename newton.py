import horner
import global_function as gf

def BTH(arr_y, arr_x):
    result = []
    result.append(arr_y)
    for i in range(1,len(arr_y)):
        result.append([])
        for j in range(len(result[i-1])-1):
            m = (result[i-1][j+1] - result[i-1][j])/(arr_x[j+i] - arr_x[j])
            result[i].append(m)
    return result

# Newton tiến 
def newton_up(arr_y, arr_x):
    arr_bth = BTH(arr_y, arr_x)
    print(arr_bth)
    print("----------")
    result = [arr_y[0]]
    for i in range(1, len(arr_bth)):
        f = [arr_bth[i][0]]
        for j in range(0, i):
            print("x: ", arr_x[j])
            f = horner.multiplication(f,arr_x[j])
        print(f)
        result = gf.add_two_polynomial(result,f)
    return result

# Newton lùi
def newton_down(arr_y, arr_x):
    arr_bth = BTH(arr_y, arr_x)
    print(arr_bth)
    print("----------")
    len_x = len(arr_x)
    result = [arr_y[len(arr_y)-1]]
    for i in range(1, len(arr_bth)):
        f = [arr_bth[i][len(arr_bth[i])-1]]
        for j in range(0, i):
            print("x: ", arr_x[len_x - j - 1])
            f = horner.multiplication(f,arr_x[len_x- j - 1])
        print(f)
        result = gf.add_two_polynomial(result,f)
    return result

if __name__ == "__main__" :

    # Input
    # Y
    A = [0.76 , 0.62, 0.45, 0.28]
    # X
    B = [1.0, 1.3, 1.6, 1.9 ]

    print("Up")
    print(gf.to_string_polynomial(newton_up(A,B)))
    print("Down")
    print(gf.to_string_polynomial(newton_down(A,B)))