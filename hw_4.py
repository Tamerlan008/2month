class GeeksPeople:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        print(f"name - {self.name}, email - {self.email}, phone - {self.phone}")
    
class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self,name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f" меня зовут {self.name} мой айди - {self.student_id} я учусь в группе {self.group_where_study}")

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        GeeksPeople.__init__(self,name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach(self):
        print(f" меня зовут {self.name} мой айди - {self.teacher_id} я учу группу {self.group_where_teach}")

class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self,name, email, phone)
        self.admin_id = admin_id
        
    def create_group(self):
        print(f" Меня зовут {self.name}, мой эмайл {self.email}, мой номер {self.phone} , мой айди {self.admin_id}, я создаю группу")

class Mentor(Student,Teacher):
    def __init__(self, name, email, phone, student_id, teacher_id, group_where_study, group_where_teach):
        Student.__init__(self, name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)

    def info(self):
        print(f"меня зовут {self.name} мой емайл {self.email} мой телефон {self.phone} мой айди {self.student_id}\nмой айди ментора {self.teacher_id} я учусь в группе {self.group_where_study} моя группа {self.group_where_teach}")
        
tamerlan = Student('Tamerlan', 'srgdthfsgd@gmail.com', 5765765, 1, '17-1B')
tamerlan.study()
syimyk = Teacher('Сыймык', 'kldjsljf', 18309, 13, '17-1B' )
syimyk.teach()
kamola = Admin('Kamola', 'wdjlkjf', 3247, 13 )
kamola.create_group()
eliza = Mentor('Элиза', 'dokk', 1233434234231,122,837494,'15-2b','17-1B')
eliza.info()