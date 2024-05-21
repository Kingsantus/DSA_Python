num1 = 34

# print(id(num1))

num2 = num1

# print(id(num2))

head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

# print(head['next']['next']['value'])

# link list is a nested dictionary
class Node:
    def __init__(self, value):
        """Node"""
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        """Create a new node"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """Create a new node and add it to the end"""
        new_node = Node(value)
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """Remove a node and rearrange the tail"""
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while(temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp

    def prepend(self, value):
        """Create a new node and add it to the beginning"""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """Removing a node from the head of the linked list"""
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        """Get the value of the node at the given index"""
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        """Set the value at the given index in the linked list"""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        """Create a new node and insert the Node"""
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        """Removes a node from the list of nodes"""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse_list(self):
        """Return a list of reversed lists"""
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        



# print(my_linkedlist.head.value)
# print(my_linkedlist.tail.value)
my_linkedlist = LinkedList(5)
my_linkedlist.append(2)
my_linkedlist.append(3)
my_linkedlist.append(23)

# my_linkedlist.print_list()
# my_linkedlist.pop_first()
# my_linkedlist.pop_first()
# my_linkedlist.pop_first()

# print(my_linkedlist.get(0))
#my_linkedlist.prepend(1)
# my_linkedlist.set_value(2, 54)
# my_linkedlist.insert(2,45)
# my_linkedlist.remove(1)
my_linkedlist.reverse_list()


my_linkedlist.print_list()

# print(my_linkedlist.pop())
# print(my_linkedlist.pop())
# print(my_linkedlist.pop())
# print(my_linkedlist.pop())