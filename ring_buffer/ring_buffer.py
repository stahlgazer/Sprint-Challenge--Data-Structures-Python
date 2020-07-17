class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring = []
        self.size = 0
        self.oldest = 0

    def append(self, item):
        if self.size < self.capacity:
            self.ring.append(item)
            self.size += 1
        elif self.size == self.capacity:
            self.ring[self.oldest] = item
            self.oldest += 1
            ## reset to front once it reaches end
            if self.oldest == self.capacity:
                self.oldest = 0
            
    def get(self):
        return self.ring