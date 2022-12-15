import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import lagrange



excel_file = 'reverse_interpolation.xlsx'
data = pd.read_excel(excel_file).values
data = np.array(data)

class newton:
    def __init__(self, Data, y0):
        self.yData = Data[1]
        self.xData = Data[0]
        self.y = y0
        self.h = self.xData[1]-self.xData[0]

    def __Bangsaiphan(self):
        m = len(self.yData)
        a = np.zeros((m,m))
        for k in range(m):
            a[k][0] = self.yData[k]

        for i in range(1,m):
            for j in range(1,i+1):
                a[i][j] = a[i][j-1] - a[i-1][j-1]
        return a

    def __g0(self, t0, t, heso):
        t1 = t0 - heso[2]/2*t*(t-1) - heso[3]/(2*3)*t*(t-1)*(t-2)
        return t1
    def __g1(self, t0, t, heso):
        t1 = t0 - heso[2]/2*t*(t+1) - heso[3]/(2*3)*t*(t+1)*(t+2)
        return t1
    def __g2(self, t0, t, heso):
        t1 = t0 + t*(t-1)*(heso[3]-heso[1])/4
        return t1

    def Newtontien(self):
        a = self.__Bangsaiphan()
        pp = 0 # xác định công thức lặp
        heso = []
        for i in range(4):
            heso.append(a[i][i]/a[1][1])

        t0 = (self.y-a[0][0])/a[1][1]
        x = self.__Lapdon(t0, heso, pp, self.xData[0])
        return x

    def Newtonlui(self):
        a = self.__Bangsaiphan()
        pp = 1  # xác định công thức lặp
        heso = []
        for i in range(4):
            heso.append(a[3][i]/a[3][1])

        t0 = (self.y-a[3][0])/a[3][1]
        x = self.__Lapdon(t0, heso, pp, self.xData[3])
        return x

    def Betxen(self):
        a = self.__Bangsaiphan()
        pp = 2
        heso = []
        for i in range(4):
            heso.append(a[i][1]/a[2][1])

        t0 = (self.y - a[1][0])/a[2][1]
        x = self.__Lapdon(t0, heso, pp, self.xData[1])
        return x

    def __Lapdon(self ,t0, heso, pp, x0):
        esp = 10e-9
        max = 1000
        delta = 100
        flag = 1
        i = 1
        t = t0 # xap xi dau
        x = t*self.h + x0
        # print(t0)
        while (delta > esp):
            t1 = t    
            x1 = x
            if (pp == 0):
                t =  self.__g0(t0, t1, heso)
            elif (pp == 1):
                t = self.__g1(t0, t1, heso)
            elif (pp == 2):
                t = self.__g2(t0, t1, heso)

            x = t*self.h + x0
            print("Lan lap thu", i, "co nghiem la", x)
            delta = math.fabs(x-x1)
            # x1 = x
            i += 1
            if (i > max):
                flag = 0
                break
        if (flag == 1):
            print("Ket qua:\t", x,"\n")
        else:
            print("Khong hoi tu hoac hoi tu cham!")
        return x



def dataSort(data):
    lenght = len(data)
    for i in range(lenght-1):
        for j in range(i, lenght):
            if data[i][0] > data[j][0]:
                data[i][0], data[j][0] = data[j][0], data[i][0]
                data[i][1], data[j][1] = data[j][1], data[i][1]
    return data



def FindMonotonousInterval(data):
    indexs = []
    lenght = len(data)
    index_head = 0
    index_tail = 1    
    for i in range(lenght-2):
        delta_y1 = data[i][1] - data[i+1][1]
        delta_y2 = data[i+1][1] - data[i+2][1]
        if delta_y1 * delta_y2 > 0:
            index_tail += 1
        else:
            indexs.append([index_head, index_tail])
            index_head = index_tail
            index_tail += 1
    indexs.append([index_head, index_tail])
    return np.array(indexs)

def InterpolationConditions(data):
    lenght = len(data)
    for i in range(lenght-1):
        for j in range(i+1,lenght):
            if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
                return False
            if data[i][0] == data[j][0]:
                return False
    return True

def x_equidistant(data, index):
    i = index[0]
    while i < (index[1]-1):
        delta_x1 = data[i][0] - data[i+1][0]
        delta_x2 = data[i+1][0] - data[i+2][0]
        i += 1
        if abs(delta_x1 - delta_x2) >= 10e-5:
            print("x khong cach deu")
            return False
    print("x cach deu")
    return True
       
def ConsiderApprox(data, indexs, y):

    lenght = len(indexs) - 1
    Newton = []
    Lagrange = []
    while lenght >= 0:
        if data[indexs[lenght][0]][1] > data[indexs[lenght][1]][1]: 
            # Xét trên đơn điệu giảm
            if (data[indexs[lenght][0]][1]<y or y<data[indexs[lenght][1]][1]):
                indexs = np.delete(indexs, indexs[lenght])
            else:
                print("Mang: {} => Su dung phuong phap: ".format(indexs[lenght]), end='')
                thu = Lagrange_Newton(-data, indexs[lenght], y)
                x_equidistant(data, indexs[lenght])
                if thu == True :
                    Newton.append(indexs[lenght])
                else:
                    Lagrange.append(indexs[lenght])
        else:
            # xét trên đơn điệu tăng
            if data[indexs[lenght][0]][1]>y or y>data[indexs[lenght][1]][1]:
                indexs = np.delete(indexs,indexs[lenght])
            else:
                print("Mang: {} => Su dung phuong phap: ".format(indexs[lenght]), end='')
                thu = Lagrange_Newton(data, indexs[lenght], y)
                x_equidistant(data, indexs[lenght])
                if thu == True :
                    Newton.append(indexs[lenght])
                else:
                    Lagrange.append(indexs[lenght])
        lenght -= 1
    return np.array(Newton), np.array(Lagrange)

# Đơn điệu tăng
def Lagrange_Newton(data, index, y):
    delta_y = []
    flat =  True
    if index[1] - index[0] == 1:
        print("Newton voi khoang 2 moc")
    else:
        if data[index[0]+1][1] > y and data[index[0]][1] < y:
            print("Newton Tien")
        elif data[index[1]-1][1] < y and data[index[1]][1] > y:
            print("Newton Lui")
        else:
            for i in range(index[1]-index[0]):
                d_y = abs(data[index[0]+i][1] - data[index[0]+i+1][1])
                d_x = abs(data[index[0]+i][0] - data[index[0]+i+1][0])
                delta = d_y/d_x
                delta_y.append(delta)

            ty_hieu_1 = delta_y[0]/delta_y[-1]
            
            if (ty_hieu_1 <= 1.5 and ty_hieu_1 >= 0.67):
                print('Larange')
                flat = False

            else:
                print('Newton')
    return flat

def f(he_so,x):
    f = 0
    for i in range(len(he_so)):
        f += he_so[i]*pow(x,len(he_so)-i-1)
    return f 

# 4 moc noi suy
def choosePoint(data, index, y):
    if data[index[0]][1] < data[index[0]+1][1]:
        data = -data
        y = -y
    flat_y = index[0]
    while y < data[flat_y][1]:
        flat_y += 1

    if flat_y == 1:
        index[1] = index[0] + 3
    elif flat_y == len(data)-1:
        index[0] = index[1] - 3
    else:
        index[0] = flat_y - 2
        index[1] = flat_y + 1
    return index


if __name__ == "__main__":
    # sap xep lai bo du lieu tang dan theo x
    # kiem tra dieu kien noi suy
    # xet tung khoang (L or N)

    data_sort = dataSort(data)
    data_sort_x_y = data_sort.transpose()

    for i in range(len(data_sort_x_y[0])):
        print(str(data_sort_x_y[0][i]) + "\t" + str(data_sort_x_y[1][i]))
    
    y = float(input("nhap gia tri y0: "))
    x0 = []

    if InterpolationConditions(data_sort) == False:
        print("Khong noi suy duoc!, x,y phai doi mot khac nhau")
    else:
        indexs = FindMonotonousInterval(data_sort)
        Newton, Lagrange = ConsiderApprox(data, indexs, y)
        print("Newton: ", Newton)
        print("Lagrange: ", Lagrange)

        for i in Lagrange:
            print('\nNoi suy Lagrange doan {}'.format(i))
            doan = choosePoint(data, i, y)
            print('Cac moc noi suy: \n',data_sort_x_y[:,doan[0]:(doan[1]+1)])
            poly = lagrange(data_sort_x_y[1][doan[0]:(doan[1]+1)],data_sort_x_y[0][doan[0]:(doan[1]+1)])
            print('Da thuc noi suy Larange')
            print(poly)
            he_so = Polynomial(poly).coef
            x0.append(f(he_so, y))
            print('Ket qua:\t',f(he_so, y))

        for i in Newton:
            print('\nNoi suy Newton doan {}'.format(i))
            doan = choosePoint(data, i, y)
            print('Cac moc noi suy: \n',data_sort_x_y[:,doan[0]:(doan[1]+1)])
            data_newton = data_sort_x_y[:,doan[0]:(doan[1]+1)]
            
            if doan[0] == 0:
                print("Dung Newton tien: ")
                x = newton(data_newton, y).Newtontien()
                x0.append(x)
            elif doan[1] == len(data)-1:
                print("Dung Newton lui: ")
                x = newton(data_newton, y).Newtonlui()
                x0.append(x)
            else:
                print("Dung Newton trung tam: ")
                x = newton(data_newton, y).Betxen()
                x0.append(x)

        print('Ket qua x0: ', x0)

# bieu dien data bang matplotlib
        plt.plot(data_sort_x_y[0], data_sort_x_y[1],'-')
        plt.plot(data_sort_x_y[0],[y]*len(data), '-')
        plt.title('vd')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.savefig('vd.png')
        # plt.show()
