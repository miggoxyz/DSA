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

# stack implemenetation using a Linked List
# Next points to stack frame below
# The key difference between arr and LL implementation is that
# the stack is dynamically sized, avoiding the stack overflow issue.


class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty.")
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self, data):
        frame = self.Node(data)
        frame.next = self.top
        self.top = frame

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.top.data

    def isEmpty(self):
        return self.top == None

    def __iter__(self):
        current = self.top
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return "[" + " -> ".join(str(item) for item in self) + "]"


if __name__ == "__main__":
    stack = Stack()

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

    print(f"popped an element: {stack.pop()}")
    print(stack)
    print(f"peeked: {stack.peek()}")
    print(stack)
