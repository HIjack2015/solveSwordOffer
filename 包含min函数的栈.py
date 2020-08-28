class MinStack:
    def __init__(self):
        self.a=[]
        self.m = []

        """
        initialize your data structure here.
        """


    def push(self, x: int) -> None:
        self.a.append(x)
        if not self.m or x<=self.m[-1]:
            self.m.append(x)
        return

    def pop(self) -> None:
        if self.a[-1]==self.m[-1]:
            self.m.pop()
        self.a.pop()
        return

    def top(self) -> int:
        return self.a[-1]

    def min(self) -> int:
        return self.m[-1]



