# from fuzzification.example_reader import set_fuzzySets
# fuzzy_sets = set_fuzzySets()
#
# for f in fuzzy_sets:
#     f.show()

array = [{'value': 10,  # crisp value
         'name': 'position',
          'type': True,  # input
          'number_of_terms': 5,
          'terms': [{'name': 'left', 'type': True, 'points': [0, 0, 10, 35]},
                   {'name': 'leftcenter', 'type': False, 'points': [30, 40, 50]},
                   {'name': 'Center', 'type': False, 'points': [45, 50, 55]},
                   {'name': 'RightCenter', 'type': False, 'points': [50, 60, 70]},
                   {'name': 'Right', 'type': True, 'points': [65, 90, 100, 100]},]
         },
         {'value': -45,  # crisp value
          'name': 'angle',
          'type': True,  # input
          'number_of_terms': 7,
          'terms': [{'name': 'RBelow', 'type': False, 'points': [-90, -45, 9]},
                    {'name': 'RUpper', 'type': False, 'points': [-9, 23, 54]},
                    {'name': 'RVertical', 'type': False, 'points': [36, 63, 90]},
                    {'name': 'Vertical', 'type': False, 'points': [72, 90, 108]},
                    {'name': 'LVertical', 'type': False, 'points': [90, 117, 144]},
                    {'name': 'LUpper', 'type': False, 'points': [126, 157, 189]},
                    {'name': 'LBelow', 'type': False, 'points': [171, 225, 270]},]
          },
         {'value': 0,  # crisp value
             'name': 'firePosition',
             'type': False,  # input
             'number_of_terms': 7,
             'terms': [{'name': 'NegBig', 'type': False, 'points': [-30, -30, 15]},
                       {'name': 'NegMed', 'type': False, 'points': [-25, -15, -5]},
                       {'name': 'NegSm', 'type': False, 'points': [-12, -6, -0]},
                       {'name': 'Zero', 'type': False, 'points': [-5, 0, 5]},
                       {'name': 'PosSm', 'type': False, 'points': [0, 6, 12]},
                       {'name': 'PosMed', 'type': False, 'points': [5, 15, 25]},
                       {'name': 'PosBig', 'type': False, 'points': [15, 30, 30]},]
          } ]

class Data:
    def __init__(self):
        self.var_name = ''
        self.term_name = ''
        self.type = False
        self.equations = []


class Fuzzifier:
    def __init__(self):
        self.fuzzy_sets = array

    def in_zone(self, value, zone):
        if self.value >= self.zone[0] and self.value <= self.zone[1]:
            return True
        else:
            return False

    def set_fuzzy_sets(self, value):
        data_list = []
        for state in self.fuzzy_sets:


            for i in range(state['number_of_terms']):
                obj = Data()

                obj.var_name = state['name']
                obj.term_name = state['terms'][i]['name']
                obj.type = state['terms'][i]['type']

                if state['terms'][i]['type'] is True: # trapezoidal
                    x1 = state['terms'][i]['points'][0]; y1 = 0
                    x2 = state['terms'][i]['points'][1]; y2 = 1
                    x3 = state['terms'][i]['points'][2]; y3 = 1
                    x4 = state['terms'][i]['points'][3]; y4 = 0

                    point1 = (x1, y1)
                    point2 = (x2, y2)
                    point3 = (x3, y3)
                    point4 = (x4, y4)

                    eq1 = Equation(x1=point1[0], x2=point2[0], y1=point1[1], y2=point2[1])
                    eq2 = Equation(x1=point2[0], x2=point3[0], y1=point2[1], y2=point3[1])
                    eq3 = Equation(x1=point3[0], x2=point4[0], y1=point3[1], y2=point4[1])

                    obj.equations.append(eq1.get_equation())
                    obj.equations.append(eq2.get_equation())
                    obj.equations.append(eq3.get_equation())

                    data_list.append(obj)
                else: # triangle
                    x1 = state['terms'][i]['points'][0] ; y1 = 0
                    x2 = state['terms'][i]['points'][1] ; y2 = 1
                    x3 = state['terms'][i]['points'][2] ; y3 = 0

                    point1 = (x1, y1)
                    point2 = (x2, y2)
                    point3 = (x3, y3)

                    eq1 = Equation(x1=point1[0], x2=point2[0], y1=point1[1], y2=point2[1])
                    eq2 = Equation(x1=point2[0], x2=point3[0], y1=point2[1], y2=point3[1])

                    obj.equations.append(eq1.get_equation())
                    obj.equations.append(eq2.get_equation())

                    data_list.append(obj)
        for i in data_list:
            print(i.var_name, i.term_name, i.type, i.equations)



class Equation:
    def __init__(self, x1, x2, y1, y2):
        self.slope = self.get_slope(x1=x1, x2=x2, y1=y1, y2=y2)
        self.b = self.get_b(x1=x1, x2=x2, y1=y1, y2=y2)
        self.zone = self.get_zone(x1=x1, x2=x2)

    def get_slope(self, x1, y1, x2, y2):
        if x1 == x2:
            return None
        else:
            return (y2-y1)/(x2-x1)

    def get_b(self, x1, y1, x2, y2): # x1=10 , y1=1 , x2=20 , y2=0
        slope = self.get_slope(x1=x1, x2=x2, y1=y1, y2=y2)
        if slope is None:
            return None
        else:
            return y1 - (slope * x1)

    def get_zone(self, x1, x2):
        return [x1, x2]

    def get_equation(self):
        return [self.slope, self.b, self.zone]

    def get_y(self, x):
        equation = self.get_equation()
        # print(equation[2][1])
        if equation[0] is None:
            return None
        else:
            return (equation[0] * x) + equation[1]


# obj = Equation(x1=65, y1=0, x2=90, y2=1)
# print(obj.get_equation())
# print(obj.get_y(5))

obj = Fuzzifier()
obj.set_fuzzy_sets(10)
