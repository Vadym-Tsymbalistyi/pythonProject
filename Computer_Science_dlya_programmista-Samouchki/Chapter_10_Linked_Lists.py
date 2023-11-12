# 1. Создайте связный список, содержащий числа от 1 до 100. Затем выведите
# каждый узел списка.

# 2. Создайте два связных списка: один содержащий цикл, а другой — без цикла.
# Убедитесь, что в каждом из них есть метод detect_cycle для определения
# того, имеется ли в списке цикл. Вызовите detect_cycle для обоих списков.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __init__(self, node):
        self.head = node

    # head = None
    # head = Node(data = 1, next = None)
    # head = Node(data = 1, next = Node(2))

    # LinkedList {
    #            head = Node(data = 1, next = Node(2))
    #            tail = Node(data = 1, next = Node(2))
    #
    #
    #            Node(1, next = Node(2)) -> Node(2, next = Node(3)) -> Node(3, next = None) -> None
    # currentNode ^
    # }

    def append(self, data):
        current_node = Node(data)
        if self.head is None:
            self.head = current_node
            self.tail = current_node
        else:
            self.tail.next = current_node
            self.tail = current_node

    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def create_cycle(self, node_id_from, node_id_to):
        # TODO: implement
        from_node = self.find_node_by_id(node_id_from)
        to_node = self.find_node_by_id(node_id_to)

        if from_node is not None and to_node is not None:
            from_node.next = to_node
        else:
            print("Warning: Cycle not created.")
        return

    # There is no Cycle: Node(1, next = Node(2)) -> Node(2, next = Node(3)) -> Node(3, next = None) -> None
    # There is a Cycle Ring: Node(1, next = Node(2)) -> Node(2, next = Node(3)) -> Node(3, next = None) -> Node(1, next = Node(2))
    # There is a Cycle Loop: Node(1, next = Node(2)) -> Node(2, next = Node(3)) -> Node(3, next = Node(2, next = Node(3)))
    def detect_cycle(self):  # should return  True or False
        return self.detect_cycle_ring() or self.detect_cycle_loop()  # pseudo code

    # O(N/2)
    def detect_cycle_ring(self):  # should return  True or False (Boolean)
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    # O(1)
    def detect_cycle_ring_O1(self):
        return self.head == self.tail

    # O(N*logN)
    # TODO: optimize O(logN) - > O(1)
    def detect_cycle_loop(self):  # should return  True or False
        visited_nodes = set()
        currentNode = self.head
        while currentNode.next is not None:
            if currentNode in visited_nodes:
                return True
            visited_nodes.add(currentNode)
            currentNode = currentNode.next
        return False


linked_list = LinkedList()
for i in range(1, 101):
    linked_list.append(i)
linked_list.print()

linked_list.create_cycle(3, 2)  # ... -> Node(3, next = Node(2, next = Node(3)))
