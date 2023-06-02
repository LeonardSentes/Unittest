class MyPriorityQueue():
    def __init__(self, size):
        self.queue = []
        self.size = size

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, item):
        self.queue.append(item)

    def delete(self):
        try:
            max_priority = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_priority]:
                    max_priority = i
            item = self.queue[max_priority]
            del self.queue[max_priority]
            return item
        except IndexError:
            print("Index Error occurred.")
            exit()

if __name__ == '__main__':
    myQueue = MyPriorityQueue(4)
    myQueue.insert(7)
    myQueue.insert(9)
    myQueue.insert(6)
    myQueue.insert(7)
    myQueue.insert(2)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())

        