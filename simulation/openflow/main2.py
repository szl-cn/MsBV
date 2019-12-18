# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:15:56 2019

@author: Administrator
"""
from Init_OpenFlow import Init_OpenFlow
from Matrix_operation2 import Matrix_operation,count1,count2,count3
import matplotlib.pyplot as plt
import numpy as np

def main():
    '''
    按行解析得到0、1、*矩阵
    '''
    #FileName = '2.txt'
    #list1312 = [,,,]
    #for filo in lsidfs

    #FileName = 'OF1_5K' #8 3 4 10 12 7 2 11 1 5 6 9
    #FileName = 'OF1_10K'#8 4 10 3 12 7 2 11 1 5 6 9
    #FileName = 'OF2_5K'#3 8 7 12 11 4 10 2 1 5 6 9
    #FileName = 'OF2_10K'#3 8 7 12 11 4 10 2 1 5 6 9
    #FileName = 'OF1_20K_new'#8 3 4 10 12 7 2 11 1 5 6 9
    
    FileName = 'OF1_100K_1'#8 4 10 3 12 7 2 11 1 5 6 9
    #FileName = 'OF1_100K_2'#8 4 10 3 12 7 2 11 1 5 6 9
    #FileName = 'OF1_100K_3'#8 12 4 10 3 7 2 11 1 5 6 9
    #FileName = 'OF1_100K_4'#8 4 10 3 12 7 2 11 1 5 6 9
    #FileName = 'OF1_100K_5'#8 4 10 3 12 7 2 11 1 5 6 9
    #FileName = 'OF1_100K_6'#8 4 10 3 12 7 2 11 1 5 6 9
    
    #FileName = 'OF2_100K_1'#8 3 12 7 11 4 10 2 1 5 6 9
    #FileName = 'OF2_100K_2'#8 3 12 7 11 4 10 2 1 5 6 9
    #FileName = 'OF2_100K_3'#8 12 3 11 7 4 10 2 1 5 6 9
    #FileName = 'OF2_100K_4'#8 3 12 7 11 4 10 2 1 5 6 9
    #FileName = 'OF2_100K_5'#8 3 12 7 11 4 10 2 1 5 6 9
    
    RuleList, linenum = Init_OpenFlow(FileName)

    '''
    0,1,*三元素矩阵写入文本test_of.txt
    '''
    fo = open("of-openflow.txt", "w")
    for i in range(0,linenum):
        fo.write(str(RuleList[i])+'\n')
        #fo.write(RuleList[i][1]+RuleList[i][2]+RuleList[i][3]+RuleList[i][4]+RuleList[i][5]+'\n')
    fo.close()
    print("linenum = "+str(linenum))
    '''
    得到0,1矩阵
    '''
    Matrix = []
    mat_line = 0
    Matrix,mat_line = Matrix_operation(RuleList,linenum,mat_line,Matrix)
    print("mat_line = "+str(mat_line))
    '''
    0,1双元素矩阵写入文本test_2.txt
    '''
    f1 = open("of-initial state.txt", "w")
    for i in range(0,mat_line):
        f1.write(str(Matrix[i])+'\n')
    f1.close()        
    
    Matrix1,mat1_line = count1(Matrix,mat_line)
 #   print(Matrix1,mat1_line)
    f2 = open("of-final state.txt", "w")
    for i in range(0,mat1_line):
        f2.write(str(Matrix1[i])+'\n')
    f2.close()
    print("mat1_line = "+str(mat1_line))
    

    
    
    #计算每个字段的通配符比例
    count_1,count_2,count_3,count_4,count_5,count_6 =0,0,0,0,0,0
    count_7,count_8,count_9,count_10,count_11,count_12 =0,0,0,0,0,0
    
    rate_1,rate_2,rate_3,rate_4,rate_5,rate_6 =0,0,0,0,0,0
    rate_7,rate_8,rate_9,rate_10,rate_11,rate_12 =0,0,0,0,0,0

    for line in range(0,linenum):
        for i in range(0,16):
            if i==1:
                for ss in range(0,16):
                    if RuleList[line][1][ss]== '*':          
                        count_1 +=1
                        rate_1 = count_1/(16*linenum)
            if i==2:
                for ss in range(0,48):
                    if RuleList[line][2][ss]== '*':          
                        count_2 +=1
                        rate_2 = count_2/(48*linenum)
            if i==3:
                for ss in range(0,48):
                    if RuleList[line][3][ss]== '*':          
                        count_3 +=1
                        rate_3 = count_3/(48*linenum)
            if i==4:
                for ss in range(0,16):
                    if RuleList[line][4][ss]== '*':          
                        count_4 +=1
                        rate_4 = count_4/(16*linenum)
            if i==5:
                for ss in range(0,12):
                    if RuleList[line][5][ss]== '*':          
                        count_5 +=1
                        rate_5 = count_5/(12*linenum)
            if i==6:
                for ss in range(0,3):
                    if RuleList[line][6][ss]== '*':          
                        count_6 +=1
                        rate_6 = count_6/(3*linenum)
            if i==7:
                for ss in range(0,32):
                    if RuleList[line][7][ss]== '*':          
                        count_7 +=1
                        rate_7 = count_7/(32*linenum)
            if i==8:
                for ss in range(0,32):
                    if RuleList[line][i][ss]== '*':          
                        count_8 +=1
                        rate_8 = count_8/(32*linenum)
            if i==9:
                for ss in range(0,6):
                    if RuleList[line][9][ss]== '*':          
                        count_9 +=1
                        rate_9 = count_9/(6*linenum)
            if i==10:
                for ss in range(0,8):
                    if RuleList[line][10][ss]== '*':          
                        count_10 +=1
                        rate_10 = count_10/(8*linenum)
            if i==11:
                for ss in range(0,16):
                    if RuleList[line][11][ss]== '*':          
                        count_11 +=1
                        rate_11 = count_11/(16*linenum)
            if i==12:
                for ss in range(0,16):
                    if RuleList[line][12][ss]== '*':          
                        count_12 +=1
                        rate_12 = count_12/(16*linenum)
    print("count_1 ="+str(count_1))
    print("rate_1 ="+str(rate_1))
    print("count_2 ="+str(count_2))
    print("rate_2 ="+str(rate_2))
    print("count_3 ="+str(count_3))
    print("rate_3 ="+str(rate_3))
    print("count_4 ="+str(count_4))
    print("rate_4 ="+str(rate_4))
    print("count_5 ="+str(count_5))
    print("rate_5 ="+str(rate_5))
    print("count_6 ="+str(count_6))
    print("rate_6 ="+str(rate_6))
    print("count_7 ="+str(count_7))
    print("rate_7 ="+str(rate_7))
    print("count_8 ="+str(count_8))
    print("rate_8 ="+str(rate_8))
    print("count_9 ="+str(count_9))
    print("rate_9 ="+str(rate_9))
    print("count_10 ="+str(count_10))
    print("rate_10 ="+str(rate_10))
    print("count_11 ="+str(count_11))
    print("rate_11 ="+str(rate_11))
    print("count_12 ="+str(count_12))
    print("rate_12 ="+str(rate_12))
    

    #比较OpenFlow规则集中12个字段中通配符占比大小比较，从小至大
    
    lt = [rate_1, rate_2, rate_3, rate_4, rate_5, rate_6, rate_7, rate_8, rate_9, rate_10, rate_11, rate_12]
    #print(lt)
    lt1 = ["rate_1", "rate_2", "rate_3", "rate_4", "rate_5", "rate_6", "rate_7", "rate_8", "rate_9", "rate_10", "rate_11", "rate_12"]
    n= len(lt)
    for x in range(n-1):
        for y in range(n-1-x):
          if lt[y]>lt[y+1]:
             lt[y],lt[y+1]=lt[y+1],lt[y]
             lt1[y],lt1[y+1]=lt1[y+1],lt1[y]
    print(lt1)
    print()
    
    
    #统计数据，画图
    #方案1
    #故障数 m1，故障率m_r
    
    
    
    m11 = 0
    for i in range(0,mat1_line):
        c11_count = 0
        for j in range(0,len(Matrix1[0])-1):
            if Matrix1[i][j] == 1:            
                c11_count += 1
        if c11_count>=3:
            m11 +=1
    m_r =  m11/mat1_line      
    print("m11 = "+str(m11))
    print("m_r = "+str(m_r))  
    
    '''
    方案1改进型
    '''
    m12 = 0

    list1 = [0,2,4,6,8,10,12,14]
    list2 = [1,3,5,7,9,11,13,15]

    for i in range(0,mat1_line):
        c12_1_count = 0
        c12_2_count = 0
        for j in range(0,len(Matrix1[0])-1):
            if Matrix1[i][j] == 1 and j in list1:
                c12_1_count += 1
            if Matrix1[i][j] == 1 and j in list2:
                c12_2_count += 1
        if c12_1_count >= 3:
            m12 = m12 + 1
        if c12_2_count >= 3:
            m12 = m12 + 1
    m_r12 = m12/(2*mat1_line)
    
    print("m12 = "+str(m12))
    print("m_r12 = "+str(m_r12))
    
    '''
    #方案1，3条总线
    '''
    m13 = 0
    list1 = [0,3,6,9,12,15]
    list2 = [1,4,7,10,13]
    list3 = [2,5,8,11,14]
    for i in range(0,mat1_line):
        c13_1_count = 0
        c13_2_count = 0
        c13_3_count = 0
        for j in range(0,len(Matrix1[0])-1):
            if Matrix1[i][j] == 1 and j in list1:
                c13_1_count += 1
            if Matrix1[i][j] == 1 and j in list2:
                c13_2_count += 1
            if Matrix1[i][j] == 1 and j in list3:
                c13_3_count += 1    
        if c13_1_count >= 3:
            m13 = m13 + 1
        if c13_2_count >= 3:
            m13 = m13 + 1
        if c13_3_count >= 3:
            m13 = m13 + 1
    m_r13 = m13/(3*mat1_line)
    
    print("m13 = "+str(m13))
    print("m_r13 = "+str(m_r13))
    print()
    '''
    #方案1，4条总线
    '''
    m14 = 0 
    aa = 0
    bb = 0
    cc = 0
    dd = 0
    list1 = [0,4,8,12]
    list2 = [1,5,9,13]
    list3 = [2,6,10,14]
    list4 = [3,7,11,15]
    '''
    list1 = [0,1,2,3]
    list2 = [4,5,6]
    list3 = [7,8,9]
    list4 = [10,11,12]
    '''
    for i in range(0,mat1_line):
        c14_1_count = 0
        c14_2_count = 0
        c14_3_count = 0
        c14_4_count = 0
        for j in range(0,len(Matrix1[0])-1):
            if Matrix1[i][j] == 1 and j in list1:
                c14_1_count += 1
            if Matrix1[i][j] == 1 and j in list2:
                c14_2_count += 1
            if Matrix1[i][j] == 1 and j in list3:
                c14_3_count += 1
            if Matrix1[i][j] == 1 and j in list4:
                c14_4_count += 1
        if c14_1_count >= 3:
            aa = aa + 1
            m14 = m14 + 1
        if c14_2_count >= 3:
            bb = bb + 1
            m14 = m14 + 1
        if c14_3_count >= 3:
            cc = cc + 1
            m14 = m14 + 1
        if c14_4_count >= 3:
            dd = dd + 1
            m14 = m14 + 1
    m_r14 = m14/(4*mat1_line)
    
    print("m14 = "+str(m14))
    print("m_r14 = "+str(m_r14))
    print("aa = "+str(aa))
    print("bb = "+str(bb))
    print("cc = "+str(cc))
    print("dd = "+str(dd))
    print()
    
    
    m15 = 0
    list1 = [0,5,10,15]
    list2 = [1,6,11]
    list3 = [2,7,12]
    list4 = [3,8,13]
    list5 = [4,9,14]
    
    for i in range(0,mat1_line):
        c15_1_count = 0
        c15_2_count = 0
        c15_3_count = 0
        c15_4_count = 0
        c15_5_count = 0
        for j in range(0,len(Matrix1[0])-1):
            if Matrix1[i][j] == 1 and j in list1:
                c15_1_count += 1
            if Matrix1[i][j] == 1 and j in list2:
                c15_2_count += 1
            if Matrix1[i][j] == 1 and j in list3:
                c15_3_count += 1
            if Matrix1[i][j] == 1 and j in list4:
                c15_4_count += 1
            if Matrix1[i][j] == 1 and j in list5:
                c15_5_count += 1
        if c15_1_count >= 3:
            m15 = m15 + 1
        if c15_2_count >= 3:
            m15 = m15 + 1
        if c15_3_count >= 3:
            m15 = m15 + 1
        if c15_4_count >= 3:
            m15 = m15 + 1
        if c15_5_count >= 3:
            m15 = m15 + 1
    m_r15 = m15/(5*mat1_line)
    
    print("m15 = "+str(m15))
    print("m_r15 = "+str(m_r15))      
    
    m16 = 0
    list1 = [0,6,12]
    list2 = [1,7,13]
    list3 = [2,8,14]
    list4 = [3,9,15]
    list5 = [4,10]
    list6 = [5,11]    
    for i in range(0,mat1_line):
        c16_1_count = 0
        c16_2_count = 0
        c16_3_count = 0
        c16_4_count = 0
        c16_5_count = 0
        c16_6_count = 0
        for j in range(0,len(Matrix1[0])-1):
            if Matrix1[i][j] == 1 and j in list1:
                c16_1_count += 1
            if Matrix1[i][j] == 1 and j in list2:
                c16_2_count += 1
            if Matrix1[i][j] == 1 and j in list3:
                c16_3_count += 1
            if Matrix1[i][j] == 1 and j in list4:
                c16_4_count += 1
            if Matrix1[i][j] == 1 and j in list5:
                c16_5_count += 1
            if Matrix1[i][j] == 1 and j in list6:
                c16_6_count += 1
        if c16_1_count >= 3:
            m16 = m16 + 1
        if c16_2_count >= 3:
            m16 = m16 + 1
        if c16_3_count >= 3:
            m16 = m16 + 1
        if c16_4_count >= 3:
            m16 = m16 + 1
        if c16_5_count >= 3:
            m16 = m16 + 1
        if c16_6_count >= 3:
            m16 = m16 + 1
    m_r16 = m16/(6*mat1_line)
    
    print("m16 = "+str(m16))
    print("m_r16 = "+str(m_r16))      

    m17 = 0
    list1 = [0,7,14]
    list2 = [1,8,15]
    list3 = [2,9]
    list4 = [3,10]
    list5 = [4,11]
    list6 = [5,12]    
    list7 = [6,13]
    for i in range(0,mat1_line):
        c17_1_count = 0
        c17_2_count = 0
        c17_3_count = 0
        c17_4_count = 0
        c17_5_count = 0
        c17_6_count = 0
        c17_7_count = 0
        for j in range(0,len(Matrix1[0])-1):
            if Matrix1[i][j] == 1 and j in list1:
                c17_1_count += 1
            if Matrix1[i][j] == 1 and j in list2:
                c17_2_count += 1
            if Matrix1[i][j] == 1 and j in list3:
                c17_3_count += 1
            if Matrix1[i][j] == 1 and j in list4:
                c17_4_count += 1
            if Matrix1[i][j] == 1 and j in list5:
                c17_5_count += 1
            if Matrix1[i][j] == 1 and j in list6:
                c17_6_count += 1
            if Matrix1[i][j] == 1 and j in list7:
                c17_7_count += 1
        if c17_1_count >= 3:
            m17= m17+ 1
        if c17_2_count >= 3:
            m17= m17+ 1
        if c17_3_count >= 3:
            m17= m17+ 1
        if c17_4_count >= 3:
            m17= m17+ 1
        if c17_5_count >= 3:
            m17= m17+ 1
        if c17_6_count >= 3:
            m17= m17+ 1
        if c17_7_count >= 3:
            m17= m17+ 1
    m_r17 = m17/(7*mat1_line) 
    print("m17 = "+str(m17))
    print("m_r17 = "+str(m_r17))      

    m18 = 0
    list1 = [0,8]
    list2 = [1,9]
    list3 = [2,10]
    list4 = [3,11]
    list5 = [4,12]
    list6 = [5,13]    
    list7 = [6,14]
    list8 = [7,15]
    for i in range(0,mat1_line):
        c18_1_count = 0
        c18_2_count = 0
        c18_3_count = 0
        c18_4_count = 0
        c18_5_count = 0
        c18_6_count = 0
        c18_7_count = 0
        c18_8_count = 0
        for j in range(0,len(Matrix1[0])-1):
            if Matrix1[i][j] == 1 and j in list1:
                c18_1_count += 1
            if Matrix1[i][j] == 1 and j in list2:
                c18_2_count += 1
            if Matrix1[i][j] == 1 and j in list3:
                c18_3_count += 1
            if Matrix1[i][j] == 1 and j in list4:
                c18_4_count += 1
            if Matrix1[i][j] == 1 and j in list5:
                c18_5_count += 1
            if Matrix1[i][j] == 1 and j in list6:
                c18_6_count += 1
            if Matrix1[i][j] == 1 and j in list7:
                c18_7_count += 1
            if Matrix1[i][j] == 1 and j in list8:
                c18_8_count += 1
        if c18_1_count >= 3:
            m18= m18+ 1
        if c18_2_count >= 3:
            m18= m18+ 1
        if c18_3_count >= 3:
            m18= m18+ 1
        if c18_4_count >= 3:
            m18= m18+ 1
        if c18_5_count >= 3:
            m18= m18+ 1
        if c18_6_count >= 3:
            m18= m18+ 1
        if c18_7_count >= 3:
            m18= m18+ 1
        if c18_8_count >= 3:
            m18= m18+ 1
    m_r18 = m18/(8*mat1_line) 
    print("m18 = "+str(m18))
    print("m_r18 = "+str(m_r18))      
    print()             

                          
    '''
    方案2
    '''
    #Matrix2,mat2_line = count2(Matrix,mat_line)
    Matrix2,mat2_line,Matrix0,mat0_line = count2(Matrix,mat_line)
    
    f3 = open("of--segment-final state.txt", "w")
    for i in range(0,mat2_line):
        f3.write(str(Matrix2[i])+'\n')
    f3.close()
    
    f0 = open("of-segment-intermediate state.txt", "w")
    for i in range(0,mat0_line):
        f0.write(str(Matrix0[i])+'\n')
    f0.close()
    print("mat0_line = "+str(mat0_line))
    '''
    故障数 m2，故障率m_r2
    '''
    m21 = 0
    for i in range(0,mat2_line):
        c21_count = 0
        for j in range(0,len(Matrix2[0])-1):
            if Matrix2[i][j] == 1:
                c21_count += 1
        if c21_count >= 3:
            m21 = m21 + 1
    m_r21 = m21/mat2_line
    
    print("m21 = "+str(m21))
    print("m_r21 = "+str(m_r21))    
    print("len(Matrix2[0] = "+str(len(Matrix2[0])))
    
    '''
    方案2，2条总线
    '''
    m22 = 0
    list1 = [0,2,4,6,8,10,12,14]
    list2 = [1,3,5,7,9,11,13,15]
    for i in range(0,mat2_line):
        c22_1_count = 0
        c22_2_count = 0
        for j in range(0,len(Matrix2[0])-1):
            if Matrix2[i][j] == 1 and j in list1:
                c22_1_count += 1
            if Matrix2[i][j] == 1 and j in list2:
                c22_2_count += 1
        if c22_1_count >= 3:
            m22 = m22 + 1
        if c22_2_count >= 3:
            m22 = m22 + 1
    m_r22 = m22/(2*mat2_line)
    
    print("m22 = "+str(m22))
    print("m_r22 = "+str(m_r22))    
    '''
    #方案2，3条总线
    '''
    m23 = 0
    
    list1 = [0,3,6,9,12,15]
    list2 = [1,4,7,10,13]
    list3 = [2,5,8,11,14]

    '''
    list1 = [0,1,2,3,4]
    list2 = [5,6,7,8]
    list3 = [9,10,11,12]
    '''
    for i in range(0,mat2_line):
        c23_1_count = 0
        c23_2_count = 0
        c23_3_count = 0
        for j in range(0,len(Matrix2[0])-1):
            if Matrix2[i][j] == 1 and j in list1:
                c23_1_count += 1
            if Matrix2[i][j] == 1 and j in list2:
                c23_2_count += 1
            if Matrix2[i][j] == 1 and j in list3:
                c23_3_count += 1    
        if c23_1_count >= 3:
            m23 = m23 + 1
        if c23_2_count >= 3:
            m23 = m23 + 1
        if c23_3_count >= 3:
            m23 = m23 + 1
    m_r23 = m23/(3*mat2_line)
    
    print("m23 = "+str(m23))
    print("m_r23 = "+str(m_r23)) 

    m24 = 0
   
    list1 = [0,4,8,12]
    list2 = [1,5,9,13]
    list3 = [2,6,10,14]
    list4 = [3,7,11,15]
    '''
    list1 = [0,12,4]
    list2 = [1,11,5]
    list3 = [2,10,6]
    list4 = [3,9,7,8]
    '''
    for i in range(0,mat2_line):
        c24_1_count = 0
        c24_2_count = 0
        c24_3_count = 0
        c24_4_count = 0
        for j in range(0,len(Matrix2[0])-1):
            if Matrix2[i][j] == 1 and j in list1:
                c24_1_count += 1
            if Matrix2[i][j] == 1 and j in list2:
                c24_2_count += 1
            if Matrix2[i][j] == 1 and j in list3:
                c24_3_count += 1
            if Matrix2[i][j] == 1 and j in list4:
                c24_4_count += 1
        if c24_1_count >= 3:
            m24 = m24 + 1
        if c24_2_count >= 3:
            m24 = m24 + 1
        if c24_3_count >= 3:
            m24 = m24 + 1
        if c24_4_count >= 3:
            m24 = m24 + 1
    m_r24 = m24/(4*mat2_line)
    
    print("m24 = "+str(m24))
    print("m_r24 = "+str(m_r24))


    m25 = 0
    '''
    list1 = [0,12,5]
    list2 = [1,11,6]
    list3 = [2,10,7]
    list4 = [3,9]
    list5 = [4,8]
    
    list1 = [0,12]
    list2 = [1,11,5]
    list3 = [2,10,6]
    list4 = [3,9,7]
    list5 = [4,8]
    '''
    list1 = [0,5,10,15]
    list2 = [1,6,11]
    list3 = [2,7,12]
    list4 = [3,8,13]
    list5 = [4,9,14]
    
    for i in range(0,mat2_line):
        c25_1_count = 0
        c25_2_count = 0
        c25_3_count = 0
        c25_4_count = 0
        c25_5_count = 0
        for j in range(0,len(Matrix2[0])-1):
            if Matrix2[i][j] == 1 and j in list1:
                c25_1_count += 1
            if Matrix2[i][j] == 1 and j in list2:
                c25_2_count += 1
            if Matrix2[i][j] == 1 and j in list3:
                c25_3_count += 1
            if Matrix2[i][j] == 1 and j in list4:
                c25_4_count += 1
            if Matrix2[i][j] == 1 and j in list5:
                c25_5_count += 1
        if c25_1_count >= 3:
            m25 = m25 + 1
        if c25_2_count >= 3:
            m25 = m25 + 1
        if c25_3_count >= 3:
            m25 = m25 + 1
        if c25_4_count >= 3:
            m25 = m25 + 1
        if c25_5_count >= 3:
            m25 = m25 + 1
    m_r25 = m25/(5*mat2_line)
    
    print("m25 = "+str(m25))
    print("m_r25 = "+str(m_r25))    

    m26= 0
    list1 = [0,6,12]
    list2 = [1,7,13]
    list3 = [2,8,14]
    list4 = [3,9,15]
    list5 = [4,10]
    list6 = [5,11]    
    for i in range(0,mat2_line):
        c26_1_count = 0
        c26_2_count = 0
        c26_3_count = 0
        c26_4_count = 0
        c26_5_count = 0
        c26_6_count = 0
        for j in range(0,len(Matrix2[0])-1):
            if Matrix2[i][j] == 1 and j in list1:
                c26_1_count += 1
            if Matrix2[i][j] == 1 and j in list2:
                c26_2_count += 1
            if Matrix2[i][j] == 1 and j in list3:
                c26_3_count += 1
            if Matrix2[i][j] == 1 and j in list4:
                c26_4_count += 1
            if Matrix2[i][j] == 1 and j in list5:
                c26_5_count += 1
            if Matrix2[i][j] == 1 and j in list6:
                c26_6_count += 1
        if c26_1_count >= 3:
            m26= m26+ 1
        if c26_2_count >= 3:
            m26= m26+ 1
        if c26_3_count >= 3:
            m26= m26+ 1
        if c26_4_count >= 3:
            m26= m26+ 1
        if c26_5_count >= 3:
            m26= m26+ 1
        if c26_6_count >= 3:
            m26= m26+ 1
    m_r26 = m26/(6*mat2_line)
    
    print("m26= "+str(m26))
    print("m_r26 = "+str(m_r26))      


    m27 = 0
    list1 = [0,7,14]
    list2 = [1,8,15]
    list3 = [2,9]
    list4 = [3,10]
    list5 = [4,11]
    list6 = [5,12]    
    list7 = [6,13]
    for i in range(0,mat2_line):
        c27_1_count = 0
        c27_2_count = 0
        c27_3_count = 0
        c27_4_count = 0
        c27_5_count = 0
        c27_6_count = 0
        c27_7_count = 0
        for j in range(0,len(Matrix2[0])-1):
            if Matrix2[i][j] == 1 and j in list1:
                c27_1_count += 1
            if Matrix2[i][j] == 1 and j in list2:
                c27_2_count += 1
            if Matrix2[i][j] == 1 and j in list3:
                c27_3_count += 1
            if Matrix2[i][j] == 1 and j in list4:
                c27_4_count += 1
            if Matrix2[i][j] == 1 and j in list5:
                c27_5_count += 1
            if Matrix2[i][j] == 1 and j in list6:
                c27_6_count += 1
            if Matrix2[i][j] == 1 and j in list7:
                c27_7_count += 1
        if c27_1_count >= 3:
            m27= m27+ 1
        if c27_2_count >= 3:
            m27= m27+ 1
        if c27_3_count >= 3:
            m27= m27+ 1
        if c27_4_count >= 3:
            m27= m27+ 1
        if c27_5_count >= 3:
            m27= m27+ 1
        if c27_6_count >= 3:
            m27= m27+ 1
        if c27_7_count >= 3:
            m27= m27+ 1
    m_r27 = m27/(7*mat2_line) 
    print("m27 = "+str(m27))
    print("m_r27 = "+str(m_r27))      

    m28 = 0
    list1 = [0,8]
    list2 = [1,9]
    list3 = [2,10]
    list4 = [3,11]
    list5 = [4,12]
    list6 = [5,13]    
    list7 = [6,14]
    list8 = [7,15]    
    for i in range(0,mat2_line):
        c28_1_count = 0
        c28_2_count = 0
        c28_3_count = 0
        c28_4_count = 0
        c28_5_count = 0
        c28_6_count = 0
        c28_7_count = 0
        c28_8_count = 0
        for j in range(0,len(Matrix2[0])-1):
            if Matrix2[i][j] == 1 and j in list1:
                c28_1_count += 1
            if Matrix2[i][j] == 1 and j in list2:
                c28_2_count += 1
            if Matrix2[i][j] == 1 and j in list3:
                c28_3_count += 1
            if Matrix2[i][j] == 1 and j in list4:
                c28_4_count += 1
            if Matrix2[i][j] == 1 and j in list5:
                c28_5_count += 1
            if Matrix2[i][j] == 1 and j in list6:
                c28_6_count += 1
            if Matrix2[i][j] == 1 and j in list7:
                c28_7_count += 1
            if Matrix2[i][j] == 1 and j in list8:
                c28_8_count += 1
        if c28_1_count >= 3:
            m28= m28+ 1
        if c28_2_count >= 3:
            m28= m28+ 1
        if c28_3_count >= 3:
            m28= m28+ 1
        if c28_4_count >= 3:
            m28= m28+ 1
        if c28_5_count >= 3:
            m28= m28+ 1
        if c28_6_count >= 3:
            m28= m28+ 1
        if c28_7_count >= 3:
            m28= m28+ 1
        if c28_8_count >= 3:
            m28= m28+ 1
    m_r28 = m28/(8*mat2_line) 
    print("m28 = "+str(m28))
    print("m_r28 = "+str(m_r28))      
    print()



    
    
    Matrix3,mat3_line,Matrix00,mat00_line = count3(Matrix,mat_line,FileName)
    f3 = open("of-packet-final state.txt", "w")
    for i in range(0,mat3_line):
        f3.write(str(Matrix3[i])+'\n')
    f3.close()
    
    f0 = open("of-packet-intermediate state.txt", "w")
    for i in range(0,mat00_line):
        f0.write(str(Matrix00[i])+'\n')
    f0.close()
    print("mat00_line = "+str(mat00_line))

    m31 = 0
    for i in range(0,mat3_line):
        c31_count = 0
        for j in range(0,len(Matrix3[0])-1):
            if Matrix3[i][j] == 1:
                c31_count += 1
        if c31_count >= 3:
            m31 = m31 + 1
    m_r31 = m31/mat3_line
    
    print("m31 = "+str(m31))
    print("m_r31 = "+str(m_r31))
    print("len(Matrix3[0] = "+str(len(Matrix3[0])))
    
    
    #方案3，2条总线
    
    m32 = 0
    list1 = [0,2,4,6,8,10,12,14]
    list2 = [1,3,5,7,9,11,13,15]
    for i in range(0,mat3_line):
        c32_1_count = 0
        c32_2_count = 0
        for j in range(0,len(Matrix3[0])-1):
            if Matrix3[i][j] == 1 and j in list1:
                c32_1_count += 1
            if Matrix3[i][j] == 1 and j in list2:
                c32_2_count += 1
        if c32_1_count >= 3:
            m32 = m32 + 1
        if c32_2_count >= 3:
            m32 = m32 + 1
    m_r32 = m32/(2*mat3_line)
    
    print("m32 = "+str(m32))
    print("m_r32 = "+str(m_r32))    
    
    #方案2，3条总线
    
    m33 = 0
    
    list1 = [0,3,6,9,12,15]
    list2 = [1,4,7,10,13]
    list3 = [2,5,8,11,14]



    for i in range(0,mat3_line):
        c33_1_count = 0
        c33_2_count = 0
        c33_3_count = 0
        for j in range(0,len(Matrix3[0])-1):
            if Matrix3[i][j] == 1 and j in list1:
                c33_1_count += 1
            if Matrix3[i][j] == 1 and j in list2:
                c33_2_count += 1
            if Matrix3[i][j] == 1 and j in list3:
                c33_3_count += 1    
        if c33_1_count >= 3:
            m33 = m33 + 1
        if c33_2_count >= 3:
            m33 = m33 + 1
        if c33_3_count >= 3:
            m33 = m33 + 1
    m_r33 = m33/(3*mat3_line)
    
    print("m33 = "+str(m33))
    print("m_r33 = "+str(m_r33)) 

    m34 = 0
   
    list1 = [0,4,8,12]
    list2 = [1,5,9,13]
    list3 = [2,6,10,14]
    list4 = [3,7,11,15]

    for i in range(0,mat3_line):
        c34_1_count = 0
        c34_2_count = 0
        c34_3_count = 0
        c34_4_count = 0
        for j in range(0,len(Matrix3[0])-1):
            if Matrix3[i][j] == 1 and j in list1:
                c34_1_count += 1
            if Matrix3[i][j] == 1 and j in list2:
                c34_2_count += 1
            if Matrix3[i][j] == 1 and j in list3:
                c34_3_count += 1
            if Matrix3[i][j] == 1 and j in list4:
                c34_4_count += 1
        if c34_1_count >= 3:
            m34 = m34 + 1
        if c34_2_count >= 3:
            m34 = m34 + 1
        if c34_3_count >= 3:
            m34 = m34 + 1
        if c34_4_count >= 3:
            m34 = m34 + 1
    m_r34 = m34/(4*mat3_line)
    
    print("m34 = "+str(m34))
    print("m_r34 = "+str(m_r34))


    m35 = 0

    list1 = [0,5,10,15]
    list2 = [1,6,11]
    list3 = [2,7,12]
    list4 = [3,8,13]
    list5 = [4,9,14]
    
    for i in range(0,mat3_line):
        c35_1_count = 0
        c35_2_count = 0
        c35_3_count = 0
        c35_4_count = 0
        c35_5_count = 0
        for j in range(0,len(Matrix3[0])-1):
            if Matrix3[i][j] == 1 and j in list1:
                c35_1_count += 1
            if Matrix3[i][j] == 1 and j in list2:
                c35_2_count += 1
            if Matrix3[i][j] == 1 and j in list3:
                c35_3_count += 1
            if Matrix3[i][j] == 1 and j in list4:
                c35_4_count += 1
            if Matrix3[i][j] == 1 and j in list5:
                c35_5_count += 1
        if c35_1_count >= 3:
            m35 = m35 + 1
        if c35_2_count >= 3:
            m35 = m35 + 1
        if c35_3_count >= 3:
            m35 = m35 + 1
        if c35_4_count >= 3:
            m35 = m35 + 1
        if c35_5_count >= 3:
            m35 = m35 + 1
    m_r35 = m35/(5*mat3_line)
    
    print("m35 = "+str(m35))
    print("m_r35 = "+str(m_r35))    

    m36= 0
    list1 = [0,6,12]
    list2 = [1,7,13]
    list3 = [2,8,14]
    list4 = [3,9,15]
    list5 = [4,10]
    list6 = [5,11]    
    for i in range(0,mat3_line):
        c36_1_count = 0
        c36_2_count = 0
        c36_3_count = 0
        c36_4_count = 0
        c36_5_count = 0
        c36_6_count = 0
        for j in range(0,len(Matrix3[0])-1):
            if Matrix3[i][j] == 1 and j in list1:
                c36_1_count += 1
            if Matrix3[i][j] == 1 and j in list2:
                c36_2_count += 1
            if Matrix3[i][j] == 1 and j in list3:
                c36_3_count += 1
            if Matrix3[i][j] == 1 and j in list4:
                c36_4_count += 1
            if Matrix3[i][j] == 1 and j in list5:
                c36_5_count += 1
            if Matrix3[i][j] == 1 and j in list6:
                c36_6_count += 1
        if c36_1_count >= 3:
            m36= m36+ 1
        if c36_2_count >= 3:
            m36= m36+ 1
        if c36_3_count >= 3:
            m36= m36+ 1
        if c36_4_count >= 3:
            m36= m36+ 1
        if c36_5_count >= 3:
            m36= m36+ 1
        if c36_6_count >= 3:
            m36= m36+ 1
    m_r36 = m36/(6*mat3_line)
    
    print("m36= "+str(m36))
    print("m_r36 = "+str(m_r36))      


    m37 = 0
    list1 = [0,7,14]
    list2 = [1,8,15]
    list3 = [2,9]
    list4 = [3,10]
    list5 = [4,11]
    list6 = [5,12]    
    list7 = [6,13]
    for i in range(0,mat3_line):
        c37_1_count = 0
        c37_2_count = 0
        c37_3_count = 0
        c37_4_count = 0
        c37_5_count = 0
        c37_6_count = 0
        c37_7_count = 0
        for j in range(0,len(Matrix3[0])-1):
            if Matrix3[i][j] == 1 and j in list1:
                c37_1_count += 1
            if Matrix3[i][j] == 1 and j in list2:
                c37_2_count += 1
            if Matrix3[i][j] == 1 and j in list3:
                c37_3_count += 1
            if Matrix3[i][j] == 1 and j in list4:
                c37_4_count += 1
            if Matrix3[i][j] == 1 and j in list5:
                c37_5_count += 1
            if Matrix3[i][j] == 1 and j in list6:
                c37_6_count += 1
            if Matrix3[i][j] == 1 and j in list7:
                c37_7_count += 1
        if c37_1_count >= 3:
            m37= m37+ 1
        if c37_2_count >= 3:
            m37= m37+ 1
        if c37_3_count >= 3:
            m37= m37+ 1
        if c37_4_count >= 3:
            m37= m37+ 1
        if c37_5_count >= 3:
            m37= m37+ 1
        if c37_6_count >= 3:
            m37= m37+ 1
        if c37_7_count >= 3:
            m37= m37+ 1
    m_r37 = m37/(7*mat3_line) 
    print("m37 = "+str(m37))
    print("m_r37 = "+str(m_r37))      

    m38 = 0
    list1 = [0,8]
    list2 = [1,9]
    list3 = [2,10]
    list4 = [3,11]
    list5 = [4,12]
    list6 = [5,13]    
    list7 = [6,14]
    list8 = [7,15]    
    for i in range(0,mat3_line):
        c38_1_count = 0
        c38_2_count = 0
        c38_3_count = 0
        c38_4_count = 0
        c38_5_count = 0
        c38_6_count = 0
        c38_7_count = 0
        c38_8_count = 0
        for j in range(0,len(Matrix3[0])-1):
            if Matrix3[i][j] == 1 and j in list1:
                c38_1_count += 1
            if Matrix3[i][j] == 1 and j in list2:
                c38_2_count += 1
            if Matrix3[i][j] == 1 and j in list3:
                c38_3_count += 1
            if Matrix3[i][j] == 1 and j in list4:
                c38_4_count += 1
            if Matrix3[i][j] == 1 and j in list5:
                c38_5_count += 1
            if Matrix3[i][j] == 1 and j in list6:
                c38_6_count += 1
            if Matrix3[i][j] == 1 and j in list7:
                c38_7_count += 1
            if Matrix3[i][j] == 1 and j in list8:
                c38_8_count += 1
        if c38_1_count >= 3:
            m38= m38+ 1
        if c38_2_count >= 3:
            m38= m38+ 1
        if c38_3_count >= 3:
            m38= m38+ 1
        if c38_4_count >= 3:
            m38= m38+ 1
        if c38_5_count >= 3:
            m38= m38+ 1
        if c38_6_count >= 3:
            m38= m38+ 1
        if c38_7_count >= 3:
            m38= m38+ 1
        if c38_8_count >= 3:
            m38= m38+ 1
    m_r38 = m38/(8*mat3_line) 
    print("m38 = "+str(m38))
    print("m_r38 = "+str(m_r38))      
    print()
    

    
    
    
    
    """
    画图
    """
    #字体配置任务，图表中的中文字体SimHei
    #plt.rcParams["font.sans-serif"]=["SimHei"]
    #处理坐标轴轴线的刻度标签是负数
    #plt.rcParams["axes.unicode_minus"]=False

    #x = [1,2,3,4,5]
    #y = [0,100,0,100,0]
    #plt.xlim =(1,5)
    #plt.ylim(20,100)

    #creat bar

    #plt.bar(x,y,align='center',color='r',tick_label=['','1','','2',''],alpha=0.6)

    #set x,y_axis label
    #plt.xlabel("Program")
    #plt.ylabel("rate")
    
    #plt.show()
    
    
if __name__ =="__main__":
    main()