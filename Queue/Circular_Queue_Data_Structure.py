# Circular Queue

class Circular_Queue:

    def __init__(self, max_SizeQ):
        self.queue = [0] * max_SizeQ

        self.max_size = max_SizeQ
        self.Head = 0
        self.Tail = 0
        self.Size = 0

    def Empty_Data(self):
        return self.Size == 0

    def Full_Data(self):
        return self.Size == self.max_size

    def Enqueue_Data(self,itme):
        if self.Full_Data():
            return "Queue is Full"
        else:

            # Add element to the queue
            self.queue[self.Tail] = itme
            self.Tail = (self.Tail+1) % self.max_size
            self.Size += 1

    def Dequeue_Data(self):
        if self.Empty_Data():
            return "Queue is Empty"
        else:
            # Fethc Data
            data = self.queue[self.Head]
            self.Head = (self.Head+1) % self.max_size
            self.Size -= 1
            return data

if __name__ == "__main__":
    Q_size = 5
    mu = Circular_Queue(Q_size)

    mu.Enqueue_Data("1. MD Murad Hossain")
    mu.Enqueue_Data("2. Md Anis Al Hasan")
    mu.Enqueue_Data("3. MD Hosne Mobarok")
    mu.Enqueue_Data("4. MD Araf")
    mu.Enqueue_Data("5. Md Rana Ali")

    print("Before Queue:")
    for i in mu.queue:
        print(i)

    # Call Dequeue Function
    mu.Dequeue_Data()
    mu.Dequeue_Data()

    print("\nAfter Queue: ")
    while not mu.Empty_Data():
        person = mu.Dequeue_Data()
        print(person)
