class Stack:
    """
    A stack
    """

    #Attribute Types
    l: list[str]

    def __init__(self, s: str):
        self.l = []

        for c in s:
            self.l.append(c.upper())

    def push(self, c: str):
        self.l.append(c)

    def pop(self) -> str:
        return self.l.pop()

    def empty(self) -> bool:
        return not self.l
