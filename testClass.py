class TestClass:
    def __init__(self, name, A, B):
        self.name = name
        self.A = A
        self.B = B

    def average(self, C, D):
        average = (C+D)/2
        print(average)

    def result(self, E, F):
        print(self.name, E, F)
