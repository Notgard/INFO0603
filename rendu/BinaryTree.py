from typing import Tuple

class BinaryTree:
    """
    Classe d'arbre binaire qui prend un arbre de gauche, droite, des couples de données
    (lettres, valeur) et une ponderation des branches
    """

    def __init__(self, tree=None):
        if tree and isinstance(tree, BinaryTree):
            self.left = tree.left
            self.right = tree.right
            self.data = tree.data
        elif not tree:
            self.left = None
            self.right = None
            self.data = 0

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.data
        if self.right:
            yield from self.right

    def add(self, data):
        if isinstance(data, BinaryTree):
            if data.data > self.data:
                self.left = BinaryTree(self)
                self.right = data
            else:
                self.right = BinaryTree(self)
                self.left = data
            self.data += data.data
        elif isinstance(data, tuple):
            if self.left == None:
                self.left = BinaryTree()
                self.left.data = data
                self.data += data[1]
            elif self.right == None:
                self.right = BinaryTree()
                self.right.data = data
                self.data += data[1]
            elif self.data < data[1]:
                self.left = BinaryTree(self)
                self.right = None
                self.add(data)
            else: #if tree is full, create new tree: right branch with the old tree and the left branch with the value
                self.right = BinaryTree(self)
                self.left = None
                self.add(data)

    def estFeuille(self):
        return (self.left == None) and (self.data != None) and (self.right == None)

    def printTree(self, level=0, branch=None):
        if self != None:
            if self.left != None:
                self.left.printTree(level + 1, "l")
            if branch == "l":
                print(' ' * 4 * level + '╭ ' + str(self.data))
            elif branch == "r":
                print(' ' * 4 * level + '╰ ' + str(self.data))
            else:
                print(' ' * 4 * level + '-> ' + str(self.data))
            if self.right != None:
                self.right.printTree(level + 1, "r")

    def printTree_(self, level=0):
        if self != None:
            if self.left != None:
                self.left.printTree_(level + 1)
            print(' ' * 4 * level + '-> ' + str(self.data))
            if self.right != None:
                self.right.printTree_(level + 1)

if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(("a", 1))
    tree.add(("b", 1))
    tree.add(("c", 2))

    print("new", tree.right.data)

    print(list(tree))
    for node in tree:
        print(node)

    tree = BinaryTree()
    values = [("a", 3), ("b", 3), ("c", 1), ("d", 1)]
    values.sort(key=lambda x: x[1])
    print(values)
    for value in values:
        tree.add(value)
    print(list(tree))

    tree = BinaryTree()
    values = [("a", 3), ("b", 3), ("c", 1)]
    values.sort(key=lambda x: x[1])
    print("------------------------------------")
    print(values)
    for value in values:
        print("inserting" ,value)
        tree.add(value)
    print(tree.left.data, tree.data, tree.right.data)
    tree.printTree()