
from Node import Node

class LinkedList():

    def __init__( self ):
        self.head = None
        self.last = None
        self.size = 0

    def append( self, valeur ):
        """
        ajoute un noeud contenant valeur a la fin de la linkedlist
        :param valeur: le mot du dictionnaire
        """
        newNode = Node(valeur)
        if self.head == None:
            self.head = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.size += 1

    def find( self, valeur ):
        """
        :param valeur: la valeur chercher dans la linkedlist
        :return:  True si find la valeur dans la linkedlist, False sinon
        """
        currentNode = self.head
        for i in range( self.size ):
            if currentNode.valeur == valeur:
                return True
            else:
                currentNode = currentNode.next
        return False

    def lastNode( self ):
        return self.last

    def firstNode( self ):
        return self.head