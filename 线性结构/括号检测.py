# 栈的应用：简单括号匹配

#使用类自定义python ADT stack
class Stack(list):
    def push(self,item):
        self.append(item)
    def isEmpty(self):
        return self == []
    def peek(self):
        return self[-1]
    def size(self):
        return len(self)

#
def parChecker(symbolString):
    s = Stack()  #创建用于存储左括号的空栈
    balanced = True
    index = 0
    while index<len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol =="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False #这里不能直接return False吗
            else:
                s.pop()
        index += 1
    if s.isEmpty() and balanced:
        return True
    else:
        return False
