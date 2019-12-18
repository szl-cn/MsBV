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
    先设置k=8,这种情况下，
    01矩阵一共有 2+6+6+2+2+1+4+4+1+1+2+2  33列
    全是通配符的情况取值为0
    '''
    s = 8
    n = 40
    '''
                            'in_port':(0, 16), \
                            'dl_src':(1, 48), \
                            'dl_dst':(2, 48), \
                            'eth_type':(3, 16), \
                            'dl_vlan':(4, 12), \
                            'dl_vlan_pcp':(5, 3), \
                            'nw_src':(6, 32), \
                            'nw_dst':(7, 32), \
                            'nw_tos':(8, 6), \
                            'nw_proto':(9, 8), \
                            'tp_src':(10, 16), \
                            'tp_dst':(11, 16)}
    '''
    for line in range(0,linenum ,n):
        list = []#记录新的矩阵的每一行
        for i in range(1,13):
            if i==1:
                for ss in range(0,16,s):
                    flag = 0
                    for t in range(0,n):
                        #print(RuleList[line][i][ss:ss+s])
                        if RuleList[line][i][ss:ss+s] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
            if i==2:
                for ss in range(0,48,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][ss:ss+s] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
            if i==3:
                for ss in range(0,48,s):
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
                #for ss in range(0,12,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][0:8] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
                        
                        if RuleList[line][i][8:12] != '****':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
                        
            if i==6:
                #for ss in range(0,3):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][0:3] != '***':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
            if i==7:
                for ss in range(0,32,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][ss:ss+s] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
            if i==8:
                for ss in range(0,32,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][ss:ss+s] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
            if i==9:
                #for ss in range(0,6,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][0:6] != '******':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
            if i==10:
                for ss in range(0,8,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][ss:ss+s] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)                                      
            if i==11:
                for ss in range(0,16,s):
                    flag = 0
                    for t in range(0,n):
                        if RuleList[line][i][ss:ss+s] != '********':
                            flag = 1               
                    if flag==0:
                        list.append(0)
                    else:
                        list.append(1)
            if i==12:
                for ss in range(0,16,s):
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
    
def count1(Matrix,mat_line):
    mat1_line = 0 #新矩阵函数行数初始化为0
    Matrix1 = []

    '''
    考虑到一共33列，33=16*2+1
    '''
    for line in range(0,mat_line):
        list = []
        for i in range(0,16):
            two2one = Matrix[line][i] & Matrix[line][32-i]
            list.append(two2one)
        two2one = Matrix[line][16]
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
    list = [18,27,0,2,3,4,8,9,10,14,16,19,20,23,24,29,31,1,5,6,7,11,12,13,15,17,21,22,25,26,30,32,28]
    for line in range(0,mat_line):
        list1 = []
        for i in range(0,33):
            two2one = Matrix[line][list[i]]
            list1.append(two2one)
        Matrix0.append(list1)
        mat0_line += 1
        
    for line2 in range(0,mat0_line):
        list2 = []
        for i in range(0,16):
            two2one = Matrix0[line2][i] & Matrix0[line2][32-i]
            list2.append(two2one)
        two2one = Matrix0[line2][16]
        list2.append(two2one)
        Matrix2.append(list2)
        mat2_line += 1
    return Matrix2,mat2_line,Matrix0,mat0_line#Matrix0,mat0_line为中间变量
    
    
def count3(Matrix,mat_line,FileName):#优化算法2,packet rearrange optimization algorithm
    mat3_line = 0 #新矩阵函数行数初始化为0
    Matrix3 = []
    mat00_line = 0 #新矩阵函数行数初始化为0
    Matrix00 = []
    if FileName == 'OF1_100K_1':#8 4 10 3 12 7 2 11 1 5 6 9
        list = [23,24,25,26,14,15,28,8,9,10,11,12,13,31,32,19,20,21,22,2,3,4,5,6,7,29,30,0,1,16,17,18,27]
    elif FileName == 'OF1_100K_2':#8 4 10 3 12 7 2 11 1 5 6 9
        list = [23,24,25,26,14,15,28,8,9,10,11,12,13,31,32,19,20,21,22,2,3,4,5,6,7,29,30,0,1,16,17,18,27]
    elif FileName == 'OF1_100K_3':#8 12 4 10 3 7 2 11 1 5 6 9
        list = [23,24,25,26,31,32,14,15,28,8,9,10,11,12,13,19,20,21,22,2,3,4,5,6,7,29,30,0,1,16,17,18,27]
    elif FileName == 'OF1_100K_4':#8 4 10 3 12 7 2 11 1 5 6 9
        list = [23,24,25,26,14,15,28,8,9,10,11,12,13,31,32,19,20,21,22,2,3,4,5,6,7,29,30,0,1,16,17,18,27]
    elif FileName == 'OF1_100K_5':#8 4 10 3 12 7 2 11 1 5 6 9
        list = [23,24,25,26,14,15,28,8,9,10,11,12,13,31,32,19,20,21,22,2,3,4,5,6,7,29,30,0,1,16,17,18,27]
    elif FileName == 'OF1_100K_6':#8 4 10 3 12 7 2 11 1 5 6 9
        list = [23,24,25,26,14,15,28,8,9,10,11,12,13,31,32,19,20,21,22,2,3,4,5,6,7,29,30,0,1,16,17,18,27]
    
    elif FileName == 'OF2_100K_1':#8 3 12 7 11 4 10 2 1 5 6 9
        list = [23,24,25,26,8,9,10,11,12,13,31,32,19,20,21,22,29,30,14,15,28,2,3,4,5,6,7,0,1,16,17,18,27]
    elif FileName == 'OF2_100K_2':#8 3 12 7 11 4 10 2 1 5 6 9
        list = [23,24,25,26,8,9,10,11,12,13,31,32,19,20,21,22,29,30,14,15,28,2,3,4,5,6,7,0,1,16,17,18,27]
    elif FileName == 'OF2_100K_3':#8 12 3 11 7 4 10 2 1 5 6 9
        list = [23,24,25,26,31,32,8,9,10,11,12,13,29,30,19,20,21,22,14,15,28,2,3,4,5,6,7,0,1,16,17,18,27]
    elif FileName == 'OF2_100K_4':#8 3 12 7 11 4 10 2 1 5 6 9
        list = [23,24,25,26,8,9,10,11,12,13,31,32,19,20,21,22,29,30,14,15,28,2,3,4,5,6,7,0,1,16,17,18,27]
    elif FileName == 'OF2_100K_5':#8 3 12 7 11 4 10 2 1 5 6 9
        list = [23,24,25,26,8,9,10,11,12,13,31,32,19,20,21,22,29,30,14,15,28,2,3,4,5,6,7,0,1,16,17,18,27]
    #elif FileName == 'OF1_10K'#8 4 10 3 12 7 2 11 1 5
    
    elif FileName == '2.txt':#用来测试
        list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,31,32,27,28]
    else:
        list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,31,32,27,28]
    for line in range(0,mat_line):
        list1 = []
        for i in range(0,33):
            two2one = Matrix[line][list[i]]
            list1.append(two2one)
        Matrix00.append(list1)
        mat00_line += 1
        
    for line2 in range(0,mat00_line):
        list2 = []
        for i in range(0,16):
            two2one = Matrix00[line2][i] & Matrix00[line2][32-i]
            list2.append(two2one)
        two2one = Matrix00[line2][16]
        list2.append(two2one)
        Matrix3.append(list2)
        mat3_line += 1
    return Matrix3,mat3_line,Matrix00,mat00_line
    
    
    
    '''
def count2(Matrix,mat_line):#优化算法1，旧方法，留存
    mat2_line = 0 #新矩阵函数行数初始化为0
    Matrix2 = []
    for line in range(0,mat_line):
        list = []

        two2one = Matrix[line][0] & Matrix[line][27]           
        list.append(two2one)
        two2one = Matrix[line][2] & Matrix[line][18]
        list.append(two2one)
        two2one = Matrix[line][3] & Matrix[line][32]
        list.append(two2one)
        two2one = Matrix[line][4] & Matrix[line][30]
        list.append(two2one)
        two2one = Matrix[line][5] & Matrix[line][28]
        list.append(two2one)
        two2one = Matrix[line][6] & Matrix[line][31]
        list.append(two2one)
        two2one = Matrix[line][7] & Matrix[line][29]
        list.append(two2one)
        two2one = Matrix[line][8] & Matrix[line][26]
        list.append(two2one)
        two2one = Matrix[line][9] & Matrix[line][25]
        list.append(two2one)
        two2one = Matrix[line][10] & Matrix[line][22]
        list.append(two2one)
        two2one = Matrix[line][11] & Matrix[line][24]
        list.append(two2one)
        two2one = Matrix[line][12] & Matrix[line][23]
        list.append(two2one)
        two2one = Matrix[line][13] & Matrix[line][20]
        list.append(two2one)
        two2one = Matrix[line][14] & Matrix[line][21]
        list.append(two2one)
        two2one = Matrix[line][15] & Matrix[line][19]
        list.append(two2one)
        two2one = Matrix[line][16] & Matrix[line][17]
        list.append(two2one)
        two2one = Matrix[line][1]
        list.append(two2one)
        
        Matrix2.append(list)
        mat2_line += 1
    return Matrix2,mat2_line
    '''
    
    
    '''
    #FileName = 'OF1_5K' #8 4 10 3 12 7 2 11 1 5 6 9
def count3(Matrix,mat_line):#FileName = 'OF1_100K' 
    mat3_line = 0 #新矩阵函数行数初始化为0
    Matrix3 = []
    for line in range(0,mat_line):
        list = []
        two2one = Matrix[line][0] & Matrix[line][15]           
        list.append(two2one)
        two2one = Matrix[line][1] & Matrix[line][14]
        list.append(two2one)
        two2one = Matrix[line][2] & Matrix[line][31]
        list.append(two2one)
        two2one = Matrix[line][3] & Matrix[line][13]
        list.append(two2one)
        two2one = Matrix[line][4] & Matrix[line][12]
        list.append(two2one)
        two2one = Matrix[line][5] & Matrix[line][11]
        list.append(two2one)
        two2one = Matrix[line][6] & Matrix[line][10]
        list.append(two2one)
        two2one = Matrix[line][7] & Matrix[line][9]
        list.append(two2one)
        two2one = Matrix[line][8] & Matrix[line][29]
        list.append(two2one)
        two2one = Matrix[line][16] & Matrix[line][26]
        list.append(two2one)
        two2one = Matrix[line][17] & Matrix[line][25]
        list.append(two2one)
        two2one = Matrix[line][18] & Matrix[line][24]
        list.append(two2one)
        two2one = Matrix[line][19] & Matrix[line][21]
        list.append(two2one)
        two2one = Matrix[line][22] & Matrix[line][32]
        list.append(two2one)
        two2one = Matrix[line][23] & Matrix[line][27]
        list.append(two2one)
        two2one = Matrix[line][28] & Matrix[line][30]
        list.append(two2one)
        two2one = Matrix[line][20]
        list.append(two2one)
        Matrix3.append(list)
        mat3_line += 1
    return Matrix3,mat3_line
    '''
    
    '''
    #FileName = 'OF2_5K' or 'OF2_10K' 
def count3(Matrix,mat_line):#FileName = 'OF2_5K' or 'OF2_10K' 
    mat3_line = 0 #新矩阵函数行数初始化为0
    Matrix3 = []
    for line in range(0,mat_line):
        list = []

        two2one = Matrix[line][0] & Matrix[line][13]           
        list.append(two2one)
        two2one = Matrix[line][1] & Matrix[line][12]
        list.append(two2one)
        two2one = Matrix[line][2] & Matrix[line][20]
        list.append(two2one)
        two2one = Matrix[line][3] & Matrix[line][19]
        list.append(two2one)
        two2one = Matrix[line][4] & Matrix[line][26]
        list.append(two2one)
        two2one = Matrix[line][5] & Matrix[line][25]
        list.append(two2one)
        two2one = Matrix[line][6] & Matrix[line][24]
        list.append(two2one)
        two2one = Matrix[line][7] & Matrix[line][23]
        list.append(two2one)
        two2one = Matrix[line][8] & Matrix[line][27]
        list.append(two2one)
        two2one = Matrix[line][9] & Matrix[line][18]
        list.append(two2one)
        two2one = Matrix[line][10] & Matrix[line][17]
        list.append(two2one)
        two2one = Matrix[line][11] & Matrix[line][16]
        list.append(two2one)
        two2one = Matrix[line][14] & Matrix[line][31]
        list.append(two2one)
        two2one = Matrix[line][15] & Matrix[line][22]
        list.append(two2one)
        two2one = Matrix[line][21] & Matrix[line][28]
        list.append(two2one)
        two2one = Matrix[line][30] & Matrix[line][32]
        list.append(two2one)
        two2one = Matrix[line][29]
        list.append(two2one)
        
        Matrix3.append(list)
        mat3_line += 1
    return Matrix3,mat3_line
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
    '''
def count3(Matrix,mat_line):#FileName = 'OF2_100K' #8 3 12 7 11 4 10 2 1 5 6 9
    mat3_line = 0 #新矩阵函数行数初始化为0
    Matrix3 = []
    for line in range(0,mat_line):
        list = []

        two2one = Matrix[line][0] & Matrix[line][9]           
        list.append(two2one)
        two2one = Matrix[line][1] & Matrix[line][8]
        list.append(two2one)
        two2one = Matrix[line][2] & Matrix[line][32]
        list.append(two2one)
        two2one = Matrix[line][3] & Matrix[line][31]
        list.append(two2one)
        two2one = Matrix[line][4] & Matrix[line][13]
        list.append(two2one)
        two2one = Matrix[line][5] & Matrix[line][12]
        list.append(two2one)
        two2one = Matrix[line][6] & Matrix[line][11]
        list.append(two2one)
        two2one = Matrix[line][7] & Matrix[line][10]
        list.append(two2one)
        two2one = Matrix[line][14] & Matrix[line][21]
        list.append(two2one)
        two2one = Matrix[line][15] & Matrix[line][20]
        list.append(two2one)
        two2one = Matrix[line][16] & Matrix[line][26]
        list.append(two2one)
        two2one = Matrix[line][17] & Matrix[line][25]
        list.append(two2one)
        two2one = Matrix[line][18] & Matrix[line][24]
        list.append(two2one)
        two2one = Matrix[line][19] & Matrix[line][28]
        list.append(two2one)
        two2one = Matrix[line][22] & Matrix[line][30]
        list.append(two2one)
        two2one = Matrix[line][23] & Matrix[line][27]
        list.append(two2one)
        two2one = Matrix[line][29]
        list.append(two2one)
        
        Matrix3.append(list)
        mat3_line += 1
    return Matrix3,mat3_line
    '''