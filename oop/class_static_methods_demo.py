class Calculator:
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a,b):
        return a + b
    
    @classmethod
    def display_calculation_type(cls):
        print(f"Calculation type: {cls.calculation_type}")
    
    @classmethod
    def multiply(cls, a, b):
        return a * b 
    