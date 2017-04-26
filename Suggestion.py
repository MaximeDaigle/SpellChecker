class Suggestion:
	# cette classe servira a creer les suggestions si le mot n'est pas dans la hashtable

	def __init__(self, mot, alphabet):
		self.tab = []
		self.tabPaire =[]
		self.mot = mot
		# il faudra modifier les autres class pour que l'alphabet se crée a partir de dict.txt
		self.alphabet = alphabet


	def createSuggestion(self):
		# on appellera toutes les méthodes de suggestions de mots qu'il faut ici pour remplir le self.tab
		self.intervertir()
		self.supprimer()
		self.inserer()
		self.remplacer()
		self.separer()


	def intervertir(self):
		if len(self.mot) >= 2:
			for lettre in range(len(self.mot)-1):
				motTemp = self.mot
				temp = ""
				temp += motTemp[lettre+1]+motTemp[lettre]
				motTemp = self.mot[0:lettre] + temp + self.mot[lettre+2:len(self.mot)]
				self.tab += [motTemp]


	def supprimer(self):
		if len(self.mot) >= 2:
			for lettre in range(len(self.mot)):
				motTemp = self.mot
				motTemp = self.mot[0:lettre] + self.mot[lettre+1:len(self.mot)]
				self.tab += [motTemp]


	def inserer(self):
		# il faudra modifier le code pour creer l'alphabet a partir de dict.txt
		for lettre in range(len(self.mot)+1):
			for char in self.alphabet:
				motTemp = self.mot
				motTemp = self.mot[0:lettre] + char + self.mot[lettre:len(self.mot)]
				self.tab += [motTemp]


	def remplacer(self):
		for lettre in range(len(self.mot)):
			for char in self.alphabet:
				motTemp = self.mot
				motTemp = self.mot[0:lettre] + char + self.mot[lettre+1:len(self.mot)]
				self.tab += [motTemp]


	def separer(self):
		for lettre in range(len(self.mot)-1):
			motTemp = self.mot
			temp1 = [self.mot[0:lettre+1]]
			temp2 = [self.mot[lettre+1:len(self.mot)]]
			self.tabPaire += [temp1 + temp2]