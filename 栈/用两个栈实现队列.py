from collections import deque


class Stack:
    def __init__(self):
        self.inner = deque()

    def push(self, ele):
        self.inner.append(ele)
        return

    def pop(self):
        return self.inner.pop()

    def is_empty(self):
        return len(self.inner) == 0
class CQueue:
    def appendTail(self, value: int) -> None:
        self.s1.push(value)
        return
    def __init__(self):
        self.s1=Stack()
        self.another_stack=Stack()

    def deleteHead(self) -> int:
        while not self.s1.is_empty():
            ele= self.s1.pop()
            self.another_stack.push(ele)
        if self.another_stack.is_empty():
            return -1
        need_result=self.another_stack.pop()
        while not self.another_stack.is_empty():
            ele = self.another_stack.pop()
            self.s1.push(ele)
        return need_result



