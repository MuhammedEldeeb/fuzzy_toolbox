from fuzzification.fuzzy_set import LinguisticVar, LinguisticTerm, Rule, Premise

class ExampleReader():

    def __init__(self , filename):
        self.f = None
        try:
            self.f = open(filename, 'r')
        except:
            print('there is no such file')

        self.fuzzy_sets = []

        """read the input Fuzzy sets"""
        num_of_linguistic_vars = int(self.f.readline())  # get number of the input fuzzy sets
        """read the input linguistic variables"""
        self.fuzzy_sets += self.readVars(num_of_linguistic_vars)

        """ read the output linguistic variables"""
        outVar = LinguisticVar()
        outVar.name = self.f.readline()
        num_of_terms_outVar = int(self.f.readline())
        outVar.terms = self.readTerms(num_of_terms_outVar)
        self.fuzzy_sets.append(outVar)

        """read the rules"""
        num_of_rules = int(self.f.readline())
        # print(num_of_rules)
        self.rules = self.readRules(num_of_rules)

        self.f.close()

    def get_fuzzySets(self):
        return self.fuzzy_sets

    def get_rules(self):
        return self.rules

    def readTerms(self, num_of_terms):
        terms = []
        for _ in range(num_of_terms):
            linguisticTerm = LinguisticTerm()
            desc = self.f.readline().split()
            term_name = desc[0]  # get the name of the term
            term_type = desc[1].lower()  # get the type of the term
            points = self.f.readline().split()  # get the points of the term on the x axis
            points = [int(p) for p in points]   # convert the values of the points to integers
            linguisticTerm.name = term_name
            linguisticTerm.points = points
            linguisticTerm.type = False if term_type == 'triangle' else True
            terms.append(linguisticTerm)
        return terms

    def readVars(self,num_of_linguistic_vars):
        vars = []
        for _ in range(num_of_linguistic_vars):
            linguisticVar = LinguisticVar()
            linguisticVar.type = True  # define as input
            linguistic = self.f.readline().split()
            var_name = linguistic[0]  # get the linguistic variable name
            var_value = int(linguistic[1])  # get the crisp value for the linguistic variable
            linguisticVar.name = var_name
            linguisticVar.value = var_value
            num_of_terms = int(self.f.readline())  # get number of the terms of a variable linguistic variable
            """read the linguistic terms for a linguistic variables"""
            linguisticVar.terms = self.readTerms(num_of_terms)
            vars.append(linguisticVar)
        return vars

    def readRules(self , num_of_rules):
        rules = []
        for _ in range(num_of_rules):
            rule = Rule()
            premesis = []
            predicts = []
            desc = self.f.readline().split()  # read the rule description
            rule.size = int(desc[0])
            i = 1
            for _ in range(rule.size):
                premise = Premise()
                premise.left = desc[i]
                premise.equal = True if desc[i+1] == '=' else False
                premise.right = desc[i+2]
                premesis.append(premise)
                if desc[i+3] != 'then':
                    predicts.append(desc[i+3])
                    i += 4
                else:
                    output = Rule()
                    output.left = desc[i+4]
                    output.equal = True if desc[i+5] == '=' else False
                    output.right = desc[i+6]
                    rule.output = output
                    break
            rule.premises = premesis
            rule.predicts = predicts
            rules.append(rule)
        return rules