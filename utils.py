import heapq


class PriorityQueue:
    """
    Defines a pq.
    """

    class Node:
        """
        A node for the priority queue.
        """

        def __init__(self, priority, obj):
            self.priority = priority
            self.obj = obj

        def __lt__(self, other):
            return self.priority < other.priority

    def __init__(self):
        self.pq = []

    def queue(self, priority, node):
        heapq.heappush(self.pq, PriorityQueue.Node(priority, node))

    def pop(self):
        return heapq.heappop(self.pq).obj

    def is_empty(self):
        return len(self.pq) == 0

