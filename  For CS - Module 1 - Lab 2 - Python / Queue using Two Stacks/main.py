class CustomQueue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, element):
        self.enqueue_stack.append(element)

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if self.dequeue_stack:
            self.dequeue_stack.pop()

    def print_front(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if self.dequeue_stack:
            print(self.dequeue_stack[-1])

# Example usage
custom_queue = CustomQueue()

queries = input().strip().split(',')

for query in queries:
    query_type, *rest = query.split()
    if query_type == '1':
        custom_queue.enqueue(int(rest[0]))
    elif query_type == '2':
        custom_queue.dequeue()
    elif query_type == '3':
        custom_queue.print_front()
                                                                                                                            
