from exercice1 import Node

class BinaryTree:
    def __init__(self,root):
        """
        assemblage des noeuds
        root: le noeud racine de l'arbre
        """
        self.__root=root

    def getRoot(self):
        return self.__root


if __name__=='__main__':
    """
    mes noeuds
    Creation de multitude de noeud:val,right,left
        val : la donnée du noeud
        right : le fils droit
        left : le fils gauche
    On construit de la feuille jusqu'à la racine
    """


    noeud3 = Node(3, None, None)
    noeud4 = Node(4, None, noeud3)
    noeud6 = Node(6, None, None)
    noeud5 = Node(5, noeud6, noeud4)

    noeud18 = Node(18, None, None)
    noeud21 = Node(21, None, None)
    noeud19 = Node(19, noeud21, noeud18)
    noeud17 = Node(17, noeud19, None)

    noeudRoot = Node(12, noeud17, noeud5) #noeud racine

    Root = BinaryTree(noeudRoot) #definition en tant que noeud racine







