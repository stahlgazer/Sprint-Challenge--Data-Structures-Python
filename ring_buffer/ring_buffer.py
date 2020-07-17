class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring = []
        self.size = 0
        self.oldest = 0

    def append(self, item):
        # if not full
        if self.size < self.capacity:
            # add to ring and increase size 1
            self.ring.append(item)
            self.size += 1
        # if full
        elif self.size == self.capacity:
            # replace oldest item
            self.ring[self.oldest] = item
            # increment to update oldest to next oldest
            self.oldest += 1
            # reset to front once it reaches end
            if self.oldest == self.capacity:
                self.oldest = 0
            
    def get(self):
        return self.ring