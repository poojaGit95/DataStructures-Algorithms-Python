class Dictionary:

    def __init__(self, size):
        self.max_size = size
        self.dict = [None]*size

    def insert(self, key, value):
        index = self.getIndex(key)
        self.dict[index] = value

    def find(self, key):
        index = self.getIndex(key)
        return self.dict[index]

    def getIndex(self, key):
        num=0
        for char in key:
            num+= ord(char)
        return num

    def update(self, key, value):
        index = self.getIndex(key)
        self.dict[index] = value


d = Dictionary(500)


