#基于 括号检测.py 修改，扩充了括号的范围，包含{[(三种括号
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
        if symbol in "{[(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else: #需要判断右括号的类型是否和左括号匹配，这里我们定义了match函数
                top = s.pop() #不管是否匹配都执行pop，这样省去下面if判断的else处理
                if not matches(top,symbol):
                    balanced = False

        index += 1
    if s.isEmpty() and balanced:
        return True
    else:
        return False

def matches(open,close):
    opens = "{[("
    closes = "}])"
    return opens.index(open) == closes.index(close)
