# 第1次作業-作業-HW1
>
>學號：112111208
><br />
>姓名：黃誌麒
><br />
>作業撰寫時間：大約50min (mins，包含程式撰寫時間)
><br />
>最後撰寫文件日期：2023/10/05
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容
- [x] 個人認為完成作業須具備觀念

## 說明程式與內容

開始寫說明，該說明需說明想法，
並於之後再對上述想法的每一部分將程式進一步進行展現，
若需引用程式區則使用下面方法，
若為.cs檔內程式除了於敘述中需註明檔案名稱外，
還需使用語法` ```語言種類 程式碼 ``` `，其中語言種類若是要用python則使用py，java則使用java，C/C++則使用cpp，
下段程式碼為語言種類選擇csharp使用後結果：

```csharp
public void mt_getResult(){
    ...
}
```

若要於內文中標示部分網頁檔，則使用以下標籤` ```html 程式碼 ``` `，
下段程式碼則為使用後結果：

```html
<%@ Page Language="C#" AutoEventWireup="true" ...>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" ...>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
    </form>
</body>
</html>
```
更多markdown方法可參閱[https://ithelp.ithome.com.tw/articles/10203758](https://ithelp.ithome.com.tw/articles/10203758)

請在撰寫"說明程式與內容"該塊內容，請把原該塊內上述敘述刪除，該塊上述內容只是用來指引該怎麼撰寫內容。

1. 請解釋何謂git中下列指令代表什麼？並舉個例子，同時必須說明該例子的結果。其指令有add、commit、push、fetch、pull、branch、checkout與merge。

Ans:
```
add(加入)
例子:創一個檔名為為ty的檔案，並在終端輸入git add ty
結果:會將ty這個檔案加入至暫存區

commit(提交)
例子:在終端輸入git commit
結果:將暫存區的ty檔案提交至客戶端的倉庫

push(推送)
例子:在終端輸入git push
結果:將提交的數據從客戶端推送到伺服器端中

fetch(獲取)
例子:在終端輸入git fetch
結果:從伺服器端的倉庫分支獲取資料至客戶端倉庫

pull(拉取)
例子:在終端輸入git pull
結果:將伺服器新的倉庫分支與客戶端新的倉庫分支合併(fetch+merge)

branch(分支)
例子:在終端輸入git branch new
結果:建立名為new的分支

checkout(切換)
例子:在終端輸入git checkout new
結果:切換至分支new

merge(合併)
例子:在終端輸入git merge new
結果:將分支new合併至分支節點
```



2. 於專案下的檔案—**hw1.py**，撰寫註解，以說明該程式每列中之背後意義。

    該hw1.py題目如下：

    ```
    統計字母數。假設今天輸入一句子，句子中有許多單字，單字皆為英文字母小寫，
    請統計句子中字母出現的字數，輸出實需要照字母排序輸出，且若該字母為0則不輸出

    如輸入
    this is an apple
    輸出
    a: 2
    e: 1
    h: 1
    i: 2
    l: 1
    n: 1
    p: 2
    s: 2
    t: 1
    ```

Ans:
```py
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
```



3. 請新增檔案**hw1_2.py，**輸入一個正整數(N)，其中$1\le N \le 100000$，請將該正整數輸出進行反轉

    ```
    如輸入
    1081

    輸出
    1801

    如輸入
    1000

    輸出
    1
    ```

Ans:
```py
num = input()
#輸入一串數字
print(num[::-1])
#將此數字進行反轉並輸出
```


4. **[課外題]**：請找尋資料，說明何謂**單元測試**，請新增檔案**hw1_3.py**，並利用溫度計攝氏轉華氏撰寫單元測試。

Ans:
```
單元測試（Unit Testing）是一種軟體測試方法，用來驗證程式中的最小可測試單位是否正確運作。
```
```py
import unittest

# 攝氏轉華氏的函數
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 單元測試類別
class TestTemperatureConversion(unittest.TestCase):

    # 測試零度轉換
    def test_zero_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
    
    # 測試正值轉換
    def test_positive_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)
    
    # 測試負值轉換
    def test_negative_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)
    
    # 測試小數點值
    def test_decimal_celsius(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(36.6), 97.88, places=2)

# 運行測試
if __name__ == '__main__':
    unittest.main()
```

## 個人認為完成作業須具備觀念

開始寫說明，需要說明本次練習需學會那些觀念 (需寫成文章，需最少50字，並且文內不得有你、我、他三種文字)且必須提供完整與練習相關過程的notion筆記連結
```
本次作業需要學會的東西有:
1.對於git指令要有基本的認識
2.要會寫一些基礎的python程式
3.學著想辦法自己上網去找詢資料
```