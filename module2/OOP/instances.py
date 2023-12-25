class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5 # Possible and fully permissible

print(example_object_1.__dict__) # Yes, this is how we can display all object elements, as a dict
print(example_object_2.__dict__)
print(example_object_3.__dict__)

class ExampleClass2:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val):
        self.__second = val


example_object_1 = ExampleClass2()
example_object_2 = ExampleClass2(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass2(4)
example_object_3.__third = 5 # It'll behave like any other ordinary property

print(example_object_1.__dict__) # Yes, this is how we can display all object elements, as a dict
print(example_object_1._ExampleClass2__first) 
print(example_object_2.__dict__)
print(example_object_3.__dict__)
