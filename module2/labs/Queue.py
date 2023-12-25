class QueueError(IndexError): # Choose base class for the new exception.
    def __init__(self) -> None:
        super().__init__(self)

    def get_non_existent_element(self):
        print('Tried to get a non-existent element')

    #
    #  Write code here
    #


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, element):
        self.__queue.append(element)

    def get(self):
        if not self.__queue:
            raise QueueError
        return self.__queue.pop(0)

    def get_queue(self):
        return self.__queue


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    print(que.get_queue())
    for i in range(4):
        print(que.get())
except Exception:
    print(Exception)
