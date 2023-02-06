class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self
        self.prev = self

    def __str__(self):
        return str(self.key)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next

    def __str__(self):
        return " -> ".join(str(v.key) for v in self)

    def print_list(self):
        v = self.head.next
        print("h -> ", end="")
        while v != self.head:
            print(str(v.key) + " -> ", end="")
            v = v.next
        print("h")

    def splice(self, a, b, x):
        """
        a부터 b까지의 노드를 x이후로 연결하는 함수
        Args:
            a (Node): 옮길 시작 노드
            b (Node): 옮길 끝 노드
            x (Node): 옮기려는 위치(x의 다음)
        """
        if a is None or b is None or x is None:
            return
        # cutting a to b
        a.prev.next = b.next
        b.next.prev = a.prev
        # linking a to b with x
        x.next.prev = b
        b.next = x.next
        x.next = a
        a.prev = x
        print()

    def move_after(self, a, x):
        self.splice(a, a, x)

    def move_before(self, a, x):
        self.splice(a, a, x.prev)

    def insert_before(self, node, key):
        self.move_before(Node(key), node)
        self.size += 1

    def insert_after(self, node, key):
        self.move_after(Node(key), node)
        self.size += 1

    def push_front(self, key):
        self.insert_after(self.head, key)

    def push_back(self, key):
        self.insert_before(self.head, key)

    def delete_node(self, node):
        if node is None or node == self.head:
            return None
        node.next.prev, node.prev.next = node.prev, node.next
        del node
        self.size -= 1

    def pop_front(self):
        if self.is_empty:
            return None
        key = self.head.next.key
        self.delete_node(self.head.next)
        return key

    def pop_back(self):
        if self.is_empty:
            return None
        key = self.head.prev.key
        self.delete_node(self.head.prev)
        return key

    def search(self, key):
        for v in self:
            if v.key == key:
                return v
        return None

    def is_empty(self):
        if len(self):
            return False
        return True

    def first(self):
        if not self.is_empty():
            return None
        return self.head.next

    def last(self):
        if not self.is_empty():
            return None
        return self.head.prev

    # join, split 구현
    def join(self, j_list):
        if j_list.is_empty():
            return None
        j_head = j_list.head.next
        j_tail = j_list.head.prev
        self.splice(j_head, j_tail, self.head.prev)

    def split(self, node):  # search랑 연계해서 노드 찾고 실행
        if node is None or node.key is None:
            return self, None
        new_list = DoublyLinkedList()
        self.splice(node, self.head.prev, new_list.head)
        return self, new_list


L = DoublyLinkedList()
L.push_front(10)
L.push_back(20)
print("L = ", end="")
L.print_list()
D = DoublyLinkedList()
D.push_back(30)
D.push_back(40)
print("D =", end=" ")
D.print_list()
L.join(D)
del D
L.print_list()
setter = L.search(30)
print(setter)
L, D = L.split(setter)
L.print_list()
D.print_list()

# while True:
#     cmd = input().split()
#     if cmd[0] == "pushF":
#         L.push_front(int(cmd[1]))
#         print("+ {0} is pushed at Front".format(cmd[1]))
#     elif cmd[0] == "pushB":
#         L.push_back(int(cmd[1]))
#         print("+ {0} is pushed at Back".format(cmd[1]))
#     elif cmd[0] == "popF":
#         key = L.pop_front()
#         if key is None:
#             print("* list is empty")
#         else:
#             print("- {0} is popped from Front".format(key))
#     elif cmd[0] == "popB":
#         key = L.pop_back()
#         if key is None:
#             print("* list is empty")
#         else:
#             print("- {0} is popped from Back".format(key))
#     elif cmd[0] == "search":
#         v = L.search(int(cmd[1]))
#         if v is None:
#             print("* {0} is not found!".format(cmd[1]))
#         else:
#             print("* {0} is found!".format(cmd[1]))
#     elif cmd[0] == "insertA":
#         # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
#         x = L.search(int(cmd[1]))
#         if x is None:
#             print("* target node of key {0} doesn't exit".format(cmd[1]))
#         else:
#             L.insert_after(x, int(cmd[2]))
#             print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
#     elif cmd[0] == "insertB":
#         # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
#         x = L.search(int(cmd[1]))
#         if x is None:
#             print("* target node of key {0} doesn't exit".format(cmd[1]))
#         else:
#             L.insert_before(x, int(cmd[2]))
#             print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
#     elif cmd[0] == "delete":
#         x = L.search(int(cmd[1]))
#         if x is None:
#             print("- {0} is not found, so nothing happens".format(cmd[1]))
#         else:
#             L.delete_node(x)
#             print("- {0} is deleted".format(cmd[1]))
#     elif cmd[0] == "first":
#         print("* {0} is the value at the front".format(L.first()))
#     elif cmd[0] == "last":
#         print("* {0} is the value at the back".format(L.last()))
#     elif cmd[0] == "print":
#         L.print_list()
#     elif cmd[0] == "exit":
#         break
#     else:
#         print("* not allowed command. enter a proper command!")
