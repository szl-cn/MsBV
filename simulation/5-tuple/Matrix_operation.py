# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:19:35 2019

@author: Administrator
"""

import numpy as np
y = np.empty([2,2],dtype = int)  #表示定义一个2*2的矩阵，该矩阵为整型

def Matrix_operation(RuleList,linenum,mat_line,Matrix):
    '''
    用嵌套列表取代矩阵,0,1元素矩阵
    '''
    mat_line = 0 #新矩阵函数行数初始化为0
    Matrix = []
    '''
    先设置k=8,这种情况下，01矩阵一共有 4+4+2+2+1 13列
    全是通配符的情况取值为0
    '''
    s = 8
    n = 40

    
    for line in range(0,linenum ,n):
        list = []#记录新的矩阵的每一行
        for i in range(1,6):
            if i==1:
                for ss in range(0,32,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][ss:ss+s] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
            if i==2:
                for ss in range(0,32,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][ss:ss+s] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
            if i==3:
                for ss in range(0,16,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][ss:ss+s] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
            if i==4:
                for ss in range(0,16,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][ss:ss+s] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
            if i==5:
                for ss in range(0,8,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][ss:ss+s] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)                        
                Matrix.append(list)
        mat_line += 1               
       # print("line",line)#查看到RuleList的函数
    return Matrix,mat_line

    '''
def count0(Matrix,mat_line):#13列
    mat0_line = 0 #新矩阵函数行数初始化为0
    Matrix0 = []
    list = [0,1,4,5,8,10,2,3,6,7,9,11,12]
    for line in range(0,mat_line):
        list1 = []
        for i in range(0,13):
            two2one = Matrix[line][list[i]]
            list1.append(two2one)
        Matrix0.append(list1)
        mat0_line += 1
    return Matrix0,mat0_line
    #print(list[0])
    '''
    '''
def count0(Matrix,mat_line):#13列,列的重排序，笨方法
    mat0_line = 0 #新矩阵函数行数初始化为0
    Matrix0 = []
    for line in range(0,mat_line):
        list = []
        two2one = Matrix[line][12]
        list.append(two2one)
        two2one = Matrix[line][11]
        list.append(two2one)
        two2one = Matrix[line][10]
        list.append(two2one)
        two2one = Matrix[line][9]
        list.append(two2one)
        two2one = Matrix[line][8]
        list.append(two2one)
        two2one = Matrix[line][7]
        list.append(two2one)
        two2one = Matrix[line][6]
        list.append(two2one)
        two2one = Matrix[line][5]
        list.append(two2one)
        two2one = Matrix[line][4]
        list.append(two2one)
        two2one = Matrix[line][3]
        list.append(two2one)
        two2one = Matrix[line][2]
        list.append(two2one)
        two2one = Matrix[line][1]
        list.append(two2one)
        two2one = Matrix[line][0]
        list.append(two2one)
        Matrix0.append(list)
        mat0_line += 1
    return Matrix0,mat0_line
    '''
def count1(Matrix,mat_line):
    mat1_line = 0 #新矩阵函数行数初始化为0
    Matrix1 = []
    '''
    考虑到一共13列，13=6*2+1
    '''
    for line in range(0,mat_line):
        list = []
        for i in range(0,6):
            two2one = Matrix[line][i] & Matrix[line][12-i]
            list.append(two2one)
        two2one = Matrix[line][6]
        list.append(two2one)
        Matrix1.append(list)
        mat1_line += 1
    return Matrix1,mat1_line
    
    
def count2(Matrix,mat_line):#优化算法1,segment rearrange optimization algorithm
    mat2_line = 0 #新矩阵函数行数初始化为0
    Matrix2 = []
    mat0_line = 0 #新矩阵函数行数初始化为0
    Matrix0 = []
    #if FileName == 'ACL1_100K'
    list = [0,1,4,5,8,10,2,3,6,7,9,11,12]
    for line in range(0,mat_line):
        list1 = []
        for i in range(0,13):
            two2one = Matrix[line][list[i]]
            list1.append(two2one)
        Matrix0.append(list1)
        mat0_line += 1
        
    for line2 in range(0,mat0_line):
        list2 = []
        for i in range(0,6):
            two2one = Matrix0[line2][i] & Matrix0[line2][12-i]
            list2.append(two2one)
        two2one = Matrix0[line2][6]
        list2.append(two2one)
        Matrix2.append(list2)
        mat2_line += 1
    return Matrix2,mat2_line,Matrix0,mat0_line#Matrix0,mat0_line为中间变量
    
    
def count3(Matrix,mat_line,FileName):#优化算法2,packet rearrange optimization algorithm
    mat3_line = 0 #新矩阵函数行数初始化为0
    Matrix3 = []
    mat00_line = 0 #新矩阵函数行数初始化为0
    Matrix00 = []
    if FileName == 'ACL1_100K':#12435
        list = [0,1,2,3,4,5,6,7,10,11,8,9,12]
    elif FileName == 'ACL2_100K':#12453
        list = [0,1,2,3,4,5,6,7,10,11,12,8,9]
    elif FileName == 'ACL3_100K':#21435
        list = [4,5,6,7,0,1,2,3,10,11,8,9,12]
    elif FileName == 'ACL4_100K':#21435
        list = [4,5,6,7,0,1,2,3,10,11,8,9,12]
    elif FileName == 'ACL5_100K':#21435
        list = [4,5,6,7,0,1,2,3,10,11,8,9,12]

    elif FileName == 'FW1_100K': #12435
        list = [0,1,2,3,4,5,6,7,10,11,8,9,12]
    elif FileName == 'FW2_100K': #13254
        list = [0,1,2,3,8,9,4,5,6,7,12,10,11]
    elif FileName == 'FW3_100K': #12435
        list = [0,1,2,3,4,5,6,7,10,11,8,9,12]
    elif FileName == 'FW4_100K':#42315
        list = [10,11,4,5,6,7,8,9,0,1,2,3,12]
    elif FileName == 'FW5_100K':#24135
        list = [4,5,6,7,10,11,0,1,2,3,8,9,12]
    
    elif FileName == 'IPC1_50K': #21435
        list = [4,5,6,7,0,1,2,3,10,11,8,9,12]
    elif FileName == 'IPC1_100K':#21435
        list = [4,5,6,7,0,1,2,3,10,11,8,9,12]
    elif FileName == 'IPC2_50K':#21534
        list = [4,5,6,7,0,1,2,3,12,8,9,10,11]
    elif FileName == 'IPC2_100K':#21534
        list = [4,5,6,7,0,1,2,3,12,8,9,10,11]
    elif FileName == '1.txt':
        list = [0,1,2,3,4,5,6,7,8,9,10,12,11]

    elif FileName == 'FW1_100K_2': #12435
        list = [0,1,2,3,4,5,6,7,10,11,8,9,12]
    elif FileName == 'FW2_100K_2': #13254
        list = [0,1,2,3,8,9,4,5,6,7,12,10,11]
    elif FileName == 'FW3_100K_2': #12435
        list = [0,1,2,3,4,5,6,7,10,11,8,9,12]
    elif FileName == 'FW4_100K_2':#43215
        list = [10,11,8,9,4,5,6,7,0,1,2,3,12]
    elif FileName == 'FW5_100K_2':#24135
        list = [4,5,6,7,10,11,0,1,2,3,8,9,12]
    
    elif FileName == 'IPC1_50K_2': #21435
        list = [4,5,6,7,0,1,2,3,10,11,8,9,12]
    elif FileName == 'IPC1_100K_2':#21435
        list = [4,5,6,7,0,1,2,3,10,11,8,9,12]
    elif FileName == 'IPC2_50K_2':#21534
        list = [4,5,6,7,0,1,2,3,12,8,9,10,11]
    elif FileName == 'IPC2_100K_2':#21534
        list = [4,5,6,7,0,1,2,3,12,8,9,10,11]
    else:
        list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    for line in range(0,mat_line):
        list1 = []
        for i in range(0,13):
            two2one = Matrix[line][list[i]]
            list1.append(two2one)
        Matrix00.append(list1)
        mat00_line += 1
        
    for line2 in range(0,mat00_line):
        list2 = []
        for i in range(0,6):
            two2one = Matrix00[line2][i] & Matrix00[line2][12-i]
            list2.append(two2one)
        two2one = Matrix00[line2][6]
        list2.append(two2one)
        Matrix3.append(list2)
        mat3_line += 1
    return Matrix3,mat3_line,Matrix00,mat00_line
    
    
    '''
def count2(Matrix,mat_line):
    mat2_line = 0 #新矩阵函数行数初始化为0
    Matrix2 = []
    for line in range(0,mat_line):
        list = []

        two2one = Matrix[line][0] & Matrix[line][12]
        list.append(two2one)
        two2one = Matrix[line][1] & Matrix[line][11]
        list.append(two2one)
        two2one = Matrix[line][3] & Matrix[line][10]
        list.append(two2one)
        two2one = Matrix[line][4] & Matrix[line][9]
        list.append(two2one)
        two2one = Matrix[line][5] & Matrix[line][7]
        list.append(two2one)
        two2one = Matrix[line][6] & Matrix[line][8]
        list.append(two2one)
        two2one = Matrix[line][2]                   
        list.append(two2one)
           
        Matrix2.append(list)
        mat2_line += 1
    return Matrix2,mat2_line
    '''
    '''
        for line in range(0,mat_line):
        list = []
        for i in range(0,13):
            if i == 0:
                two2one = Matrix[line][i] & Matrix[line][25]
            if i == 1:
                two2one = Matrix[line][i] & Matrix[line][23]
            if i == 2:
                two2one = Matrix[line][i] & Matrix[line][22]
            if i == 3:
                two2one = Matrix[line][i] & Matrix[line][19]
            if i == 4:
                two2one = Matrix[line][i] & Matrix[line][24]
            if i == 5:
                two2one = Matrix[line][i] & Matrix[line][21]
            if i == 6:
                two2one = Matrix[line][i] & Matrix[line][20]
            if i == 7:
                two2one = Matrix[line][i] & Matrix[line][17]
            if i == 8:
                two2one = Matrix[line][i] & Matrix[line][18]
            if i == 9:
                two2one = Matrix[line][i] & Matrix[line][15]
            if i == 10:
                two2one = Matrix[line][i] & Matrix[line][14]
            if i == 11:
                two2one = Matrix[line][i] & Matrix[line][13]
            if i == 12:
                two2one = Matrix[line][i] & Matrix[line][12]
                '''