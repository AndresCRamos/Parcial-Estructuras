class Tree2:
    def get_elements(self):
        return self.__elements

    def __init__(self, level):
        self.__elements = []
        for a in range(2**(level+1)):
            if a % 2 == 0:
                self.__elements.append(True)
            else:
                self.__elements.append(False)

    def close(self, index):
        if self.__elements[index]:
            self.__elements[index] = False
        else:
            self.__elements[index] = True

    def start(self):
        def ball(index_n):
            jump = (index_n * 2)

            if jump+1 > len(self.get_elements()):
                return index_n
            else:
                if self.get_elements()[jump] is True:
                    self.close(jump)
                    self.close(jump+1)
                    return ball(jump)
                elif self.get_elements()[jump+1] is True:
                    self.close(jump)
                    self.close(jump+1)
                    return ball(jump+1)
        return ball(1)
