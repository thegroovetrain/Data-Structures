"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __iter__(self):
        self.n = 1
        self.pointer = self.head
        return self

    def __next__(self):
        if self.n <= len(self):
            value = self.pointer.value
            self.n += 1
            self.pointer = self.pointer.next
            return value
        else:
            raise StopIteration

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head is None:
            new_head = ListNode(value, None, None)
            self.head = self.tail = new_head
        else:
            old_head = self.head
            new_head = ListNode(value, None, old_head)
            old_head.prev = self.head = new_head
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            current_head = self.head
            self.head = self.tail = None
            self.length -= 1
            return current_head.value
        else:
            current_head = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return current_head.value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail is None:
            new_tail = ListNode(value, None, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            old_tail = self.tail
            new_tail = ListNode(value, old_tail, None)
            old_tail.next = new_tail
            self.tail = new_tail
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        elif self.tail == self.head:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return current_tail.value
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_tail = self.tail
            self.tail = current_node
            current_node.next = None
            self.length -= 1
            return current_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = self.delete(node)
        self.add_to_head(value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node == self.head:
            return self.remove_from_head()
        elif node == self.tail:
            return self.remove_from_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            return node.value



    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        return max(self)
