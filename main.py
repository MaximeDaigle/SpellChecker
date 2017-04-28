import io
from HashTable import HashTable
from Suggestion import Suggestion

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

with io.open('input.txt','r',encoding='utf8') as f:
    inputTxt = f.read()

#retire les ponctuations
phrase = ''.join( char for char in inputTxt if char not in '.,:;!?\'\"').split(" ")

correctedInput = ''

#regarde chaque mot du text input
for mot in phrase:

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
        if hashTable.get(motPotentiel[0]) and hashTable.get(motPotentiel[1]):
            bonneSuggestion.append(motPotentiel[0] + ' '+ motPotentiel[1])

    #enleve les repetition et ajoute les bonnes suggestions l'input corriger
    correctedInput += ', '.join(set(bonneSuggestion)) + ')'


#enleve espace de trop devant le premier mot
correctedInput = correctedInput.strip(' ')

print(correctedInput)