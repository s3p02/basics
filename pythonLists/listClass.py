class lb:
	def __init__(self,inputList):
		self.inputList = inputList
	
	def printList(self):
		for i in self.inputList:
			print(i)
	def add2list(self,additionalElement):
		self.inputList.append(additionalElement)

	def checkForDuplicates(self):
		listSet = set(self.inputList)
		if(len(listSet) != len(self.inputList)):
			print("Duplicates Exist\n")
		else:
			print("No Duplicates\n")

	def removeDuplicates(self):
		lbSet = set(self.inputList)
		self.inputList.clear()
		self.inputList = list(lbSet)
