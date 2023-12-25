class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, value):
        self.__stack_list.append(value)

    def pop(self):
        value = self.__stack_list.pop()
        return value

my_stack = Stack()

my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
