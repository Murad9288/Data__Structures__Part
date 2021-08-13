# Stack 1st system...
'''
 stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() fucntion to pop
# element from stack in 
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are poped:')
print(stack)
 
# uncommenting print(stack.pop())  
# will cause an IndexError 
# as the stack is now empty

'''
# Stack Example and 2nd Rules:
'''
class My_stack():
    def __init__(self):
        self.data = []
    def my_push(self, x):
        return (self.data.append(x))
    def my_pop(self):
        return (self.data.pop())
    def my_peak(self):
        return (self.data[-1])
    def my_contains(self, x):
        return (self.data.count(x))
    def my_show_all(self):
        return (self.data)

arrStack = My_stack()     
arrStack.my_push(1)
arrStack.my_push(2)
arrStack.my_push(1)
arrStack.my_push(3)
print(arrStack.my_show_all())
arrStack.my_pop()
print(arrStack.my_show_all())
print(arrStack.my_contains(1))
'''
# Stack 3rd Rules:
# Stack main structure = Last in First Out..
'''
class Stack:

    def __init__(self):
        self.Stack = []
        self.size = 0

    def DataAdd(self, new_data):
        self.Stack.append(new_data)
        self.size += 1

    def outElement(self):
        self.size -= 1
        return self.Stack.pop()

    def isEmptySTack(self):
        if self.size == 0:
            return "Stack is Empty!"
        else:
            return "Stack is Full"

    def print_Stack(self):
        return self.Stack


    def firstData(self):
        return self.Stack[0]


    def LastData(self):
        return self.Stack[-1]
     
     # Reversing korar jonno
    def ReversedStack(self):
        return self.Stack[::-1]

if __name__ == "__main__":
    op = Stack()

    # add data
    op.DataAdd('0. English')
    op.DataAdd("1. Bangla")
    op.DataAdd("2. Math")
    op.DataAdd("3. Islam")
    op.DataAdd("4. Hindi")


    print("Before Stack:", op.print_Stack())
    print("Before Stack Size", op.size)
    print()

    # remove Data
    op.outElement()
    op.outElement() # 2 element remove
    print("After Stack", op.print_Stack())
    print("After Stack Size", op.size)

    # Stack Size
    print(op.size)
    # Reversed Stack
    print("Reversed Stack", op.ReversedStack())

    # Stack First Data
    print("This is Stack First Element", op.firstData())
    print("This is Stack Last Element", op.LastData())

'''
# Stuck Example to 4th system...
'''
class BBPI:

    def __init__(self, name, roll, id):
        self.Name = name
        self.Roll = roll
        self.Id = id

    def CMT(self):
        return self.Name, self.Roll, self.Id


    def EMT(self):
        return self.Name, self.Roll, self.Id


    def RAT(self):
        pass


class CPI(BBPI):

    def emt(self):
        return self.Name, self.Roll, self.Id




# Driver Code
if _name_ == '_main_':

    op = BBPI("Murad", 165090, 677312838)
    op1 = BBPI("kamal", 214231, 124535221)

    print(op.CMT())
    print(op1.EMT())


    print("CPI")
    o = CPI("a", 121, 11)
    print(o.emt())
'''
