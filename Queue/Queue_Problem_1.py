
# First in First Out..
# Queue use to Intest problem Example..
queue = []
def Enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print(element,"IS ADDED QUEUE ELEMENT.")
def Dequeue():
    if not queue:
        print("QUEUE IS EMPTY.")
    else:
        e = queue.pop(0)
        print("Removed element: ",e)
def display():
    print(queue)

while True:
    print("Select the operation number:\n1.Data_Add.\n2.Data_Remove.\n3.Data_Show.\n4.Quit.")
    ch = int(input("Please select option number: "))
    if ch == 1:
        Enqueue()
    elif ch == 2:
        Dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("The select option number wrong!.")
