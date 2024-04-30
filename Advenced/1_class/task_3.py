class Queue:
    def __init__(self):
        self.new_list = []

    def enque(self, element):
        self.new_list.append(element)

    def deque(self, element):
        self.new_list.remove(element)

    def size(self):
        return len(self.new_list)

queue = Queue()
def test_Queue():
    assert queue.size()==0

    queue.enque("alice")
    queue.enque("john")
    queue.enque("amir")
    queue.enque("xoja")
    assert queue.size()==4

    queue.deque("alice")
    queue.deque("amir")
    queue.deque("xoja")
    assert queue.size()==1

if __name__=='__main__':
    test_Queue()

