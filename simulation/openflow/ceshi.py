from Init_OpenFlow import Init_OpenFlow
from Matrix_operation2 import Matrix_operation,count1,count2
#import matplotlib.pyplot as plt
#import numpy as np

def main():
    '''
    按行解析得到0、1、*矩阵
    '''
    FileName = '2.txt'
#    FileName = '1.txt'
    #FileName = 'OF1_10K'
    
    RuleList, linenum = Init_OpenFlow(FileName)
    print("linenum = "+str(linenum))
    '''
    0,1,*三元素矩阵写入文本test.txt
    '''
    fo = open("test.txt", "w")
    for i in range(0,linenum):#linenum-1 row
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
    
    f1 = open("test_2.txt", "w")
    for i in range(0,mat_line):
        f1.write(str(Matrix[i])+'\n')
    f1.close()        
 
    '''
    统计数据，画图
    方案1
    '''
    Matrix1,mat1_line = count1(Matrix,mat_line)
 #   print(Matrix1,mat1_line)
    f2 = open("test_3.txt", "w")
    for i in range(0,mat1_line):
        f2.write(str(Matrix1[i])+'\n')
    f2.close()  
    print("mat1_line = "+str(mat1_line))
    '''
    方案2
    '''
    Matrix2,mat2_line = count2(Matrix,mat_line)
    f3 = open("test_4.txt", "w")
    for i in range(0,mat2_line):
        f3.write(str(Matrix2[i])+'\n')
    f3.close()    
    
    
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    count_10 = 0
    count_11 = 0
    count_12 = 0

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
                    if RuleList[line][8][ss]== '*':          
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
    '''

    #比较OpenFlow规则集中12个字段中通配符占比大小比较，从小至大
    '''
    lt = [rate_1, rate_2, rate_3, rate_4, rate_5, rate_6, rate_7, rate_8, rate_9, rate_10, rate_11, rate_12]
    #print(lt)
    lt1 = ["rate_1", "rate_2", "rate_3", "rate_4", "rate_5", "rate_6", "rate_7", "rate_8", "rate_9", "rate_10", "rate_11", "rate_12"]
    n= len(lt)
    for x in range(n-1):
        for y in range(n-1-x):
          if lt[y]>lt[y+1]:
             lt[y],lt[y+1]=lt[y+1],lt[y]
             lt1[y],lt1[y+1]=lt1[y+1],lt1[y]
    #print(lt)
    print(lt1)
    print()
    
    '''
    count_1 = 0    
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    for line in range(0,linenum):#linenum low
        for i in range(1,6):
            if i==1:
                for ss in range(0,16):
                    if RuleList[line][i][ss]== '*':          
                        count_1 +=1
                        rate_1 = count_1/(16*linenum)
            if i==2:
                for ss in range(0,48):
                    if RuleList[line][i][ss]== '*':          
                        count_2 +=1
                        rate_2 = count_2/(48*linenum)
            if i==3:
                for ss in range(0,48):
                    if RuleList[line][i][ss]== '*':          
                        count_3 +=1
                        rate_3 = count_3/(48*linenum)
            if i==4:
                for ss in range(0,16):
                    if RuleList[line][i][ss]== '*':          
                        count_4 +=1
                        rate_4 = count_4/(16*linenum)
            if i==5:
                for ss in range(0,12):
                    if RuleList[line][i][ss]== '*':          
                        count_5 +=1
                        rate_5 = count_5/(12*linenum)
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
    '''
    
if __name__ =="__main__":
    main()