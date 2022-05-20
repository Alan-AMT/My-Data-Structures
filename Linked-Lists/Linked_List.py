class _LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_after_node(self, data, target_node=None):
        if not target_node:
            raise ValueError ("No target node defined")
        new_node = _LinkedListNode(data)
        new_node.next = target_node.next
        target_node.next = new_node

    def append(self, data):
        if not self.head:
            self.head = _LinkedListNode(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = _LinkedListNode(data)

    def prepend(self, data):
        new_node = _LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def __str__(self,):
        current_node = self.head
        linked_list_data = ""
        while current_node:
            linked_list_data += f"{current_node.data}-"
            current_node = current_node.next
        return linked_list_data
    
    def delete(self, key):
        current_node = self.head
        if not current_node:
            raise ValueError ("Linked List is empty")
            
        if current_node.data == key:
            self.head = current_node.next
            del current_node
            gc.collect()
        else:
            while current_node.next:
                if current_node.next.data == key:
                    t = current_node.next
                    current_node.next = t.next
                    del t
                    gc.collect()
                    break
                current_node = current_node.next
            else:
                raise ValueError (f"Node {key} not found in Linked List")

my_ll = LinkedList()
my_ll.append(2)
my_ll.prepend(1)
my_ll.insert_after_node(3, my_ll.head.next)
my_ll.append(4)
print(my_ll)

my_ll.delete(4)
print(my_ll)
