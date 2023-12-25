class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, value):
        self.__stk.append(value)

    def pop(self):
        val = self.__stk.pop()
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_counter(self):
        return self.__sum

    def pop(self):
        value = Stack.pop(self)
        self.__sum -= value

    def push(self, value):
        Stack.push(self, value)
        self.__sum += value

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
