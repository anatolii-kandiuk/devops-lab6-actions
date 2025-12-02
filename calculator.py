class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == "__main__":
    calc = Calculator()
    print("Calculator Demo")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 + 20 = {calc.add(10, 20)}")
