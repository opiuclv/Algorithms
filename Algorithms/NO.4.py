# 演算法

import numpy as np

#將數字讀入
inputnum = input("Enter Number:\n").split() #輸入數字以空格隔開
# 將輸入為整數存入
inputnum = np.array( inputnum, np.int32 ) 

#利用Class建構Node相關屬性
class Treenode: # 一個節點
    def __init__( self, key ):
        # 存放數字的地方
        self.Key = [key] 
        # 指向位置的地方
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.parent = None
   
        
def build_tree( val, node, root ): #新增節點，val為欲增加的值，根的位置
    #先比較這個節點的大小
    #再看看有沒有子區間
    #假如有存在再到子區間，重復第一步
    #--------------#
    #先看看有幾個節點
    #2度節點-------------------------------------#
    if len(node.Key) is 1:
        # 比最小的還小
        if val <= node.Key[0]:
            if node.child1 is None: #假如下面沒有
                # 就要加在這裡           
                node.Key.append(val) #數字存入最後
                node.Key.sort()      #數字做排序
                return root
                # 這個數字存完，換下一筆數字
            else :
                return build_tree( val, node.child1, root ) # 就繼續往下找
        # 比最大的還大
        else :
            if node.child2 is None: #假如下面沒有
                # 就要加在這裡
                node.Key.append(val) #數字存入最後
                return root
                # 這個數字存完，換下一筆數字
            else :
                return build_tree( val, node.child2, root ) # 就繼續往下找
    #3度節點-------------------------------------#
    elif len(node.Key) is 2:
        # 比最小的還小
        if val <= node.Key[0]:
            if node.child1 is None: #假如下面沒有
                # 就要加在這裡
                node.Key.append(val) #數字存入最後
                node.Key.sort()      #數字做排序
                return root
                # 這個數字存完，換下一筆數字
            else :
                return build_tree( val, node.child1, root ) # 就繼續往下找
        # 介在中間
        elif node.Key[0] < val and val <= node.Key[1]: 
            if node.child2 is None: #假如下面沒有
                # 就要加在這裡
               node.Key.append(val) #數字存入最後
               node.Key.sort()      #數字做排序
               return root
                # 這個數字存完，換下一筆數字
            else :
                return build_tree( val, node.child2, root ) # 就繼續往下找
        # 比最大的還大
        else:
            if node.child3 is None: #假如下面沒有
                # 就要加在這裡
                node.Key.append(val) #數字存入最後
                return root
                # 這個數字存完，換下一筆數字
            else :
                return build_tree( val, node.child3, root ) # 就繼續往下找
    #4度節點-------------------------------------#
    else:
        #要先做分裂
        return Split_tree( val, node, root )
        


def Split_tree( val, node, root ): #要處理分裂的問題
    father_node = node.parent #指向父節點
    #假如到了根
    if father_node is root and len(father_node.Key) is 3 :
        #就將中間節點拉上去
        #    (M)    father
        #    /  \
        #  (S)  (B) node
        Snode = Treenode( node.Key[0] ) #左邊也建立新的
        Snode.child1 = node.child1
        Snode.child2 = node.child2
        Bnode = Treenode( node.Key[2] ) #右邊也建立新的
        Bnode.child1 = node.child3
        Bnode.child2 = node.child4
        Mnode = Treenode( node.Key[1] ) #將中間變成根
        Mnode.child1 = Snode
        Mnode.child2 = Bnode
        # 子節點指向父節點
        Snode.parent = Mnode
        Bnode.parent = Mnode
        #根指向 M
        root = Mnode
        # 父節點指向根
        Mnode.parent = root
        # 再將數字加入
        return build_tree( val , root, root )
        # 這個數字存完，換下一筆數字
    # 假如父節點是2度節點
    elif len( father_node.Key ) is 1:
        if node.Key[1] <= father_node.Key[0] :# 假如在左邊
           #   ( M  P )   father
           #   /   |   \
           # (S)  (B)     node

           Snode = Treenode( node.Key[0] ) #左邊也建立新的
           Snode.child1 = node.child1
           Snode.child2 = node.child2
           Bnode = Treenode( node.Key[2] ) #右邊也建立新的
           Bnode.child1 = node.child3
           Bnode.child2 = node.child4
           father_node.Key.append(node.Key[1]) # 插入數字
           father_node.Key.sort() # 排序
           # 父節點指向子節點           
           father_node.child3 = father_node.child2 #中間要讓出來           
           father_node.child2 = Bnode           
           father_node.child1 = Snode 
           # 子節點指向父節點
           Snode.parent = father_node
           Bnode.parent = father_node
           # 再將數字加入
           return build_tree( val , root, root )
        else:
           #   ( P  M )    father
           #   /   |   \
           #      (S)  (B) node

           Snode = Treenode( node.Key[0] ) #左邊也建立新的
           Snode.child1 = node.child1
           Snode.child2 = node.child2
           Bnode = Treenode( node.Key[2] ) #右邊也建立新的
           Bnode.child1 = node.child3
           Bnode.child2 = node.child4
           father_node.Key.append(node.Key[1]) # 插入數字
           father_node.Key.sort() # 排序 
           # 父節點指向子節點           
           father_node.child3 = Bnode          
           father_node.child2 = Snode
           # 子節點指向父節點
           Snode.parent = father_node
           Bnode.parent = father_node
           # 再將數字加入
           return build_tree( val , root, root )
       
          # 可以跳出
    # 假如父節點是3度節點
    else:
        if node.Key[1] <= father_node.Key[0] :# 假如在左邊
           #   ( M  P  Q )   father
           #   /   |  \  \
           # (S)  (B)       node

           Snode = Treenode( node.Key[0] ) #左邊也建立新的
           Snode.child1 = node.child1
           Snode.child2 = node.child2
           Bnode = Treenode( node.Key[2] ) #右邊也建立新的
           Bnode.child1 = node.child3
           Bnode.child2 = node.child4
           father_node.Key.append(node.Key[1]) # 插入數字
           father_node.Key.sort() # 排序
           # 父節點指向子節點 
           father_node.child4 = father_node.child3          
           father_node.child3 = father_node.child2          
           father_node.child2 = Bnode           
           father_node.child1 = Snode 
           # 子節點指向父節點
           Snode.parent = father_node
           Bnode.parent = father_node
           return build_tree( val , root, root )
           # 這個數字存完，換下一筆數字
        elif father_node.Key[0] < node.Key[1] and node.Key[1] <= father_node.Key[1] :
           #   ( P  M   Q  )   father
           #    /  |   \  \
           #      (S) (B)      node 
           Snode = Treenode( node.Key[0] ) #左邊也建立新的
           Snode.child1 = node.child1
           Snode.child2 = node.child2
           Bnode = Treenode( node.Key[2] ) #右邊也建立新的
           Bnode.child1 = node.child3
           Bnode.child2 = node.child4
           father_node.Key.append(node.Key[1]) # 插入數字
           father_node.Key.sort() # 排序
           # 父節點指向子節點           
           father_node.child4 = father_node.child3          
           father_node.child3 = Bnode       
           father_node.child2 = Snode
           # 子節點指向父節點
           Snode.parent = father_node
           Bnode.parent = father_node
           return build_tree( val , root, root )
           # 這個數字存完，換下一筆數字
        else:
           #   ( P  Q   M  )   father
           #    /  |   \  \
           #           (S) (B) node
           node.Key.append(val) # 先加入
           node.Key.sort() #排序
           Snode = Treenode( node.Key[0] ) #左邊也建立新的
           Snode.child1 = node.child1
           Snode.child2 = node.child2
           Bnode = Treenode( node.Key[2] ) #右邊也建立新的
           Bnode.child1 = node.child3
           Bnode.child2 = node.child4
           father_node.Key.append(node.Key[1]) # 插入數字
           father_node.Key.sort() # 排序
           # 父節點指向子節點           
           father_node.child4 = Bnode
           father_node.child3 = Snode
           # 子節點指向父節點
           Snode.parent = father_node
           Bnode.parent = father_node
           return build_tree( val , root, root )
           # 這個數字存完，換下一筆數字
        

# 開始建立樹
root = Treenode(inputnum[0]) #實體化node類別 # 也先建立頭
root.parent = root #將父節點指向根

for i in range(len(inputnum)-1): #利用迴圈將所有數值新增節點
    root = build_tree(inputnum[i+1], root, root) 


def postorder(tree): 
    print( "2-3-4 Tree (Postorder):" )
    def post_recurse(node):
        if not node: #如果沒有結點則結束讀取
            return
        post_recurse(node.child1) #如果有結點則繼續讀取
        post_recurse(node.child2)
        post_recurse(node.child3)
        post_recurse(node.child4)
        if len( node.Key ) is 1 :
            print( "(", node.Key[0] , ")" ,end=' ')
        elif len( node.Key ) is 2 :
            print( "(", node.Key[0], "," , node.Key[1] , ")" ,end=' ')
        else:
            print( "(", node.Key[0], "," , node.Key[1], "," , node.Key[2], ")" ,end=' ' )

    post_recurse(tree)    
    print( "\n" )



def preorder(tree):
    print( "2-3-4 Tree (Preorder):" )
    def pre_recurse(node):
        if not node: #如果沒有結點則結束讀取
            return        

        if len( node.Key ) is 1 :
            print( "(", node.Key[0] , ")" ,end=' ')
        elif len( node.Key ) is 2 :
            print( "(", node.Key[0], "," , node.Key[1] , ")" ,end=' ' )
        else:
            print( "(", node.Key[0], "," , node.Key[1], "," , node.Key[2], ")" ,end=' ' )

        pre_recurse(node.child1) #如果有結點則繼續讀取
        pre_recurse(node.child2)
        pre_recurse(node.child3)
        pre_recurse(node.child4)
         
    pre_recurse(tree)    
    print( "\n" )


# 印出樹
print( "output:" )
preorder(root)
postorder(root)
