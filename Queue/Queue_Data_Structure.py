class Queue:
    def __init__(self,size):
        self.items = [0] * size
        self.max_size = size
        self.head, self.tail, self.size = 0,0,0

    def Enqueue(self,item):
        if self.is_full():
            print("Queue is full!")
            return
        print("Inserting", item)
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def Dequeue(self):
        item = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item


    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def is_full(self):
        if self.size == self.max_size:
            return True
        return False

if __name__ == "__main__":
    mu = Queue(3)
    mu.Enqueue("Tahmid")
    mu.Enqueue("Murad")
    mu.Enqueue("Rana")
    mu.Enqueue("Subeen")

    while not mu.is_empty():
        person = mu.Dequeue()
        print(person)

    mu.Enqueue("Subeen")
    mu.Enqueue("Murad")
    print(mu.items)
    print("Head: ",mu.head)
    print("Tail: ",mu.tail)

