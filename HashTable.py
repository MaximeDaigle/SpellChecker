from LinkedList import LinkedList


class HashTable:
    # table de hashage contenant les mots du dictionnaire

    def __init__(self, lengthdict):
        # self.tab = [LinkedList()] * lengthdict * 2
        self.tab = [LinkedList() for i in range(lengthdict * 2)]

    def hash(self, word):
        """
        polynomial accumulation avec horner's rule
        :param word: string a hasher
        :return: le hashcode de word
        """
        # si string vide
        if len(word) == 0:
            return 0

        hashcode = ord(word[len(word) - 1])
        i = len(word) - 2
        while i >= 0:
            hashcode = hashcode * 33 + ord(word[i])
            i = i - 1
        hashcode = hashcode % len(self.tab) - 1
        return hashcode

    def get(self, valeur):
        """
        :param valeur: le mot chercher dans la hashTable
        :return: retourne True si dans la hashtable, sinon False
        """
        key = self.hash(valeur)
        return self.tab[key].find(valeur)

    def set(self, valeur):
        """
        ajoute valeur dans la hashtable
        :param valeur: le mot qu'on ajoute dans le hashTable
        """
        key = self.hash(valeur)
        self.tab[key].append(valeur)