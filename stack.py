class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, x):
        self.items.append(x)
        
    def pop(self):
        try: 
            return self.items.pop()
        except IndexError:
            print('Stack is empty!')
            
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print('Stack is empty!')      
            
    def __len__(self):
        return len(self.items)
    

def parChecker(parSeq):
    S = Stack()
    for p in parSeq:
        if p == '(':
            S.push(p)
        elif p == ')':
            if len(S) == 0:
                return False
            else:
                S.pop()
        else:
            print('Not allowed Symbol')
    if len(S) > 0:
        return False
    else:
        return True


p = input("괄호 입력 > ")
print(parChecker(p))