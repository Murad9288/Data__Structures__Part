# Zulkarnine Videos.

class Node:
    def __init__(self,value):
        self.prev = None
        self.next = None
        self.val = value

class Double_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

# Append value
    def Append(self,val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    # Remove node
    def remove_node(self,node):
        if node.prev is None:
            self.head = node.next

        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev

        else:
            node.next.prev = node.prev
        self.size -= 1

    # Remove Value
    def remove(self,value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.remove_node(node)
                break #break er kaj = eikhane ekoyrokom element er moddhe shudhu prothom element ta k remove korbe...
            node = node.next

#last element remove
    def remove_last(self):
        if self.tail is not None:
            self.remove_node(self.tail)

#first element remove     
    def remove_first(self):
        if self.head is not None:
            self.remove_node(self.head)

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append((node.val))
            node = node.next
        return f"[{','.join(str(val) for val in vals)}]"

my_list = Double_Linked_List()
my_list.Append(1)
my_list.Append(2)
my_list.Append(3)
my_list.Append(4)
my_list.Append(5)
my_list.Append(6)
my_list.Append(7)
my_list.Append(8)
my_list.Append(9)
my_list.Append(10)

print("Total element append =",my_list)
print("Tatal size =",my_list.size)
'''
# Only First element remove
print("First Element Remove:")
my_list.remove_first()
print(my_list)

#Only Last element remove
print("Last Element Remove:")
my_list.remove_last()
print(my_list)
'''
my_list.remove(int(input("Please Enter the Remove Element: ")))
print("Update list =",my_list)
print("Update size =",my_list.size)

my_list.remove(int(input("Please Enter the Remove Element: ")))
print("Update list =",my_list)
print("Update size =",my_list.size)

my_list.remove(int(input("Please Enter the Remove Element: ")))
print("Update list =",my_list)
print("Update size =",my_list.size)
