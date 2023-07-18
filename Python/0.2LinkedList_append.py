class Node:
    def __init__(self,val,next = None) -> None:
        self.val = val 
        self.next = next 

class LinkedList:
    
    def __init__(self) -> None:
        self.head = None 
    
    def append(self , data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            current = self.head 
            while current.next:
                current = current.next
            current.next = new_node

    def print_linked_list(self):
        current = self.head 
        while current:
            print(current.val)
            current = current.next 

               
LinkedList =  LinkedList()
LinkedList.append('Aboud')
LinkedList.append(2003)
LinkedList.append(19)
LinkedList.print_linked_list()


        

