class MinStack:

    def __init__(self):
        self.stack = []
        self.track_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.track_min.append(val)
        if len(self.track_min) >= 2:
            if self.track_min[-2] < val:
                self.track_min[-1] = self.track_min[-2]

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.track_min.pop()

    def top(self) -> int:
        # if self.stack:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 1:
            return self.stack[0]
        return self.track_min[-1]
    

if __name__ == "__main__":
    input = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
    stack = None
    outputs = []
    for cmd in input:
        if cmd == "MinStack":
            stack = MinStack()
            outputs.append(None)
        elif cmd == "push":
            # Get the next value in the input list
            continue  # Value will be handled in the next iteration
        elif isinstance(cmd, int):
            stack.push(cmd)
            outputs.append(None)
        elif cmd == "pop":
            stack.pop()
            outputs.append(None)
        elif cmd == "top":
            outputs.append(stack.top())
        elif cmd == "getMin":
            outputs.append(stack.getMin())
    print(outputs)