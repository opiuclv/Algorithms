# 演算法

import numpy as np

def CalculateMain(formula, i, parentheses, inparentheses):    # 判斷及切割 parentheses 括號
    arr1 = []                       # 放讀到的數字陣列
    symbol = []                     # 放讀到的符號陣列
    num1 = []                       # 放讀到的數字( 因為是逐個字元抓有可能未完成 ex:10只讀到1 )
    tempNum = 0.0                   # 放回傳回來的括號內的計算結果
    parenthesesEnd = False          # 使括號結尾延遲跳出迴圈
    curParentheses = parentheses    # 放進入時計數器應為多少
    numConti = 0                    # 確定數字是否連續 ex: 1  2 error

    def Calculate(lNum, rNum, symbol):      # 兩數字之計算
        subSum = 0.0    # 計算結果
        if symbol == '+':           # 兩數字相加
            subSum = lNum + rNum
        if symbol == '-':           # 兩數字相減
            subSum = lNum - rNum
        if symbol == '*':           # 兩數字相乘
            subSum = lNum * rNum
        if symbol == '/':           # 兩數字相除
            subSum = lNum / rNum
        return subSum

    while i < len(formula):        # 將讀入的input切割並判斷
        if parentheses < 0:
            return None, len(formula)           # 多一個右括號 直接跳Error
        
        if formula[i] == '(':                   # 抓到左括號 計數器+1 呼叫自己回傳括號內計算結果&括號結束點
            parentheses += 1
            tempNum, i = CalculateMain(formula, i+1, parentheses, True)
            if tempNum == None:
                return None, len(formula)
            arr1.append(tempNum)            # 將括號內計算結果接到陣列後面
        elif formula[i] == ')':                 # 抓到右括號 計數器-1
            if curParentheses >= parentheses:
                parenthesesEnd = True           # 等計算完跳出迴圈結束括號內的計算
            parentheses -= 1
            if inparentheses == True:           # 如果是括號內的計算 此處應有一個數字尚未加到陣列
                if len(num1) > 0:               # 有數字
                    arr1.append(int(''.join(num1)))     # 將數字加到陣列中
                    del (num1[:])                       # 刪除暫存

        elif formula[i] == '+' or formula[i] == '-' or formula[i] == '*' or formula[i] == '/':
            if formula[i] == '+':               # 抓到+號 加入陣列中
                symbol.append('+')
            elif formula[i] == '-':             # 抓到-號 加入陣列中
                symbol.append('-')
            elif formula[i] == '*':             # 抓到*號 加入陣列中
                symbol.append('*')
            elif formula[i] == '/':             # 抓到/號 加入陣列中
                symbol.append('/')

            if len(num1) > 0:                       # 有數字
                arr1.append(int(''.join(num1)))     # 將數字加到陣列中
                del (num1[:])                       # 刪除暫存
        elif formula[i].isdigit():             # 只抓數字 非數字無視(abc ABC :{}[] ... etc.)
            if len(num1) == 0:                      # 剛抓到一個新的數字 紀錄抓到的第一個字元位置
                numConti = i
            else :                                  # 連續抓到兩個數字
                numConti += 1
                if i != numConti:                   # 如果兩個數字位置不連續 return error ex: 1  2 + 3
                    return None, len(formula)
            num1.append( (formula[i]) )             # 有數字 ( 可能不只一個字元

        if i == len(formula)-1 and len(num1) > 0:   # 到算式的結尾了 若有抓到數字將數字放入陣列 並刪除暫存
            arr1.append(int(''.join(num1)))
            del (num1[:])
        
        tempC = formula[i]
        if len(arr1) >= 3 and len(symbol) >= 2:                         # 判斷先乘除後加減
            if symbol[0] == '+' or symbol[0] == '-':                    # 加減在前的狀況
                if symbol[1] == '*' or symbol[1] == '/':                                                           # 乘除在後
                    arr1.insert( 1, Calculate(arr1[1], arr1[2], symbol[1]) )    # 將後兩個數字送去做計算 並刪除陣列中的該元素
                    del (arr1[2:4])
                    del (symbol[1:2])
                else:                        # 不是乘除在後
                    arr1.insert( 0, Calculate(arr1[0], arr1[1], symbol[0]) )    # 將前兩個數字送去做計算 並刪除陣列中的該元素
                    del (arr1[1:3])
                    del (symbol[0:1])
            else:                                                       # 乘除在前的狀況
                arr1.insert( 0, Calculate(arr1[0], arr1[1], symbol[0]) )        # 將前兩個數字送去做計算 並刪除陣列中的該元素
                del (arr1[1:3])
                del (symbol[0:1])
        if parenthesesEnd:                                                      # 括號內以計算完畢 跳出迴圈
            break
        i += 1

    if ( not inparentheses ) and parentheses != 0:              # 算式全部跑完了 計數器不等於零(還有括號) 回傳Error
        return None, len(formula)
    if len(arr1) == 2 and len(symbol) == 1:                     # 只剩兩個數字跟一個符號要做計算的狀況(最後的計算)
        arr1.append( Calculate(arr1[0], arr1[1], symbol[0]) )   # 將前兩個數字送去做計算 並刪除陣列中的該元素
        del (arr1[0:2])
        del (symbol[0:1])

    if len(arr1) != 1 or len(symbol) > 0 :                      # 剩下的數字不是一個(除了結果還有其他數字或沒有)或還有剩下的符號 回傳Error
        return None, i-1                                        # 有可能只剩下一個數字(結果)沒有符號

    return arr1[0], i-1                                         # 一切正常 回傳計算結果

i = 0
sum = 0.0           # 計算結果

formula = input("輸入算式: ")
formula = formula.strip()                           # 去除頭尾空白
while formula != '0':                               # 輸入單數字0結束程式
    sum, i = CalculateMain(formula, 0, 0, False)    # 送去做計算 回傳結果
    if sum == None:                                 # 過程有問題
        print('Error !!!')
    else:                                           # 一切正常
        print('result: ', round(sum, 4))
    formula = input("輸入算式: ")
    formula = formula.strip()                       # 去除頭尾空白