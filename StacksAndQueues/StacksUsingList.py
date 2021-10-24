class Stacks:
    def __init__(self,maxsize):
        self.stackList = []
        #if limited size then declare size
        self.maxSize = maxsize

    def display(self):
        slist = reversed(self.stackList)
        for i in slist:
            print(i)

    def isEmpty(self):
        if len(self.stackList)==0:
            return True
        else:
            return False

    #if size is taken into consideration
    def isFull(self):
        if self.maxSize == len(self.stackList):
            return True
        else:
            return False


    def push(self,value):
        if self.isFull():
            return "Stack is full"
        else:
            self.stackList.append(value)

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            self.stackList.pop()

    def peek(self):
        print(self.stackList[len(self.stackList)-1])


    def deleteStack(self):
        self.stackList=[]



s = Stacks(5)
print(s.isEmpty())
s.push(7)
s.push(8)
s.push(9)
s.push(10)

s.push(11)
print(s.push(12))
s.display()
s.pop()
s.pop()

print("------")

s.pop()

s.display()
s.deleteStack()
print("----")
s.display()



