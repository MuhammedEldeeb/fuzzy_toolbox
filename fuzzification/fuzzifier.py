import matplotlib.pyplot as plt
from fuzzification.fuzzy_set import in_zone
class Fuzzifier:
    def __init__(self):
        self.fuzzySets = []
        self.rules = []
        self.output = None

    def set_fuzzySets(self , fuzzySets):
        for f in fuzzySets:
            if f.type:
                self.fuzzySets.append(f)
            else:
                self.output = f

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

    def drawVars(self, inputs=True , value=0):
        if inputs:
            for var in self.fuzzySets:
                plt.figure(figsize=(12, 5))
                ax = plt.subplot()
                for term in var.terms:
                    if term.type == False:  # triangle
                        ax.plot(term.points , [0 , 1 , 0], label=term.name)
                    else:  # trapezoidal
                        ax.plot(term.points , [0 , 1 , 1 , 0], label=term.name)
                ax.bar([var.value], [1], width=0.2, color='r', label='crisp_value')
                ax.set_xlabel(var.name)
                ax.set_ylabel('Member Func')
                ax.set_title(var.name + ' vs. Member Func')
                ax.legend()
                plt.show()
        else:
            plt.figure(figsize=(12,5))
            ax = plt.subplot()
            for term in self.output.terms:
                if term.type == False:  # triangle
                    ax.plot(term.points, [0, 1, 0], label=term.name)
                else:  # trapezoidal
                    ax.plot(term.points, [0, 1, 1, 0], label=term.name)
            ax.bar([value], [1], width=0.2, color='r', label='crisp_value')
            ax.set_xlabel(self.output.name)
            ax.set_ylabel('Member Func')
            ax.set_title(self.output.name + ' vs. Member Func')
            ax.legend()
            plt.show()

    def duffuzzify(self):
        numerator = 0
        denominator = 0
        for term in self.output.terms:
            for r in self.rules:
                if (r.output.left.strip() == self.output.name.strip()) and (r.output.right.strip() == term.name.strip()):
                    numerator += (r.output.value * term.getCentroid())
                    denominator += r.output.value
        return (numerator/denominator)

    def fuzzify(self):
        for var in self.fuzzySets:
            for term in var.terms:
                term.set_equations()

        self.setMemberFunction()
                # print(var.name, term.name, term.equations[0].zone) # not complete

    def setMemberFunction(self):
        for var in self.fuzzySets:
            crisp = var.value
            for term in var.terms:
                for eq in term.equations:
                    if in_zone(crisp, eq.zone):
                        term.membershipFunc = (eq.get_y(crisp))
