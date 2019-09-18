#  字符串

### 字符串相关概念

- **字典序**：字符序采用字母表中的顺序abcd...；崇左往右比较下标相同的各队字符，遇到的第一对不同字符的字符序决定了这两个字符串的顺序；如果下标的各队字符都相同，其中一个串较短，那么认为它较小。

### 字符串抽象数据类型

下面是一个简单的字符串ADT，其中定义了一些字符串操作：

```python
ADT String:
    String(self, sseq) # 基于字符序列sseq建立一个字符串
    is_empty(self) # 判断本字符串是否空串
    len(self) # 取得字符串的长度
    char(self, index) # 取得字符串中位置index的字符
    substr(self, a, b) # 取得字符串中[a:b]的子串
    match(self, string) # 查找串string在本字符串中第一个出现的位置
    concat(self, string) # 做出本字符串与另一个字符串string的拼接串
    subst(self, str1, str2) # 做出将本字符串里的子串str1都替换为str2的结果串
```

### 字符串的实现

- **字符串的存储**：1. 把字符串的全部内容存储在一块连续存储区内；2. 把串中每个字符串单独存入一个独立存储块，并将这些块链接起来。 这两种方式都很极端。实际中，采用的方式是：把一个串的字符序列分段保存在一块存储块里，并链接起这些块。
- **串的表示**：1. 用一个专门的数据域记录字符长度，就像连续表中的num域； 2. 用一个特殊编码表示串结束（c语言采用这种方式）

python的字符串实现，采用了一体式顺序表形式。在 一个str对象的头部，除了记录字符串长度外，还记录一些解释器用于管理对象的信息。



### 字符串匹配问题（自串查找）

**朴素的串匹配算法**

1. 从左到右逐个字符匹配；
2. 发现不匹配时，赚取考虑目标串里的下一个欸子是否域模式串匹配

朴素串匹配算法的一个实现：

```python
def naive_matching(t, p):
	# t是目标串，p是模式串
	m, n = len(p), len(t)
	i, j = 0, 0
	while i < m and j < n:
		if p[i] == t[j]: # 字符相同，考虑下一对字符
			i, j = i+1, j+1
		else:
			i, j = 0, j-i+1 # 字符不同，考虑t中下一位置
	if i == m:
		return j - i # 找到匹配，返回其开始的下标
	return -1 # 无匹配，返回特殊值
```

算法效率低下，主要原因是出现回溯：遇到一对字符不同时，模式串右移一个字符位置，匹配回到模式串的开始，也回到目标串中前面的下一个位置。

出现最坏情况的实例：

目标串：00000000000000001

模式串：0001



**无回溯串匹配算法（KMP算法）**

**KMP算法的基本考虑：**

匹配过程中不回溯，利用之前匹配的记录信息去跳转下一次匹配的开始位置，即把模式串前移若干位置。

**KMP算法：**

假设已经根据模式串做出了pnext表，考虑KMP算法的实现。

```python
def matching_KMP(t, p, pnext):
    """
    KMP串匹配，主函数
    """
    while j < n and i < m: # i == m说明找到了匹配
        if i == -1 or t[j] == p[i]: # 比较下一对字符
            j, i = j+1, i+1
        else:
            i = pnext[i] # 从pnext取得p的下一字符位置
    if i == m:
        return j - i # 找到匹配，返回其下标
    return -1 # 无匹配，返回特殊值
    
```

pnext表构造算法

```python
def gen_pnext(p):
    """
    生成针对p中各位置i的下一检查位置表，用于KMP算法
    """
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m # 初始数组元素全为 -1
    while i < m-1: # 生成下一个pnext元素值
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            pnext[i] = k # 设置pnext元素
        else:
            k = pnext[k] # 退到更短相同前缀
    return pnext
```

### 正则表达式

python语言的正则表达式功能由标准包re提供。

**主要操作：**

- 生成正则表达式对象：re.complie(pattern, flag=0)
- 检索：re.search(pattern, string, flag=0)
- 匹配：re.match(pattern, string, flag=0)
- 分割：re.split(pattern, string, flag=0)
- 找出所有匹配串：re.findall(pattern, string, flags=0)



## 字符串应用

### 应用一、反转字符串

![](https://raw.githubusercontent.com/wemozj/image/master/20190909164038.png)

#### 应用二、整数反转

![](https://raw.githubusercontent.com/wemozj/image/master/20190909165706.png)

#### 应用三、字符串中的第一个唯一字符

![](https://raw.githubusercontent.com/wemozj/image/master/20190909171715.png)

#### 应用四、有效的字母异位词

![](https://raw.githubusercontent.com/wemozj/image/master/20190909203642.png)

#### 应用五、验证回文字符串

![1568037797269](C:\Users\wemo\AppData\Roaming\Typora\typora-user-images\1568037797269.png)

#### 应用六、

![](https://raw.githubusercontent.com/wemozj/image/master/20190910222044.png)

![](https://raw.githubusercontent.com/wemozj/image/master/20190910221836.png)



### 应用七、实现strStr()

![](https://raw.githubusercontent.com/wemozj/image/master/20190918094821.png)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        length_comp = len(needle)
        length_sour = len(haystack)
        for i in range(length_sour):
            if (i + length_comp) > length_sour:
                return -1
            part = haystack[i:i+length_comp]
            if part == needle:
                return i
        return -1
```



### 应用八、最长公共前缀

![](https://raw.githubusercontent.com/wemozj/image/master/20190918110101.png)



```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        ss = list(map(set, zip(*strs)))
        res = ''
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res += x[0]
            
        return res
# 对于示例，['flower', 'flow', 'flight']， ss输出： [{'f'}, {'l'}, {'o', 'i'}, {'w', 'g'}]
# list(map(list, zip(*strs))) : [['f', 'f', 'f'], ['l', 'l', 'l'], ['o', 'o', 'i'], ['w', 'w', 'g']]
# 真是好方法
```

下面再贴一个针对python的奇技淫巧：

![1568775892855](C:\Users\wemo\AppData\Roaming\Typora\typora-user-images\1568775892855.png)



