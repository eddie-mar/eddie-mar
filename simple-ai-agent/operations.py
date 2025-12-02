from abc import ABC, abstractmethod

class AbsOperator(ABC):
    @abstractmethod
    def calculate(self):
        raise NotImplementedError
    
class Add(AbsOperator):
    def calculate(self, a, b):
        return a + b

class Subtract(AbsOperator):
    def calculate(self, a, b):
        return a - b

class Divide(AbsOperator):
    def calculate(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b

class Multiply(AbsOperator):
    def calculate(self, a, b):
        return a * b
    

class OperatorFactory:
    @staticmethod
    def get(operator: str) -> AbsOperator:
        mapping = {
            '+': Add,
            '-': Subtract,
            '/': Divide,
            '*': Multiply
        }

        try: 
            return mapping[operator]()
        except KeyError:
            raise ValueError(f'Unknown operator: {operator}')



