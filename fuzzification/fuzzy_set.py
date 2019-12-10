class LinguisticTerm():
    def __init__(self):
        self.name = ''
        self.type = False  # false for triangle and true for trapezoidal
        self.points = []  # points of the term on the x axis
        self.membershipFunc = 0

    def show(self):
        return 'term : ' + self.name + ' (' +  str(self.type) + ') ' + str(self.points) + ' ((' + str(self.membershipFunc) +'))'

class LinguisticVar():
    def __init__(self):
        self.value = 0  # crisp Value ==> value 0 if it is output
        self.type = False  # false for output and true for input
        self.name = ''
        self.terms = []

    def show(self):
        print('var : ' + self.name + ' (' + str(self.type) + ') ' + str(self.value) )
        for term in self.terms:
            print('\t' , term.show())

class Rule():
    def __init__(self):
        self.size = 0
        self.premises = []
        self.predicts = []
        self.output = None

    def show(self):
        n = len(self.predicts)
        for i in range(n):
            print(self.premises[i].show() + self.predicts[i])
        print(self.premises[n].show())

        print( '==> (' + self.output.left , self.output.equal, self.output.right + ') ((' + str(self.output.value) + '))')
        # print('==>' , self.output.show())

class Premise():
    def __init__(self):
        self.left = ''
        self.equal = True
        self.right = ''
        self.value = 0

    def show(self):
        return '(' + self.left + ' ' + str(self.equal) + ' ' + self.right + ') ((' + str(self.value) + '))'