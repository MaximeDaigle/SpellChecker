class TextToTab:

	# la classe TextToTab servira a convertir le fichier dict.txt et input.txt en un tableau contenant les mots pour que ce soit facile de creer la hashtable ou de voir si les input sont dans le hashtable

	def __init__(self, Text):
		self.tabMot = []
		self.text = Text


	def setMot(self):
		phraseMot = []
		charDeb = 0
		for i in range(len(self.text)):
			if (self.text[i] == " "):
				if len(self.text[charDeb:i]) > 0:
					phraseMot += [self.text[charDeb:i]]
				charDeb = i+1
				continue
			if (self.text[i] == "!"):
				if len(self.text[charDeb:i]) > 0:
					phraseMot += [self.text[charDeb:i]]
				charDeb = i+1
				continue
			if (self.text[i] == "\""):
				if len(self.text[charDeb:i]) > 0:
					phraseMot += [self.text[charDeb:i]]
				charDeb = i+1
				continue
			if (self.text[i] == "\'"):
				if len(self.text[charDeb:i]) > 0:
					phraseMot += [self.text[charDeb:i]]
				charDeb = i+1
				continue
			if (self.text[i] == ","):
				if len(self.text[charDeb:i]) > 0:
					phraseMot += [self.text[charDeb:i]]
				charDeb = i+1
				continue
			if (self.text[i] == "."):
				if len(self.text[charDeb:i]) > 0:
					phraseMot += [self.text[charDeb:i]]
				charDeb = i+1
				continue	
			if (self.text[i] == "?"):
				if len(self.text[charDeb:i]) > 0:
					phraseMot += [self.text[charDeb:i]]
				charDeb = i+1
				continue	
			if (self.text[i] == ":"):
				if len(self.text[charDeb:i]) > 0:
					phraseMot += [self.text[charDeb:i]]
				charDeb = i+1
				continue
			if (self.text[i] == ";"):
				if len(self.text[charDeb:i]) > 0:
					phraseMot += [self.text[charDeb:i]]
				charDeb = i+1
				continue
		self.tabMot = phraseMot		