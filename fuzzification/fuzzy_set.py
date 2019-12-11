class LinguisticTerm:
    def __init__(self):
        self.name = ''
        self.type = False  # false for triangle and true for trapezoidal
        self.points = []  # points of the term on the x axis
        self.membershipFunc = 0
        self.equations = []

    def set_equations(self):
        points = self.get_points()
        if self.type:  # trapezoidal
            eq1 = Equation(x1=points[0][0], x2=points[1][0], y1=points[0][1], y2=points[1][1])
            eq2 = Equation(x1=points[1][0], x2=points[2][0], y1=points[1][1], y2=points[2][1])
            eq3 = Equation(x1=points[2][0], x2=points[3][0], y1=points[2][1], y2=points[3][1])

            self.equations.append(eq1)
            self.equations.append(eq2)
            self.equations.append(eq3)

        else:
            eq1 = Equation(x1=points[0][0], x2=points[1][0], y1=points[0][1], y2=points[1][1])
            eq2 = Equation(x1=points[1][0], x2=points[2][0], y1=points[1][1], y2=points[2][1])

            self.equations.append(eq1)
            self.equations.append(eq2)

    def get_points(self):
        if self.type:
            return [[self.points[0], 0], [self.points[1], 1], [self.points[2], 1] , [self.points[3] , 0]]
        else:
            return [[self.points[0] , 0] , [self.points[1] , 1] , [self.points[2] , 0]]

    def getArea(self):
        points = self.get_points()
        area = 0
        for i in range(0, len(points) - 1):
            area += (points[i][0] * points[i + 1][1]) - \
                    (points[i + 1][0] * points[i][1])
        return abs(area) * 0.5

    def getCentroid(self):
        points = self.get_points()
        sum = 0
        for i in range(0, len(points) - 1):
            sum += (points[i][0] + points[i + 1][0]) * \
                   ((points[i][0] * points[i + 1][1]) -
                    (points[i + 1][0] * points[i][1]))

        value = abs(sum) * (1 / (6 * self.getArea()))

        return value


    def show(self):
        return 'term : ' + self.name + ' (' +  str(self.type) + ') ' + str(self.points) + ' ((' + str(self.membershipFunc) +'))'


class LinguisticVar:
    def __init__(self):
        self.value = 0  # crisp Value ==> value 0 if it is output
        self.type = False  # false for output and true for input
        self.name = ''
        self.terms = []

    def show(self):
        print('var : ' + self.name + ' (' + str(self.type) + ') ' + str(self.value) )
        for term in self.terms:
            print('\t' , term.show())


class Rule:
    def __init__(self):
        self.size = 0
        self.premises = []
        self.predicts = []
        self.output = None # obj of premise type

    def show(self):
        n = len(self.predicts)
        rule = ''
        for i in range(n):
            rule += (self.premises[i].show() + self.predicts[i] )
        rule += (self.premises[n].show())
        if self.output.equal:
            rule += ( '==> (' + self.output.left + ' = ' +  self.output.right + ') ((' + str(self.output.value) + '))')
        else:
            rule += ( '==> (' + self.output.left + ' != ' +  self.output.right + ') ((' + str(self.output.value) + '))')

        print(rule)


class Premise:
    def __init__(self):
        self.left = ''
        self.equal = True
        self.right = ''
        self.value = 0  # evaluation of the premise

    def show(self):
        if self.equal:
            return '(' + self.left + ' = ' + self.right + ') ((' + str(self.value) + ')) '
        else:
            return '(' + self.left + ' != ' + self.right + ') ((' + str(self.value) + ')) '

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
            return 1
        else:
            return (equation[0] * x) + equation[1]

def in_zone(value, zone):
    if value >= zone[0] and value <= zone[1]:
        return True
    else:
        return False