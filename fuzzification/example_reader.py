from fuzzification.fuzzy_set import LinguisticVar, LinguisticTerm

def readTerms(f , num_of_terms):
    terms = []
    for term in range(num_of_terms):
        linguisticTerm = LinguisticTerm()
        desc = f.readline().split()
        term_name = desc[0]  # get the name of the term
        term_type = desc[1].lower()  # get the type of the term
        points = f.readline().split()  # get the points of the term on the x axis
        points = [int(p) for p in points]   # convert the values of the points to integers
        linguisticTerm.name = term_name.lower()
        linguisticTerm.points = points
        linguisticTerm.type = False if term_type == 'triangle' else True
        terms.append(linguisticTerm)
    return terms

def readVars(f , num_of_linguistic_vars):
    vars = []
    for var in range(num_of_linguistic_vars):
        linguisticVar = LinguisticVar()
        linguisticVar.type = True  # define as input
        linguistic = f.readline().split()
        var_name = linguistic[0]  # get the linguistic variable name
        var_value = linguistic[1]  # get the crisp value for the linguistic variable
        linguisticVar.name = var_name.lower()
        linguisticVar.value = var_value
        num_of_terms = int(f.readline())  # get number of the terms of a variable linguistic variable
        """read the linguistic terms for a linguistic variables"""
        linguisticVar.terms = readTerms(f, num_of_terms)
        vars.append(linguisticVar)
    return vars

def readRules(f , num_of_rules):
    rules = []
    for rule in range(num_of_rules):
        desc = f.readline().split()  # read the rule description
        print(desc)


f = None
try:
    f = open(r'../files/example.txt', 'r')
except:
    print('there is no such file')

fuzzy_sets = []

"""read the input Fuzzy sets"""
num_of_linguistic_vars = int(f.readline())  # get number of the input fuzzy sets
"""read the input linguistic variables"""
fuzzy_sets += readVars(f , num_of_linguistic_vars)

""" read the output linguistic variables"""
outVar = LinguisticVar()
outVar.name = f.readline()
num_of_terms_outVar = int(f.readline())
outVar.terms = readTerms(f, num_of_terms_outVar)
fuzzy_sets.append(outVar)

"""read the rules"""
num_of_rules = int(f.readline())
print(num_of_rules)
rules = readRules(f, num_of_rules)

f.close()

# for f in fuzzy_sets:
#     f.show()