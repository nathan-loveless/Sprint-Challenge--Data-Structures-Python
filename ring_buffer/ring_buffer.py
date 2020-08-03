class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.storage = [None for i in range(capacity)]

    def append(self, item):
        if self.capacity  == self.index:
            self.storage[0] = item
            self.index = 1

        else:
            self.storage[self.index] = item
            self.index += 1

    def get(self):
        if self.index > 0:
            return [i for i in self.storage if i]