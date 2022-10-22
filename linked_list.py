# Singly linked list
#head ilk node, tail son node
#nodelardan oluşan sıralı liste
#her bir node veri ve pointer depolar
"""
class Node(object):

	def __init__(self, value):
		
		#Node yarat: node has value and next pointer

		
		self.value = value
		self.nextnode = None

	def setNextNode(self, node):
		
		#next nodeun ne olduğunu set eder
		
		self.nextnode = node

	def getNextNode(self):
		
		#bir sonraki nodeu return eder
		
		return self.nextnode

	def getNodeValue(self):
		
		#node içerisinde depolanan değeri return eder
		
		return self.value

# node sehir. node value sehir plakası
ankara = Node("06")
bolu = Node("14")
istanbul = Node("34")

ankara.setNextNode(bolu)

print(ankara.getNextNode().getNodeValue())

bolu.setNextNode(istanbul)
"""
#print(bolu.getNextNode().getNodeValue())

#ankara => bolu => istanbul

#print(ankara.getNextNode().getNextNode().getNodeValue())

# Doubly Linked List

# Her bir node kendisinden önceki ve sonraki node'un pointer'ını tutar

class doublyLinkedListNode(object):

	def __init__(self, value):

		# Node yarat: node has value and next pointer and prev pointer

		self.value = value
		self.nextnode = None
		self.prevnode = None

	def setNextNode(self, node):

		# Next nodeun ne olduğunu set eder

		self.nextnode = node

	def setPrevNode(self, node):

		# Next nodeun ne olduğunu set eder

		self.prevnode = node
		
	def getNextNode(self):

		# Bir sonraki node u döndür

		return self.nextnode

	def getPrevNode(self):

		# Bir sonraki node u döndür

		return self.prevnode
		
	def getNodeValue(self):

		# Node içerisinde depolanan veriyi return eder

		return self.value

ankara = doublyLinkedListNode("06")
bolu = doublyLinkedListNode("14")
istanbul = doublyLinkedListNode("34")

# ankara => bolu
ankara.setNextNode(bolu)

# bolu => ankara
bolu.setPrevNode(ankara)

# ankara <=> bolu
print(bolu.getPrevNode().getNodeValue())
print(ankara.getNextNode().getNodeValue())

# bolu => istanbul
bolu.setNextNode(istanbul)
print(istanbul.getPrevNode)

# istanbul => bolu
istanbul.setPrevNode(bolu)
print(istanbul.getPrevNode().getNodeValue())

# istanbul => bolu => ankara
print(istanbul.getPrevNode().getPrevNode().getNodeValue())

