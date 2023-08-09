class queue(object):
    'a queue class'

    def __init__(self):
        self.q = []
        print('Constructed')
    def enqueue(self,item):
        self.q.append(item)
    def dequeue(self):
        return self.q.pop(0)
    def size(self):
        return len(self.q)
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def sort(self):
        pass
    def reverse(self):
        pass
    def __iter__(self):
        return iter(self.q)
