# 演算法

import numpy as np
from itertools import combinations

def comb(items): 
    listnum = [] #建立所有的組合
    for j in range( 0, len( items ) + 1 ):
        for i in combinations(items, j):
            listnum.append( i )

    return listnum

x = int(input("輸入目標值:\n"))

while x != 0:
    inputlist = input("輸入集合:\n")
    inputlist = inputlist.strip() #先去除頭尾空白
    inputlist = inputlist.strip('{') #在去除頭尾括號
    inputlist = inputlist.strip('}')
    inputlist = inputlist.split(',')

    inputlist = np.array( inputlist , np.int32)
    subset = comb( inputlist ) # 尋找所有組合
    flag = 0
    temptest = [] # 找最小解
    for i in range(len(subset)):
        if sum(subset[i]) == x:
            #判斷是不是第一次進入
            if flag == 0 :
                temptest = subset[i]
                flag = 1
            else:
                if len( temptest ) > len( subset[i] ) : #有進入過，就要比較哪個比較少
                    temptest = subset[i]           
    
    print('結果:')  
    temptest = list( temptest ) 
    if flag == 1:        
        temptest.sort() # 做個排序
        print( "{ " ,end=' ' )
        for i in range( len(temptest) ):
            if i == len(temptest)-1 :
                print( temptest[i] ,end=' ' ) #最後一項
            else:                
                print( temptest[i] , ", " ,end=' ' )
        print( " }" )
    else:
        print('No Solution!') 

    #重新跑
    x = int(input("輸入目標值:\n"))