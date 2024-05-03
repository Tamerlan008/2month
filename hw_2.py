class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    
    def introduce_myself(self):
        print(f"Привет, меня зовут {self.fullname}. Мне {self.age} лет. {'Я замужем.' if self.is_married else 'Я не замужем.'}")


class Teacher(Person):
    salary = 0

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        self.salary = 20000 + self.experience * 3000

    def introduce_myself(self):
        super().introduce_myself()
        print(f"У меня опыт работы {self.experience} лет. Моя зарплата составляет {self.salary} рублей.")


teacher1 = Teacher("Иван Петровна", 46, True, 27)
teacher1.calculate_salary()
teacher1.introduce_myself()
