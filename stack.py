import tkinter as tk


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
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3       
    }
    
    for token in token_list:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while opstack.top() != '(':  # ( 아닐 때까지
                outstack.append(opstack.pop())
            opstack.pop()  # ( 제거
        elif token in '+-/*^':
            while not opstack.isEmpty() and prec[opstack.top()] >= prec[token]:
                outstack.append(opstack.pop())
            opstack.push(token)
        else:
            outstack.append(token)

    while opstack:
        outstack.append(opstack.pop())
    return compute_postfix(" ".join(outstack))


def compute_postfix(postfix):
    result = Stack()
    token_list = str(postfix).split()
    
    for token in token_list:
        if token in '+-*/^':
            oprnd1 = float(result.pop())
            oprnd2 = float(result.pop())
            if token == '+':
                result.push(oprnd2 + oprnd1)
            elif token == '-':
                result.push(oprnd2 - oprnd1)
            elif token == '*':
                result.push(oprnd2 * oprnd1)
            elif token == '/':
                result.push(oprnd2 / oprnd1)
            elif token == '^':
                result.push(oprnd2**oprnd1)
        else:
            result.push(float(token))
    
    return result.pop()


def do_something():
    value = compute_postfix(infix_to_postfix(expr.get()))
    total.set("{0:.4f}".format(value))
    return


root = tk.Tk()
root.title("My Calculator")
expr = tk.StringVar()
title_label = tk.Label(root, text="My Calcualtor").grid(row=0, columnspan=2)
input_exam = tk.Label(root, text="Space between terms: ( 3 + 2 ) * 8").grid(row=1, columnspan=2)
exp_entry = tk.Entry(root, textvariable=expr).grid(row=2, column=0)
total_label = tk.Label(root, text="TOTAL").grid(row=3, column=0)
total = tk.StringVar()
total.set('0')
value_label = tk.Label(root, textvariable=total, width=20).grid(row=3, column=1)
equal_btn = tk.Button(root, text=' = ', width=20, command=do_something).grid(row=2, column=1)
root.mainloop()
root.destroy()
