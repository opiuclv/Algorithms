# 演算法

import numpy as np
pre_order = input("Enter Something:\n").split() #輸入數字以空格隔開

while ( len(pre_order) != 1 and pre_order[0] != 0 ) :

    try: #假設輸入為整數則轉為整數
        pre_order = np.array(pre_order, np.int32) 
        flag = 0
    except: #假設輸入為字母則用ASCII轉成數值
        for i in range(len(pre_order)):
            pre_order[i] = ord(pre_order[i])
        flag = 1
    
    class Node(): #利用Class建構Node相關屬性
    	def __init__(self,key):
    		self.key = key
    		self.left = None
    		self.right = None
    
    def add_node(val, node): #新增節點，val為欲增加的值
    	if val <= node.key : 
    		if node.left is None:
    			node.left = Node(val) #若左子樹沒有值則新增節點及其屬性
    			return 
    		else:
    			add_node(val, node.left) #若左子樹有值則進入遞迴繼續判斷
    	else:
    		if node.right is None: #同理左子樹
    			node.right = Node(val)
    			return 
    		else:
    			add_node(val, node.right)
    
    root = Node(pre_order[0]) #實體化node類別
    
    for i in range(len(pre_order)-1): #利用迴圈將所有數值新增節點
        add_node(pre_order[i+1], root) 
        
    print("Tree be created!")
    
    def postorder(tree):
        data = []
    
        def recurse(node):
            if not node: #如果沒有結點則結束讀取
                return
            recurse(node.left) #如果有結點則繼續讀取
            recurse(node.right)
            if flag == 0: #如果一開始就是數值則直接印
                print(node.key,"", end='')
            elif flag == 1: #如果一開始是字母則由ASCII轉回Chr印出來
                print(chr(node.key),"", end='')
    
        recurse(tree)
        return data
            
    data = postorder(root)
    
    pre_order = input("\nEnter Something:\n").split() #輸入數字以空格隔開