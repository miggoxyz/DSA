"""
There are two ways to implement a stack,
1) array as the underlying DS
2) LinkedList
operations:
    Push => aware of stack overflow
    Pop  => aware of stack underflow.
    isEmpty
    peek

"""

# stack implemenetation using an array


class Stack:
    def __init__(self, size):
        """
        we init the stack with a specified size
        we also init the pointer to -1, indicating an empty stack.
        """
        self.stack = [None] * size
        self.top = -1

    def push(self, data):
        # handle overflow
        if self.top == len(self.stack) - 1:
            raise Exception("Stack is full")
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        # handle underflow
        if self.isEmpty():
            raise Exception("Stack is empty")
        # temp var to store content
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return data

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is emptu")
        return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1

    def __repr__(self):
        return f"{self.stack}"


if __name__ == "__main__":
    stack = Stack(5)

    print("Attempting to pop an empty stack")
    try:
        stack.pop()
    except Exception as e:
        print(e)

    print("Attempting to peek an empty stack")
    try:
        stack.peek()
    except Exception as e:
        print(e)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)

    print("Attempting to push onto a full stack")
    try:
        stack.push(6)
    except Exception as e:
        print(e)

    print(f"popped an element: {stack.pop()}")
    print(stack)
    print(f"peeked: {stack.peek()}")
    print(stack)
