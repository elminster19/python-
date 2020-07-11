#十进制转换为二进制，短除之后的结果是由低到高的二进制位，二进制时需要反转顺序，使用栈来实现
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


def devidedBy2(decnumber):
    remstack = Stack()
    while decnumber>0 :
        rem = decnumber % 2
        remstack.push(rem) #将余数压入栈中
        decnumber = decnumber // 2

    binString = ""
    while not remstack.isEmpty() :
        binString = binString + str(remstack.pop()) #栈里存储的是数值型。输出需要转为字符串类型
    return binString