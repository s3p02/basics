class lb:
	def __init__(self,inputList):
		self.inputList = inputList
	
	def printList(self):
		for i in self.inputList:
			print(i)
	def add2list(self,additionalElement):
		self.inputList.append(additionalElement)
