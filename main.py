import io
from HashTable import HashTable
from Suggestion import Suggestion
from TextToTab import TextToTab

with io.open('dict.txt','r',encoding='utf8') as f:
    dictionnaire = f.read()

#obtenir tous les mots du dictionnaire
dictionnaire = dictionnaire.split('\n')

#creer le hashtable selon le nombre d'entree dans le dictionnaire
hashTable = HashTable(len(dictionnaire))

alphabet = set()
#placer chaque mots du dictionnaires dans le hashtable
for i in dictionnaire:
    hashTable.set(i)
    for char in i:
        alphabet.add(char)


#Creer l'alphabet
alphabet = list(alphabet)
#alphabet = "abcdefghijklmnopqrstuvwxyz"


with io.open('input.txt','r',encoding='utf8') as f:
    inputTxt = f.read()

#retire les ponctuations
phrase = TextToTab(inputTxt)
phrase.setMot()

correctedInput = ''
#regarde chaque mot du test input
for mot in phrase.tabMot:

    #Si mot correctement orthographier (i.e est dans le dictionnaire), passer au prochain mot
    if hashTable.get(mot.lower()):
        correctedInput += ' ' +mot
        continue

    correctedInput += ' [' + mot+ ']('

    #si mal orthagraphier, creer des suggestion d'orthographes possibles
    suggestion = Suggestion(mot, alphabet)
    suggestion.createSuggestion()

    bonneSuggestion = []

    #verifier si suggestion est bonne
    for motPotentiel in suggestion.tab:
        if hashTable.get(motPotentiel):
            bonneSuggestion.append(motPotentiel)

    #verifier si pas deux mots coller
    for motPotentiel in suggestion.tabPaire:
        pass #TODO

    #enleve les repetition et ajoute les bonnes suggestions l'input corriger
    correctedInput += ', '.join(set(bonneSuggestion)) + ')'

    #enleve espace de trop devant le premier mot
    correctedInput = correctedInput.strip(' ')

print(correctedInput)



# for mot in range(len(phrase.tabMot)):
# 	suggTest = Suggestion(phrase.tabMot[mot], alphabet)
# 	suggTest.createSuggestion()
# 	print(suggTest.tab)
# 	#print(suggTest.tabPaire)
