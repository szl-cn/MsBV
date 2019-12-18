# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:15:56 2019

@author: Administrator
"""
from Init import Init
from Matrix_operation import Matrix_operation,count1,count2,count3
import matplotlib.pyplot as plt
import numpy as np

def main():
    '''
    按行解析得到0、1、*矩阵
    '''
    #FileName = '1.txt'
    #list1312 = [,,,]
    #for filo in lsidfs
    #FileName = 'ACL1_10K'
    #FileName = 'ACL2_10K'
    #FileName = 'ACL3_10K'
    #FileName = 'ACL4_10K'
    #FileName = 'ACL5_10K'
                 
    #FileName = 'FW1_10K' 
    #FileName = 'FW2_10K' 
    #FileName = 'FW3_10K' 
    #FileName = 'FW4_10K' 
    #FileName = 'FW5_10K'
                 
    #FileName = 'IPC1_5K' 
    #FileName = 'IPC1_10K'
    #FileName = 'IPC2_5K'
    #FileName = 'IPC2_10K'
    
    #FileName = 'ACL1_100K'#12435
    #FileName = 'ACL2_100K'#12453
    #FileName = 'ACL3_100K'#21435
    #FileName = 'ACL4_100K'#21435
    #FileName = 'ACL5_100K'#21435

    #FileName = 'FW1_100K' #12435
    #FileName = 'FW2_100K' #13254
    #FileName = 'FW3_100K' #12435
    #FileName = 'FW4_100K'#42315
    #FileName = 'FW5_100K'#24135
    
    #FileName = 'IPC1_50K' #21435
    #FileName = 'IPC1_100K'#21435
    #FileName = 'IPC2_50K'#21534
    #FileName = 'IPC2_100K'#21534
    
    #FileName = 'FW1_100K_2' #12435
    #FileName = 'FW2_100K_2' #13254
    #FileName = 'FW3_100K_2' #12435
    #FileName = 'FW4_100K_2'#43215
    #FileName = 'FW5_100K_2'#24135
    
    #FileName = 'IPC1_50K_2' #21435
    #FileName = 'IPC1_100K_2'#21435
    #FileName = 'IPC2_50K_2'#21534
    FileName = 'IPC2_100K_2'#21534
    RuleList, linenum = Init(FileName)
    print("linenum = "+str(linenum))

    '''
    0,1,*三元素矩阵写入文本test.txt
    '''
    fo = open("5-tuple.txt", "w")
    for i in range(0,linenum):
        fo.write(str(RuleList[i])+'\n')
        #fo.write(RuleList[i][1]+RuleList[i][2]+RuleList[i][3]+RuleList[i][4]+RuleList[i][5]+'\n')
    fo.close()
    
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
    f1 = open("5-tuple-initial state.txt", "w")
    for i in range(0,mat_line):
        f1.write(str(Matrix[i])+'\n')
    f1.close()
    #print("mat_line = "=str(mat_line))

   
    '''
    统计数据，画图
    方案1
    '''
    Matrix1,mat1_line = count1(Matrix,mat_line)
 #   print(Matrix1,mat1_line)
    f2 = open("5-tuple-final state.txt", "w")
    for i in range(0,mat1_line):
        f2.write(str(Matrix1[i])+'\n')
    f2.close()
    
    count_1 = 0    
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    rate_1,rate_2,rate_3,rate_4,rate_5 =0,0,0,0,0
    for line in range(0,linenum):
        for i in range(1,6):
            if i==1:
                for ss in range(0,32):
                    if RuleList[line][i][ss]== '*':          
                        count_1 +=1
                        rate_1 = count_1/(32*linenum)
            if i==2:
                for ss in range(0,32):
                    if RuleList[line][i][ss]== '*':          
                        count_2 +=1
                        rate_2 = count_2/(32*linenum)
            if i==3:
                for ss in range(0,16):
                    if RuleList[line][i][ss]== '*':          
                        count_3 +=1
                        rate_3 = count_3/(16*linenum)
            if i==4:
                for ss in range(0,16):
                    if RuleList[line][i][ss]== '*':          
                        count_4 +=1
                        rate_4 = count_4/(16*linenum)
            if i==5:
                for ss in range(0,8):
                    if RuleList[line][i][ss]== '*':          
                        count_5 +=1
                        rate_5 = count_5/(8*linenum)
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
    
    
    #比较五个字段中通配符占比大小比较，从小至大
    
    lt = [str(rate_1), str(rate_2), str(rate_3), str(rate_4), str(rate_5)]
    print(lt)
    lt1 = ["rate_1", "rate_2", "rate_3", "rate_4", "rate_5"]
    n= len(lt)
    for x in range(n-1):
        for y in range(n-1-x):
          if lt[y]>lt[y+1]:
             lt[y],lt[y+1]=lt[y+1],lt[y]
             lt1[y],lt1[y+1]=lt1[y+1],lt1[y]
    print(lt)
    print(lt1)
    print()
    
    
    '''
    故障数 m1，故障率m_r
    '''
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
    print("len(Matrix1[0] = "+str(len(Matrix1[0])))
    print()
    
    '''
    方案1改进型
    '''
    m12 = 0

    list1 = [0,2,4]
    list2 = [1,3,5]
    #list1 = [0,1,2]
    #list2 = [3,4,5]

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
    list1 = [0,3]
    list2 = [1,4]
    list3 = [2,5]
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
    方案2
    '''
    Matrix2,mat2_line,Matrix0,mat0_line = count2(Matrix,mat_line)
    f3 = open("5-tuple-segment-final state.txt", "w")
    for i in range(0,mat2_line):
        f3.write(str(Matrix2[i])+'\n')
    f3.close()
    
    f0 = open("5-tuple-segment-intermediate state.txt", "w")
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
    list1 = [0,1,2]
    list2 = [3,4,5]
    #list1 = [0,2,4]
    #list2 = [1,3,5]
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
    list1 = [0,3]
    list2 = [1,4]
    list3 = [2,5]
    '''    
    list1 = [0,3,6,9,12]
    list2 = [1,4,7,10]
    list3 = [2,5,8,11]
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

    
    
    
    
    Matrix3,mat3_line,Matrix00,mat00_line = count3(Matrix,mat_line,FileName)
    f3 = open("5-tuple-packet-final state.txt", "w")
    for i in range(0,mat3_line):
        f3.write(str(Matrix3[i])+'\n')
    f3.close()
    
    f0 = open("5-tuple-packet-intermediate state.txt", "w")
    for i in range(0,mat00_line):
        f0.write(str(Matrix00[i])+'\n')
    f0.close()
    print("mat00_line = "+str(mat00_line))
    
    
    
    
    
    '''
    方案3
    '''
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
    
    '''
    方案2，2条总线
    '''
    m32 = 0
    #list1 = [0,1,2]
    #list2 = [3,4,5]
    list1 = [0,2,4]
    list2 = [1,3,5]
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
    '''
    #方案2，3条总线
    '''
    m33 = 0
    list1 = [0,3]
    list2 = [1,4]
    list3 = [2,5]
    '''    
    list1 = [0,3,6,9,12]
    list2 = [1,4,7,10]
    list3 = [2,5,8,11]
    '''
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

    """
    画图
    """
    #字体配置任务，图表中的中文字体SimHei
    plt.rcParams["font.sans-serif"]=["SimHei"]
    #处理坐标轴轴线的刻度标签是负数
    plt.rcParams["axes.unicode_minus"]=False

    x = [1,2,3,4,5]
    y = [0,100,0,100,0]
    plt.xlim =(1,5)
    plt.ylim(20,100)

    #creat bar

    plt.bar(x,y,align='center',color='r',tick_label=['','1','','2',''],alpha=0.6)

    #set x,y_axis label
    plt.xlabel("Program")
    plt.ylabel("rate")
    
    plt.show()
    
    
if __name__ =="__main__":
    main()