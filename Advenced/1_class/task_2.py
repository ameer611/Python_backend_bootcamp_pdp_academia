class Queue:
    def __init__(self):
        self.new_list = []

    def enque(self, element):
        self.new_list.append(element)

    def deque(self, element):
        self.new_list.remove(element)

    def size(self):
        return len(self.new_list)

