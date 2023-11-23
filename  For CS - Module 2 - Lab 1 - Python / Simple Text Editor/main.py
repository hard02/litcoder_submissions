class CustomStack:
    def __init__(self):
        self.text = ""
        self.commands = []

    def insert(self, value):
        self.text += value
        self.commands.append(("delete", len(value)))

    def delete(self, value):
        deleted = self.text[-value:]
        self.text = self.text[:-value]
        self.commands.append(("insert", deleted))

    def get(self, value):
        char = self.text[value - 1]
        print(char)

    def undo(self):
        if self.commands:
            operation, value = self.commands.pop()
            if operation == "delete":
                self.text += value
            elif operation == "insert":
                self.text = self.text[:-len(value)]

# Example usage
custom_stack = CustomStack()

commands = input().strip().split(',')

for command in commands:
    op, *rest = command.split()
    if op == '1':
        custom_stack.insert(rest[0])
    elif op == '2':
        custom_stack.delete(int(rest[0]))
    elif op == '3':
        custom_stack.get(int(rest[0]))
    elif op == '4':
        custom_stack.undo()
                                                                                                                            
