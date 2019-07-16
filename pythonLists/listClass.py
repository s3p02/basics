class lb:
	def __init__(self,inputList):
		self.inputList = inputList
	
	def printList(self):
		print("___________________________")
		print("index\t:\telement")
		print("___________________________")
		for i in range(len(self.inputList)):
			print(str(i)+"\t:\t"+self.inputList[i])
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
		del self.inputList[:]
		self.inputList = list(lbSet)

	def removeElement(self,element2remove):
		#Removes first match
		self.inputList.remove(element2remove)

	def removeIndex(self,indexNo):
		del self.inputList[indexNo]
