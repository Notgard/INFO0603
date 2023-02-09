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

    def add(self, data: Tuple):
        if self.left == None:
            print("left", data)
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
            print("ok")
            self.right = BinaryTree(self)
            print(self.right.data)
            self.left = None
            self.add(data)

    def __str__(self):
        pass

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
    print(values)
    for value in values:
        tree.add(value)
    print(tree.left.data, tree.data, tree.right)
