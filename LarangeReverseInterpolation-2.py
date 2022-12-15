import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def multiPoly(A, B):
    prod = [0]*(len(A) + len(B) - 1)
    for i in range(0, len(A), 1):
        for j in range(0, len(B), 1):
            prod[i + j] += A[i] * B[j]
    return prod

def Lagrange(x, y, F, L):
    L = [[0] * len(x)] * len(x)
    poly = [[0, 0]]*len(x)  # mảng cho các đa thức đơn vị
    temp = [1]*len(x)
    tempPoly = [[]]*len(x)  # đa thức cơ sở ( 1 + 0*x)
    for i in range(len(x)):
        poly[i] = [-x[i], 1]
        # hàm tạo các đa thức nhỏ từ mảng x
    for i in range(len(x)):
        if i == 0:
            tempPoly[i] = poly[1]
        else:
            tempPoly[i] = poly[0]
        for j in range(len(x)):
            if (j != 0 and j != i and i != 0) or (i == 0 and (j > 1)):
                # if i != j:
                tempPoly[i] = multiPoly(tempPoly[i], poly[j])
                # tinh tu so L[i]
            if j != i:
                temp[i] *= (-poly[i][0] + poly[j][0])
                # tính mẫu số L[i]
    for i in range(len(tempPoly)):
        L[i] = [tempPoly[i][j]/temp[i] for j in range(len(tempPoly[i]))]
        # tính các đa thức Lagrange cơ bản

    for i in range(len(x)):
        for j in range(len(x)):
            F[i] += L[j][i] * y[j]
            # tính đa thức Lagrange
    return L, F

def printPoly(F):
    print("F = ", end='')
    for i in range(len(F)):
        if i != len(F)-1:
            print(f'{F[i]}*x^{i} + ', end='')
        else:
            print(f'{F[i]}*x^{i}  ', end='')


if __name__ == "__main__":

    x=  [2.7 , 2.8 , 2.9 , 3.  ]
    y =  [0.24 ,0.39, 0.56, 0.75]
  #  x = [1.03  , 1.09 ,  1.22 ,  1.29  ]
  #  y = [0.6909, 0.5781 ,0.3584 ,0.2541]

    print(x)
    print(y)

    F = [0]*len(x)  # mảng cho đa thức nội suy Lagrange
    L = [[0]*len(x)]*len(x)  # mảng cho các đa thức Lagrange cơ bản
    L, F = Lagrange(y, x, F, L)
    printPoly(F)
    k = 0.4 #điểm cần nội suy ngược
    result = 0
    for i in range(len(F)):
        result += F[i]*pow(k,i)
        #thử lại 
    print("\n kết quả")
    print(result)
    

    
   
   

