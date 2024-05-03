class MagicCalculator:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    
    def __add__(self, other):
        return self.number_1 + other.number_1, self.number_2 + other.number_2
    
    def __sub__(self, other):
        return self.number_1 - other.number_1, self.number_2 - other.number_2
    
    def __mul__(self, other):
        return self.number_1 * other.number_1, self.number_2 * other.number_2
    
    def __truediv__(self, other):
        return self.number_1 / other.number_1, self.number_2 / other.number_2
    
    def __floordiv__(self, other):
        return self.number_1 // other.number_1, self.number_2 // other.number_2
    
num1 = MagicCalculator(23,24)
num2 = MagicCalculator(12,12)
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)

     
     
     
# Доп задания
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __lt__(self, other):
        return self.year < other.year
    
    def __le__(self, other):
        return self.year <= other.year
    
    def __gt__(self, other):
        return self.year > other.year
    
    def __ge__(self, other):
        return self.year >= other.year
    
    def __eq__(self, other):
        return self.year == other.year
    
    def __ne__(self, other):
        return self.year != other.year
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
   
       
loh = Book('loh','loh2', 2013)
mal = Book('Mal', 'mal2', 2012)
print(loh)
print(mal)
print(loh<mal)
print(loh<=mal)
print(loh>mal)
print(loh>=mal)
print(loh==mal)
print(loh!=mal)