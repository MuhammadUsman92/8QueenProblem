import random


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            minCount = 0
            for i in range(len(self.queue)):
                if self.queue[i]["fitness"] < self.queue[minCount]["fitness"]:
                    minCount = i
            item = self.queue[minCount]
            del self.queue[minCount]
            return item
        except IndexError:
            print()
            exit()


def generateSolutions():
    myQueue = PriorityQueue()
    for i in range(0, 8):
        lis = []
        for j in range(0, 8):
            lis.append(random.randint(0, 7))
        myQueue.insert({"solution": lis, "fitness": calculateFitnessScore(lis)})
    bestTwo = [myQueue.delete()['solution'], myQueue.delete()['solution']]
    return bestTwo


def calculateFitnessScore(lis):
    count = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if i != j:
                if lis[i] == lis[j]:
                    count += 1
                if i - lis[i] == j - lis[j]:
                    count += 1
                if i + lis[i] == j + lis[j]:
                    count += 1
    if count == 0:
        print("Achieve")
        print(lis)
        exit()
    return count


def crossover(lists):
    myQueue = PriorityQueue()
    a = lists[0]
    b = lists[1]
    myQueue.insert({"solution": a, "fitness": calculateFitnessScore(a)})
    myQueue.insert({"solution": b, "fitness": calculateFitnessScore(b)})
    index = random.randint(1, 7)
    newlista = a[:index] + b[index:]
    myQueue.insert({"solution": newlista, "fitness": calculateFitnessScore(newlista)})
    newlistb = a[index:] + b[:index]
    myQueue.insert({"solution": newlistb, "fitness": calculateFitnessScore(newlistb)})
    bestTwo = [myQueue.delete()['solution'], myQueue.delete()['solution']]
    return bestTwo


def mutation(lists):
    myQueue = PriorityQueue()
    a = lists[0]
    b = lists[1]
    newlista = a
    newlista[random.randint(0, 7)] = random.randint(0, 7)
    myQueue.insert({"solution": newlista, "fitness": calculateFitnessScore(newlista)})
    newlistb = b
    newlistb[random.randint(0, 7)] = random.randint(0, 7)
    myQueue.insert({"solution": newlistb, "fitness": calculateFitnessScore(newlistb)})
    bestTwo = [myQueue.delete()['solution'], myQueue.delete()['solution']]
    return bestTwo


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        mutation(crossover(generateSolutions()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
