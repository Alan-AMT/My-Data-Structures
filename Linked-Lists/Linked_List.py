class _LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def insert_after_node(self, data, target_node=None):
        if not target_node:
            raise ValueError ("No target node defined")
        new_node = _LinkedListNode(data)
        new_node.next = target_node.next
        target_node.next = new_node
        self._size += 1

    def append(self, data):
        if not self.head:
            self.head = _LinkedListNode(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = _LinkedListNode(data)
        self._size += 1

    def prepend(self, data):
        new_node = _LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

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
        self._size -= 1
    
    def __len__(self):
        return self._size
    
    def swap_nodes(self, key1, key2):
        current1 = self.head
        prev1 = None
        if not current1:
            raise ValueError ("Nodes not found in linked List")
        
        while current1:
            if current1.data == key1:
                break
            elif current1.data == key2:
                break
            else:
                prev1 = current1
                current1 = current1.next
        else:
            raise ValueError ("Nodes not found in linked List")
        
        current2 = current1.next
        prev2 = current1
        while current2:
            if current2.data == key1:
                break
            elif current2.data == key2:
                break
            else:
                prev2 = current2
                current2 = current2.next
        else:
            raise ValueError ("Nodes not found in linked List")
        
        if prev1:
            prev1.next, prev2.next = current2, current1
            current2.next, current1.next = current1.next, current2.next
        else:
            self.head, prev2.next = current2, current1
            current2.next, current1.next = current1.next, current2.next

    def reverse(self):
        nodes = []
        current = self.head
        if not current:
            raise ValueError ("Can't reverse an empty Linked List")

        while current:
            nodes.append(current)
            current = current.next

        current = self.head = nodes.pop()
        while len(nodes) > 0:
            current.next = nodes.pop()
            current = current.next

if __name__ == "__main__":
    my_ll = LinkedList()
    my_ll.append(2)
    my_ll.prepend(1)
    my_ll.insert_after_node(3, my_ll.head.next)
    my_ll.append(4)
    print(my_ll)

    my_ll.delete(4)
    print(my_ll)
    my_ll.swap_nodes(3,1)
    print(my_ll)
    print(len(my_ll))

    y = LinkedList()
    y.append("a")
    y.append("b")
    y.append("c")
    y.append("d")
    y.reverse()
    print(y.head.data)
    print(y.head.next.data)
    print(y.head.next.next.data)
    print(y.head.next.next.next.data)