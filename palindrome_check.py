class Deque:
    def __init__(self, s):
        self.items = []
        for word in s:
            self.items.append(word)

    def __str__(self):
        return f"{self.items}"

    def append(self, c):
        self.items.append(c)

    def appendleft(self, c):
        self.items.insert(0, c)

    def __len__(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()

    def popleft(self):
        return self.items.pop(0)

    def right(self):
        return self.items[-1]

    def left(self):
        return self.items[0]


def check_palindrome(s):
    dq = Deque(s)
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
            break
    return palindrome


s = input()
print(check_palindrome(s))
