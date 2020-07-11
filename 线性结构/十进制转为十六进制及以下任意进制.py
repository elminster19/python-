#十进制转换为十六进制以下任意进制，在 十进制转换为二进制.py基础上进行修改
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


def baseConverter(decnumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decnumber>0 :
        rem = decnumber % base
        remstack.push(rem) #将余数压入栈中
        decnumber = decnumber // base

    newString = ""
    while not remstack.isEmpty() :
        newString = newString + digits[remstack.pop()] #数字在digits中的索引正好等于其对应的数值
    return newString