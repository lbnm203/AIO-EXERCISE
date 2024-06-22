class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return 'Stack is empty'

    def push(self, value):
        if not self.is_full():
            return self.stack.append(value)
        else:
            return 'Stack is full'

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return 'Stack is empty'


stack1 = MyStack(capacity=5)

stack1.push(1)
stack1.push(2)

print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
