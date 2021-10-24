class Queue:
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        if len(self.qlist)==0:
            return True
        else:
            return False

    def enqueue(self,value):
        self.qlist.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        else:
            self.qlist.pop(0)

    def peek(self):
        return self.qlist[0]

    def display(self):
        if self.isEmpty():
            print("queue empty")
            return
        for i in self.qlist:
            print(i)

    def deleteQueue(self):
        self.qlist=[]


queue = Queue()
print(queue.isEmpty())
queue.display()
print(queue.dequeue())
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.display()
print("---------")
queue.dequeue()

queue.display()
print("------")
print(queue.peek())
queue.deleteQueue()
queue.display()