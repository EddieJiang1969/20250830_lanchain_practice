# Python 基礎：變數與數學運算

## 目錄
1. [變數的概念](#變數的概念)
2. [變數的命名規則](#變數的命名規則)
3. [資料型別](#資料型別)
4. [數學運算](#數學運算)
5. [運算優先順序](#運算優先順序)
6. [練習題](#練習題)

---

## 變數的概念

變數是程式設計中的基本概念，用來儲存資料。在Python中，變數就像是一個容器，可以存放各種類型的資料。

### 基本語法
```python
變數名稱 = 值
```

### 範例
```python
# 建立一個名為 name 的變數，儲存字串 "小明"
name = "小明"

# 建立一個名為 age 的變數，儲存數字 18
age = 18

# 建立一個名為 height 的變數，儲存小數 175.5
height = 175.5
```

---

## 變數的命名規則

### 基本規則
1. **只能包含**：字母、數字、底線 `_`
2. **不能以數字開頭**
3. **區分大小寫**：`name` 和 `Name` 是不同的變數
4. **不能使用Python關鍵字**：如 `if`、`for`、`while` 等

### 好的命名範例
```python
student_name = "小明"      # 使用底線分隔單字
age = 18                  # 簡潔明瞭
total_score = 95.5        # 描述性名稱
```

### 不好的命名範例
```python
2name = "小明"            # 以數字開頭
student-name = "小明"     # 使用連字號
if = 18                  # 使用關鍵字
```

---

## 資料型別

Python中的基本資料型別包括：

### 1. 整數 (int)
```python
age = 18
year = 2024
temperature = -5
```

### 2. 浮點數 (float)
```python
height = 175.5
pi = 3.14159
price = 99.99
```

### 3. 字串 (str)
```python
name = "小明"
message = '你好，世界！'
address = """台北市
信義區
101大樓"""
```

### 4. 布林值 (bool)
```python
is_student = True
is_working = False
```

### 檢查資料型別
```python
age = 18
print(type(age))        # 輸出：<class 'int'>

name = "小明"
print(type(name))       # 輸出：<class 'str'>
```

---

## 數學運算

### 基本運算符

| 運算符 | 說明 | 範例 | 結果 |
|--------|------|------|------|
| `+` | 加法 | `5 + 3` | `8` |
| `-` | 減法 | `10 - 4` | `6` |
| `*` | 乘法 | `6 * 7` | `42` |
| `/` | 除法 | `15 / 3` | `5.0` |
| `//` | 整數除法 | `17 // 3` | `5` |
| `%` | 取餘數 | `17 % 3` | `2` |
| `**` | 次方 | `2 ** 3` | `8` |

### 範例程式碼
```python
# 基本運算
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"加法：{a} + {b} = {a + b}")
print(f"減法：{a} - {b} = {a - b}")
print(f"乘法：{a} * {b} = {a * b}")
print(f"除法：{a} / {b} = {a / b}")
print(f"整數除法：{a} // {b} = {a // b}")
print(f"餘數：{a} % {b} = {a % b}")
print(f"次方：{a} ** {b} = {a ** b}")
```

### 複合運算符
```python
x = 10

# 等同於 x = x + 5
x += 5
print(f"x += 5 後，x = {x}")  # 輸出：15

# 等同於 x = x * 2
x *= 2
print(f"x *= 2 後，x = {x}")  # 輸出：30

# 等同於 x = x - 3
x -= 3
print(f"x -= 3 後，x = {x}")  # 輸出：27
```

---

## 運算優先順序

數學運算遵循特定的優先順序規則：

### 優先順序（由高到低）
1. **括號** `()`
2. **次方** `**`
3. **乘法、除法、取餘數** `*` `/` `//` `%`
4. **加法、減法** `+` `-`

### 範例
```python
# 沒有括號的情況
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")  # 輸出：14 (先算 3*4=12，再加2)

# 使用括號改變優先順序
result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")  # 輸出：20 (先算 2+3=5，再乘4)

# 複雜運算
result3 = 2 ** 3 + 4 * 2 - 1
print(f"2 ** 3 + 4 * 2 - 1 = {result3}")  # 輸出：15
# 計算順序：2**3=8, 4*2=8, 8+8-1=15
```

---

## 練習題

### 練習1：基本變數操作
```python
# 請完成以下程式碼
name = "你的名字"
age = 你的年齡
height = 你的身高（公尺）

print(f"我叫{name}，今年{age}歲，身高{height}公尺")
```

### 練習2：數學運算
```python
# 計算圓的面積
radius = 5
pi = 3.14159
area = pi * radius ** 2

print(f"半徑為{radius}的圓，面積為{area}")
```

### 練習3：溫度轉換
```python
# 將攝氏溫度轉換為華氏溫度
celsius = 25
fahrenheit = celsius * 9/5 + 32

print(f"攝氏{celsius}度 = 華氏{fahrenheit}度")
```

### 練習4：購物計算
```python
# 計算購物總價
apple_price = 25
apple_count = 3
banana_price = 15
banana_count = 2

total = apple_price * apple_count + banana_price * banana_count
print(f"蘋果{apple_count}個：{apple_price * apple_count}元")
print(f"香蕉{banana_count}個：{banana_price * banana_count}元")
print(f"總計：{total}元")
```

---

## 總結

在本講義中，我們學習了：

1. **變數的概念**：變數是用來儲存資料的容器
2. **命名規則**：遵循Python的變數命名規範
3. **資料型別**：整數、浮點數、字串、布林值
4. **數學運算**：基本運算符和複合運算符
5. **運算優先順序**：括號 > 次方 > 乘除 > 加減

這些是Python程式設計的基礎知識，掌握好這些概念，將為後續學習打下堅實的基礎。

---

## 延伸閱讀

- Python官方文件：https://docs.python.org/
- Python數學模組：`math`、`random`、`statistics`
- 進階數學運算：NumPy、SciPy

---

*最後更新：2024年*
