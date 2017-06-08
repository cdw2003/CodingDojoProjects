# Part 1
class MathDojo(object):
    def add(self, *number):
        self.number = number
        sum = 0
        for i in range(0,len(number)):
            sum += number[i]
        print sum
        return self
    def subtract(self, *number):
        sum = 0
        for i in range(0,len(number)):
            sum -= number[i]
        print sum
        return self

md = MathDojo()
md.add(2).add(2, 5).subtract(3, 2)

# Part 2
class MathDojo(object):
    def add(self, *number):
        self.number = number
        sum = 0
        for i in range(0,len(number)):
            if type(number[i]) == list:
                for j in range(0,len(number[i])):
                    sum += float(number[i][j])
            else:
                sum += float(number[i])
        print sum
        return self
    def subtract(self, *number):
        sum = 0
        for i in range(0,len(number)):
            if type(number[i]) == list:
                for j in range(0,len(number[i])):
                    sum -= float(number[i][j])
            else:
                sum -= float(number[i])
        print sum
        return self

md = MathDojo()
md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3])

# Part 3
class MathDojo(object):
    def add(self, *number):
        self.number = number
        sum = 0
        for i in range(0,len(number)):
            if type(number[i]) == list:
                for j in range(0,len(number[i])):
                    sum += float(number[i][j])
            elif type(number[i]) == tuple:
                for num in number[i]:
                    sum += float(num)
            else:
                sum += float(number[i])
        print sum
        return self
    def subtract(self, *number):
        sum = 0
        for i in range(0,len(number)):
            if type(number[i]) == list:
                for j in range(0,len(number[i])):
                    sum -= float(number[i][j])
            elif type(number[i]) == tuple:
                for num in number[i]:
                    sum -= float(num)
            else:
                sum -= float(number[i])
        print sum
        return self

md = MathDojo()
md.add([1],3,4).add([3, 5, 7, 8], (1,2,4), [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3])
