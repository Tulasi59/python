class Node:
	def __init__(self,value):
		self.next = None
		self.data = value

class LinkedList:

	def __init__(self):
		self.head = None

	def traverse(self):
		head = self.head
		while head:
			print(head.data)
			head = head.next

	def insert(self, value):
		newNode = Node(value)
		newNode.next = self.head
		self.head = newNode
			
	def insert_after(self,after_val, prev_val):
		head = self.head
		next_node = self.head
		while head:
			next_node = head.next
			if head.data == prev_val:
				newNode = Node(after_val)
				newNode.next = next_node
				head.next = newNode
				break;
			head = head.next

	def inset_last(self):
		head = self.head
		while head:
			head = head.next
		newnode = Node(25)
		head.next = newnode


	def sorted_array(self,value):

		previous = self.head
		nextnode = self.head
		head = self.head
		newNode = Node(value)
		# import pdb;pdb.set_trace()
		while head and nextnode.next:
			
			nextnode = nextnode.next
			if head.data > value:
				newNode.next = head
				head.next = newNode

			elif previous.data < value and nextnode.data > value:
					previous.next = newNode
					newNode.next = nextnode
					break;
					
			else:
				pass
			previous = head.next
			head = head.next


		# head.next = newNode

if __name__ == '__main__':
	obj = LinkedList()
	obj.insert(40)
	obj.insert(30)
	obj.insert(20)
	obj.insert(10)
	# obj.insert_after(70,20)	

	#obj.sorted_array(5)
	#obj.traverse()
