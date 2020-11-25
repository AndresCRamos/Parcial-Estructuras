class Tree:
    def __init__(self, num):
        self.__elements = []
        for a in range((2**(num+1))-1):
            self.__elements.append(
                [True, False]
            )

    def close(self, index):
        element = self.get_elements()[index]
        if element[0]:
            element[0] = False
            element[1] = True
        else:
            element[0] = True
            element[1] = False

    def start(self):
        def ball(node_index):
            lis = self.get_elements()
            node = lis[node_index-1]
            if node[0]:
                jump_to = 2 * node_index
            else:
                jump_to = 2 * node_index+1
            if jump_to > len(self.get_elements()):
                return node_index
            else:
                self.close(node_index-1)
                return ball(jump_to)
        return ball(1)

    def get_elements(self):
        return self.__elements

    def __str__(self):
        return str(self.get_elements())


if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        level, balls = map(int, input().split())
        new = Tree(level)
        for j in range(balls-1):
            new.start()
        print(f"Test #{i+1}: {new.start()}")
