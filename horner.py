import math

import global_function as gf 

# Chia da thuc voi x - c
def division(arr, c):
    arr_a = arr.copy()
    arr_b = []
    if(len(arr_a) == 0):
        return (arr_a , 0)

    arr_b.append(arr_a[0])
    for i in range(1, len(arr_a)):
        m = arr_a[i] + arr_b[i-1]*c
        arr_b.append(m)

    return (arr_b[0:len(arr_b)-1] , arr_b[len(arr_b)-1])

# Nhan da thuc voi x - c
def multiplication(arr, c):
    arr_a = arr.copy()
    arr_a.append(0)
    arr_b = []
    arr_b.append(arr_a[0])
    for i in range(1,len(arr_a)):
        m = arr_a[i] - arr_a[i-1]*c
        arr_b.append(m)
    return arr_b

# Tính giá trị của đa thức tại điểm c
def value(arr,c):
    if(len(arr) == 0):
        result = 0
    else:
        result = arr[0]

    for i in range(1,len(arr)):
        result = result*c + arr[i]

    return result   

# Tinh dao ham cap n tai diem c
def derivative(arr,c,n):
    arr_a = arr.copy()
    if(len(arr_a) == 0):
        return 0
    for i in range(n):
        (arr_a,r) = division(arr_a,c)

    return(math.factorial(n)*value(arr_a,c))

# Tìm nghiệm của đa thức
def find_roots(arr):
	roots = []
	for i in range(len(arr)-1):
		root = newton_loop(arr,0)
		if root == None:
			break
		else:
			roots.append(root)
			(arr, r) = division(arr, root)
		
	return roots

# Phương pháp lặp Newton tìm nghiệm
def newton_loop(arr, x):
	i = 0
	px = value(arr,x)
	qx = derivative(arr,x , 1)
	while abs(px) > 0.0000001 and i < 1000:
		if qx == 0:
			return None
		x = x - px / qx

		px = value(arr,x)
		qx = derivative(arr,x,1)

		i = i + 1
	
    #Vòng lặp quá 1000 sẽ dừng
	if i == 1000: 
		return None
	
    # Kiểm tra xem làm tròn có đem lại kết quả tốt hơn không
	r = round(x) 
	if(abs(value(arr,r)) < abs(value(arr,x))):
		x = r

	return x



if __name__ == "__main__":

    # Input
    # Mảng hệ số của đa thức
    A = [1, 2, 2]

    # Hằng số c
    c = - 2
    # Dao ham bac n
    n = 6

    (result_division,r) = division(A, c)


    print("Chia da thuc voi x - " + str(c)+ " : ", gf.to_string_polynomial(result_division), " phan du:" + str(r))
    print()
    print("Nhan da thuc voi x - " + str(c) + " : ", gf.to_string_polynomial(multiplication(A, c)))
    print()
    print("Gia tri da thuc tai " + str(c) + " :", value(A,c))
    print()
    print("Dao ham bac " + str(n) + " da thuc tai " + str(c) + " :", derivative(A,c,n))
    print()
    print("Nghiem cua phuong trinh la: " , find_roots(A))