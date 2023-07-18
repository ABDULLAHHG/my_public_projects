class Node:
    def __init__(self,val,next = None) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None 
    
    def append(self,data):
        if self.head is None :
            self.head = Node(data)
        else:
            new_node = Node(data)
            current = self.head 
            while current.next:
                current = current.next 
            current.next = new_node
            
    def print_linked_list_values(self):
        current = self.head 
        while current:
            print(current.val)
            current = current.next 

    def linked_list_value_tolist(self):
        current = self.head
        list_values = []  
        while current:
            list_values.append(current.val)
            current = current.next
        return list_values



LinkedList = LinkedList()
LinkedList.append(1)
LinkedList.append(2)
LinkedList.append(3)

print(LinkedList.linked_list_value_tolist())
