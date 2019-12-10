from fuzzification.example_reader import ExampleReader
from fuzzification.fuzzifier import Fuzzifier

e = ExampleReader(r'./files/example.txt')
f = Fuzzifier()

fuzzysets = e.get_fuzzySets()

"""
(1) Fuzzification 
"""

f.set_fuzzySets(fuzzysets)
# f.drawVars(inputs=True)
# f.drawVars(inputs=False)


"""i should call f.setMemberFunction() ==> will do it mannually until it is working"""
for var in f.fuzzySets:
    if var.name == 'position':
        for term in var.terms:
            if term.name == 'Left':
                term.membershipFunc = 0.7
            else:
                term.membershipFunc = 0.3
    elif var.name == 'angel':
        for term in var.terms:
            if term.name == 'RBelow':
                term.membershipFunc = 0.6
            else:
                term.membershipFunc = 0.4
""" suppose the f.setMemberFunction() get run and will continue"""

"""*******
(2) Apply Rules (Inference)
"""
# get the rules from the example
rules = e.get_rules()
# set the rules to the fuzzifier
f.set_rules(rules)
# apply rules (inference)
f.apply_rules()


"""
(3) Defuzzification
"""
print(f.duffuzzify() )

"""
for testing
"""
# for a in f.fuzzySets:
#     a.show()
#
# for r in f.rules:
#     r.show()
print('Done')