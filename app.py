from fuzzification.example_reader import ExampleReader
from fuzzification.fuzzifier import Fuzzifier

e = ExampleReader(r'./files/example.txt')
f = Fuzzifier()

"""
(1) Fuzzification 
"""

fuzzysets = e.get_fuzzySets()
f.set_fuzzySets(fuzzysets)
f.drawVars(inputs=True)
f.drawVars(inputs=False)
f.fuzzify()

print('FUZZIFICATION')
for var in f.fuzzySets:
    for term in var.terms:
        print('m({},{},{}) = {}'.format(var.name , term.name , var.value, term.membershipFunc))

print('-----------------------------------------------')

"""*******
(2) Apply Rules (Inference)
"""

print('INFERENCE')
# get the rules from the example
rules = e.get_rules()
# set the rules to the fuzzifier
f.set_rules(rules)
# apply rules (inference)
f.apply_rules()

for r in rules:
    r.show()
print('--------------------------------------------')
"""
(3) Defuzzification
"""
print('DEFUZZIFICATION')
print('predicted value of ' + f.output.name + ' = ' + str(f.duffuzzify()))
