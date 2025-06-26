class Node:
    def __init__(self, head: int,  tail: int):
        self.head = head
        self.tail = tail



    def set_node(self):
        print("current linked list:")
        print(f"{self.head}, {self.tail}")


    def append(self, next, prev):
        self.next = next
        self.prev = prev
        prev = self.head

        self.head = next

    def print(self):
        current = self.head
        while current:
            print(current, end ="->")
            current = current.next





k1 = Node(5, 8)
k1.append(4,5)
k1.append(1,3)
k1.append(14,32)

k1.print()
