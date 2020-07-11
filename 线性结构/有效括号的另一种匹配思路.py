'''
题目内容：
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。

有效字符串需满足：
(1)左括号必须用相同类型的右括号闭合。
(2)左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

输入格式:一行字符串
输出格式：True或False，表示该输入是否为合法括号串
输入样例1：([])
输出样例1：True
'''
#使用字典的键值进行匹配检测
class Stack(list):
    def push(self,item):
        self.append(item)
    def peek(self):
        return self[-1]
    def isEmpty(self):
        return self == []
    def size(self):
        return len(self)

st = Stack()
d = {"(": ")", "[": "]", "{": "}"}
s = input()
for a in s:
    if a in d.keys():
        st.push(a)
    elif st.isEmpty() or not a == d[st.pop()]:  # 右括号多出来或不匹配
        print("False")
        break
else:
    if st.isEmpty():
        print("True")  # 正好匹配
    else:
        print("False")  # 左括号多出来
