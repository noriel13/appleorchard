class Apple:
    def __init__(self):
        self.diameter = Math.random() * 10


class AppleTree:
    def __init__(self):
        self.alive = True


class AppleOrchard:

    def __init__(self):

        self.display = \
            """
                /\\
                ||
            """
        treeOne = AppleTree()
        treeTwo = AppleTree()
        treeTwo.alive = False
        self.trees = [treeOne, treeTwo]


    def num_trees(self):
        num_alive = 0
        for tree in self.trees:
            if tree.alive:
                num_alive += 1
        return num_alive

    def display_orchard(self):
        print(self.display)



if __name__ == "__main__":
    pass

