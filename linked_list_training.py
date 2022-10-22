# node class

class Node(object):

	def __init__(self, data):

		# Node initialize node yarat

		self.data = data
		self.next = None



# Linked List class

class LinkedList(object):

	def __init__(self):

		# Head initializer

		self.head = None

	def push(self, new_data):

		# Linked List başına node ekler

		# node yarat ve içerisindeki veriyi belirler
		new_node = Node(new_data)

		# yeni node kendisinden sonra gelen node u işaret etsin
		new_node.next = self.head

		# head yeni node u işaret etsin
		self.head = new_node

	def insertAfter(self, prev_node, new_data):

		# Verilen (prev node) verilen node dan sonra yeni node ekle

		# prev_node var mı yok mu onu kontrol et
		if prev_node is None:
			print("Boyle bir node yok")
			return
		
		# yeni node yarat ve içerisine veri koy
		new_node = Node(new_data)

		# new_node next'ini prev_node next'i yap
		new_node.next = prev_node.next

		# prev_noce next'i new node yap		
		prev_node.next = new_node


	def append(self, new_data):

		# Linked list sonuna node eklemek


		# yeni node yarat daha sonra içerisine new_data verisini depola
		new_node = Node(new_data)

		# eğer linked list boş ise yeni eklenen node head olsun
		if self.head is None:
			self.head = new_node
			return

		# linked list'in head'inden başla sonuna kadar git
		last = self.head
		while last.next:
			last = last.next

		# last.next None. onun yerine new_node ekle	
		last.next = new_node

	def deleteNode(self, key):

		# istenilen key'e göre node sil

		temp = self.head

		# eğer tek bir node var ve bu node istenilen değere sahipse
		if temp is not None:
			if temp.data == key:
				self.head = temp.next
				temp = None
				return

		# nodu silmek için key parametresini ara
		while temp is not None:
			if temp.data == key:
				break
			prev = temp
			temp = temp.next


		# node'u sil
		prev.next = temp.next
		temp = None

	def printLinkedList(self):

		# Linked List print eder

		temp = self.head
		print("Linked List: ")
		while temp:
			print(temp.data)
			temp = temp.next




"""linked_list = LinkedList()

linked_list.push("tail")
linked_list.push(15)
linked_list.push(25)
linked_list.push("head")

linked_list.insertAfter(linked_list.head, 100)

linked_list.insertAfter(linked_list.head.next.next, "insert")

#linked_list.printLinkedList()

linked_list.append("sona eklenen eleman")
linked_list.append("en sona node ekle")

linked_list.printLinkedList()"""

linked_list = LinkedList()
linked_list.push("ankara")
linked_list.push("bolu")
linked_list.push("istanbul")
linked_list.printLinkedList()

print()

linked_list.deleteNode("ankara")
linked_list.printLinkedList()