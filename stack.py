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
    
    def isEmpty(self):
        return self.items.__len__() == 0
    
    def __str__(self):
        return f"{self.items}"
    

def infix_to_postfix(infix):
    opstack = Stack()
    outstack = []
    token_list = infix.split()
    
    #연산자 우선순위 설정
    prec = {
        '(': 0,
        '+': 1,
        '-': 2,
        '*': 3,
        '/': 4,
        '^': 5       
    }
    
    for token in token_list:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while opstack.top() != '(':  # ( 아닐 때까지
                outstack.append(opstack.pop())
            opstack.pop()  # ( 제거
        elif token in '+-/*^':
            while not opstack.isEmpty() and prec[opstack.top()] > prec[token]:
                outstack.append(opstack.pop())
            opstack.push(token)
        else:
            outstack.append(token)

    while not opstack.isEmpty():
        outstack.append(opstack.pop())
    return " ".join(outstack)

print(infix_to_postfix('( a + b ) * c'))
