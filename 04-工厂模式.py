# 大批量创建对象的时候有统一的入口，易于代码维护
# 当发生修改时，仅修改工厂类的创建方法即可

class Person:
    pass
class Worker(Person):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

class PersonFactory:     #创建一个额外的工厂类
    def get_person(self,p_type):
        if p_type=='w':
            return Worker()
        elif p_type=='s':
            return Student()
        else:
            return Teacher()

pf=PersonFactory()
worker=pf.get_person('w')
stu=pf.get_person('s')
teacher=pf.get_person('t')







