# Chuyển mảng hệ số sang chuỗi đa thức
def to_string_polynomial(arr):
    result = ""
    n = len(arr)
    for i in range(n-1):
        if (result != ""):
            result = result + " + (" + str(arr[i]) + "x^" + str(n-i-1) + ")"
        else:
            result += " (" + str(arr[i]) + "x^" + str(n-i-1) + ")"

    result += " + (" + str(arr[n-1]) + ")"

    return result

# Nhân đa thức với 1 hệ số


def multi_constant(arr, k):
    result = arr.copy()
    for i in range(len(result)):
        result[i] = result[i] * k
    return result


# Làm tròn hệ số của đa thức

def round_polynomial(arr, r):
    result = arr.copy()
    for i in range(len(result)):
        result[i] = round(result[i], r)
    return result


# Cộng 2 đa thức với nhau

def add_two_polynomial(arr_a, arr_b):
    if (len(arr_a) < len(arr_b)):
        n = len(arr_a)
        k = len(arr_b) - len(arr_a)
        result = arr_b.copy()
        for i in range(n-1, -1, -1):
            result[i+k] = result[i+k] + arr_a[i]
    else:
        n = len(arr_b)
        k = len(arr_a) - len(arr_b)
        result = arr_a.copy()
        for i in range(n-1, -1, -1):
            result[i+k] = result[i+k] + arr_b[i]

    return result

    
# Kiểm tra mốc nội suy có cách đều không

def check_inter_point(arr):
    d = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if(arr[i-1] + d != arr[i]):
            return True
    return False