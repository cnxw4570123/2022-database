# __iter__(self) method inserted


class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def printList(self):
        for v in self:
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    def push_front(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def push_back(self, key):
        new_node = Node(key)
        if self.size == 0:
            self.head = new_node
        else:  # node(1) -> node(2) -> node(3) -> node(4)
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return None
        else:
            node = self.head
            key = node.key
            self.head = node.next
            del node
        self.size -= 1
        return key

    def pop_back(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            key = self.head.key
            self.head = None
        else:
            prev, tail = None, self.head
            while tail.next is not None:
                prev = tail
                tail = tail.next
            prev.next = None
            key = tail.key
            del tail
        self.size -= 1
        return key

    def search(self, key):
        for v in self:
            if v.key == key:
                break
            v = v.next
        return v

    def remove(self, x):
        if x is None:
            return False
        for v in self:
            prev = None
            if v == x:
                if prev is None:
                    self.head = v.next
                else:
                    prev.next = v.next
                del v
                self.size -= 1
                return True
            else:
                prev = v
                v = v.next
        return False

    def size(self):
        return self.size

    def __iter__(self):
        v = self.head
        while v:
            yield v
            v = v.next


L = SinglyLinkedList()

while True:
    cmd = input("").split()
    if cmd[0] == "exit":
        print("DONE!")
        break
    elif cmd[0] == "pushFront":
        L.push_front(int(cmd[1]))
        print(f"{int(cmd[1])} is pushed at front.")
    elif cmd[0] == "pushBack":
        L.push_back(int(cmd[1]))
        print(f"{int(cmd[1])} is pushed at back.")
    elif cmd[0] == "popFront":
        x = L.pop_front()
        if x:
            print(f"{x} is popped from front")
        else:
            print("List is empty.")
    elif cmd[0] == "popBack":
        x = L.pop_back()
        if x:
            print(f"{x} is popped from back.")
        else:
            print("List is empty.")

    elif cmd[0] == "search":
        x = L.search(int(cmd[1]))
        if x:  # None이면 false
            print(f"{int(cmd[1])} is found!")
        else:
            print(f"{int(cmd[1])} is not found!")

    elif cmd[0] == "remove":
        x = L.search(int(cmd[1]))
        if L.remove(x):
            print(f"{x} is removed.")
        else:
            print("Key is not removed for some reason")
    elif cmd[0] == "printList":
        L.printList()
    elif cmd[0] == "size":
        print(f"list has {L.size} nodes.")
    else:
        print("Not allowed operation! Enter a legal one!")
