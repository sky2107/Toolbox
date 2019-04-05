

class Node():
    """ nodes l + r plus data """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        self.pointer_l = self.left
        self.pointer_r = self.right

    def add(self, flag, data):
        if flag == 'l':
            self.left = Node(data)
            self.pointer_l = self.left.pointer_l
        else:
            self.right = Node(data)
            self.pointer_r = self.right.pointer_r



if __name__ == '__main__':
    root = Node(21)
