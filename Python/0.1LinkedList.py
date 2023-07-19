class Node:
	def __init__(self , val,next=None):
		self.val = val
		self.next = next

def print_linked_list_values(head):
	current = head
	while current:
		print(current.val)
		current = current.next 


a = Node("A")
b = Node("B")
c = Node("C")

a.next = b
b.next = c

print_linked_list_values(a)	

