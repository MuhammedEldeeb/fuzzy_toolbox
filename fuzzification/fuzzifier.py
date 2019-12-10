import matplotlib.pyplot as plt
class Fuzzifier():

    def __init__(self):
        self.fuzzySets = []
        self.rules = []

    def set_fuzzySets(self , fuzzySets):
        self.fuzzySets = fuzzySets

    def set_rules(self , rules):
        self.rules = rules

    def apply_rules(self):
        # get values of the premises
        for rule in self.rules:
            for premise in rule.premises:
                self.evaluate_premises(premise)

        # get value of the output of the rules
        self.evaluate_rules()



    def evaluate_rules(self):
        for rule in self.rules:
            value = 0
            n = len(rule.predicts)
            for i in range(n):
                if i == 0:
                    value = self.oring(value, rule.premises[i])
                if rule.predicts[i] == 'OR':
                    value = self.oring(value, rule.premises[i+1])
                elif rule.predicts[i] == 'AND':
                    value = self.anding(value, rule.premises[i+1])
            rule.output.value = value

    def anding(self, num, p):
        return num if num < p.value else p.value

    def oring(self, num, p):
        return num if num > p.value else p.value

    def evaluate_premises(self, premise):
        for var in self.fuzzySets:
            for term in var.terms:
                if var.name == premise.left and term.name == premise.right and premise.equal:
                    premise.value = term.membershipFunc
                elif var.name == premise.left and term.name == premise.right and premise.equal == False:
                    premise.value = 1 - term.membershipFunc

    def drawVars(self, inputs=True):
        for var in self.fuzzySets:
            if var.type == inputs:
                plt.figure(figsize=(12, 5))
                ax = plt.subplot()
                for term in var.terms:
                    if term.type == False:  # triangle
                        ax.plot(term.points , [0 , 1 , 0], label=term.name)
                    else:  # trapezoidal
                        ax.plot(term.points , [0 , 1 , 1 , 0], label=term.name)
                if inputs:
                    ax.bar([var.value], [1], width=0.1, color='r', label='crisp_value')
                ax.set_xlabel(var.name)
                ax.set_ylabel('Member Func')
                ax.set_title(var.name + ' vs. Member Func')
                ax.legend()
                plt.show()

    def draw_output(self):
        for var in self.fuzzySets:
            if var.type == False:
                plt.figure(figsize=(12, 5))
                ax = plt.subplot()
                for term in var.terms:
                    if term.type == False:  # triangle
                        ax.plot(term.points , [0 , 1 , 0], label=term.name)
                    else:  # trapezoidal
                        ax.plot(term.points , [0 , 1 , 1 , 0], label=term.name)
                ax.set_xlabel(var.name)
                ax.set_ylabel('Member Func')
                ax.set_title(var.name + ' vs. Member Func')
                ax.legend()
                plt.show()

    def get_centroid(self, term):
        return sum(term.points)/len(term.points)

    def duffuzzify(self):
        numerator , denominator = 0
        for var in self.fuzzySets:
            if var.type == False:  # if it is an output
                for term in var.terms:
                    pass
