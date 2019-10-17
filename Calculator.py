class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a+b

    def difference(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b


class ScienceCalculator(Calculator):
    def pot(self, a, b):
        return a**b

kalk=ScienceCalculator()
print(kalk.pot(2, 3))