class Queue:
    """
    A queue
    """

    #Attribute Types
    l: list[str]

    def __init__(self):
        self.l = []

    def enqueue(self, c: str):
        self.l.append(c)

    def dequeue(self) -> str:
        return self.l.pop(0)

    def empty(self) -> bool:
        return not self.l

    def __contains__(self, item):
        return item in self.l

    def __len__(self):
        return len(self.l)
