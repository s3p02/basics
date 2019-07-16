class lb:
	def __init__(self,iList):
		self.iList = iList
	
	def printList(self):
		print("___________________________")
		print("index\t:\telement")
		print("___________________________")
		for i in range(len(self.iList)):
			print(str(i)+"\t:\t"+self.iList[i])
	def add2list(self,additionalElement):
		self.iList.append(additionalElement)

	def checkForDuplicates(self):
		listSet = set(self.iList)
		if(len(listSet) != len(self.iList)):
			print("Duplicates Exist\n")
		else:
			print("No Duplicates\n")

	def removeDuplicates(self):
		lbSet = set(self.iList)
		del self.iList[:]
		self.iList = list(lbSet)

	def removeElement(self,element2remove):
		#Removes first match
		self.iList.remove(element2remove)

	def removeIndex(self,indexNo):
		del self.iList[indexNo]
