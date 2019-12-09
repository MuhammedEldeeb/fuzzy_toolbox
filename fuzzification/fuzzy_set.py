class LinguisticTerm():
    def __init__(self):
        self.name = ''
        self.type = False  # false for triangle and true for trapezoidal
        self.points = []  # points of the term on the x axis

    def show(self):
        return 'term : ' + self.name + ' (' +  str(self.type) + ') ' + str(self.points)

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
        self.output = ''

    def show(self):
        prem , pred = 0
        for _ in range(self.size):
            rule = 'rule : ('
            rule += self.premises[prem] + self.predicts[pred]
            prem += 1
            pred += 1
        rule += ')' + self.output

        print(rule)
