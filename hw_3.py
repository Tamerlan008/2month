class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __make_computations(self, operation):
        if operation == '+':
            result = self.__cpu + self.__memory
        elif operation == '-':
            result = self.__cpu - self.__memory
        elif operation == '*':
            result = self.__cpu * self.__memory
        elif operation == '/':
            if self.__memory != 0:
                result = self.__cpu / self.__memory
            else:
                result = "Division by zero error"
        else:
            result = "Invalid operation"
        return result

    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    def info(self):
        print("Computer:")
        print(f"CPU: {self.get_cpu()}")
        print(f"Memory: {self.get_memory()}")

    def test_operations(self):
        print("Testing operations:")
        operations = ['+', '-', '*', '/']
        for op in operations:
            print(f"Operation {op}: {self.__make_computations(op)}")


class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    def get_memory_card(self):
        return self.__memory_card

    def info(self):
        super().info()
        print(f"Memory Card: {self.get_memory_card()}")


computer = Computer(4, 8)
laptop = Laptop(2, 4, "256GB SSD")

computer.info()
computer.test_operations()

print("\n")

laptop.info()
laptop.test_operations()
