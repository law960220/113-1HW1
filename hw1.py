from typing import List

def countLetters(sentence: str) -> List[int]:
    letterCount: List[int] = [0] * 26
    #26個值分別計數a-z

    for char in sentence:
        if char.isalpha():
        #判斷是否為字母    
            index = ord(char) - ord('a')
            #判斷是哪個字母
            letterCount[index] += 1
            #將此字母計數+1

    return letterCount
pass

def printLetterCount(letterCount: List[int]) -> None:

    for i in range(26):
    #26個字母a-z    
        if letterCount[i] > 0:
        #如果對應字母有出現過    
            print(f"{chr(i + ord('a'))}: {letterCount[i]}")
            #顯示哪個字母出現了幾次
pass

inputSentence: str = "this is an apple"
#將字串this is an apple放入以上程式
letterCount: List[int] = countLetters(inputSentence)
#計算各字母出現次數
printLetterCount(letterCount)
#輸出結果