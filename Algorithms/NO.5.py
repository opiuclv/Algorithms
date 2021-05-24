# 演算法分析機測
# 學號: 10527109 / 10527112 / 10527124
# 姓名: 范文豪   / 周志鴻   / 邱正皓 
# 中原大學資訊工程系 
# 第五題
import numpy as np

#利用Class建構一桶水的大小
class Bucket: # 一個水桶
    def __init__( self, name , capacity ):
        # 存放這個水桶名稱
        self.name = name
        # 水桶容量
        self.capacity = capacity #水桶大小
        self.remain = 0  #水桶目前容量
   
def PourBucket( L_Bucket, S_Bucket, goal ) : #L是大杯的 S是小杯的

    while L_Bucket.remain != goal : #當還沒完成目標水量就要繼續
        #當小杯是空的就裝滿它
        if S_Bucket.remain is 0 :
            S_Bucket.remain = S_Bucket.capacity #裝滿水
            print( "Fill    ", S_Bucket.name )

        if L_Bucket.remain is not goal : #當大杯還沒到目標水量就將小杯的水倒入
            #要判斷大杯的倒入小杯會不會超過
            L_now_remain = L_Bucket.capacity - L_Bucket.remain #大杯目前剩下容量
            #能夠承受小杯的水量就全倒
            if L_now_remain >= S_Bucket.remain :
                L_Bucket.remain = L_Bucket.remain + S_Bucket.remain
                S_Bucket.remain = 0 #小杯清空
            # 會超過喔
            else:
                S_Bucket.remain = ( L_Bucket.remain + S_Bucket.remain ) - L_Bucket.capacity #小杯剩下的水量
                L_Bucket.remain = L_Bucket.capacity #大杯就全滿了
            
            print( "Pour    ", S_Bucket.name, " " , L_Bucket.name )

        #當大杯滿了，且沒達成目標，就要倒空
        if L_Bucket.remain is not goal and L_Bucket.capacity is L_Bucket.remain:
            #清空大杯
            L_Bucket.remain = 0
            print( "Empty   ", L_Bucket.name )
    #整個結束
    print( "Success" )


#將數字讀入
inputnum = input("Enter Number:\n").split() #輸入數字以空格隔開
# 將輸入為整數存入
inputnum = np.array( inputnum, np.int32 ) 

while inputnum[0] != 0 and inputnum[1] != 0 and inputnum[2] != 0 :
    # 開始建立水桶
    A_Bucket =  Bucket( "A" ,inputnum[0] ) #實體化node類別 # 也先建立A水桶
    B_Bucket =  Bucket( "B" ,inputnum[1] )
    goal_level = inputnum[2]
    
    #開始遊戲直到成功
    if A_Bucket.capacity > B_Bucket.capacity : #判斷哪個要做存到目標水桶
        PourBucket( A_Bucket, B_Bucket, goal_level )
    else :
        PourBucket( B_Bucket, A_Bucket, goal_level )
    #整個結束再次將數字讀入
    inputnum = input().split() #輸入數字以空格隔開
    # 將輸入為整數存入
    inputnum = np.array( inputnum, np.int32 ) 
