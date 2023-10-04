# s = 'dfsjkdfagsadfgjsladg'
# print(s.capitalize())

# (object)は無くてもOK
# class Person(object):
#     def __init__(self,name):
#         self.name = name
#         # print(self.name)
#     def say_something(self):
#         # print('hello')
#         print('I am {}. hello'.format(self.name))
#         self.run(10)
#     def run(self,num):
#         print('run'*num)
#     def __del__(self):
#         print('goodbye')

# person = Person('Mike')
# person.say_something()

# del person

# print('#########')

import abc

class _Person(metaclass=abc.ABCMeta):
    def __init__(self,age=1):
        self.age = age
    # def drive(self):
    #     if self.age >= 18:
    #         print('ok')
    #     else:
    #         raise Exception('No drive')
    @abc.abstractmethod
    def drive(self):
        pass

# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#     def drive(self):
#         raise Exception('No drive')

# class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        raise Exception('No drive')

# baby = Baby()
# adult = Adult()

# class Car(object):
#     def __init__(self,model=None):
#         self.model = model
#     def run(self):
#         print('run')
#     def ride(self,person):
#         person.drive()

# car = Car()
# car.ride(adult)

# class ToyotaCar(Car):
#     def run(self):
#         print('fast')

# class TeslaCar(Car):
#     def __init__(self,
#                  model='Model S',
#                  enable_auto_run=False,
#                  passwd='123'):
#         super().__init__(model)
#         self._enable_auto_run = enable_auto_run
#         # self.__enable_auto_run = enable_auto_run
#         self.passwd= passwd

#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run

#     @enable_auto_run.setter
#     def enable_auto_run(self,is_enable):
#         if self.passwd == '456':
#             self._enable_auto_run=is_enable
#         else:
#             raise ValueError

#     def run(self):
#         # print(self.__enable_auto_run)
#         print('super fast')

#     def auto_run(self):
#         print('Auto run')

# car = Car()
# car.run()
# print('#########')
# toyotacar = ToyotaCar('Lexus')
# print(toyotacar.model)
# toyotacar.run()
# print('#########')
# tesla_car = TeslaCar('Models')
# print(tesla_car.model)
# tesla_car.auto_run()
# tesla_car.run()

# tesla_car = TeslaCar('Model X',passwd='456')
# tesla_car.enable_auto_run=True
# tesla_car.run()
# print(tesla_car.enable_auto_run)


# class T(object):
#     pass

# t=T()
# t.name = 'Mike'
# t.age = 20
# print(t.name,t.age)

# class Person(object):
#     def talk(self):
#         print('talk')

# class Car(object):
#     def run(self):
#         print('run')

# class PersonCarRobot(Person,Car):
#     def fly(self):
#         print('fly')

# person_car_robot = PersonCarRobot()
# person_car_robot.fly()
# person_car_robot.run()
# person_car_robot.talk()

# class Person(object):
#     kind = 'human'

#     def __init__(self,name):
#         # self.kind = 'human'
#         self.name = name

#     def who_are_you(self):
#         print(self.name,self.kind)

# Person('A').who_are_you()
# Person('B').who_are_you()

# class T(object):
#     def __init__(self):
#         self.words = []

#     def add_word(self,word):
#         self.words.append(word)

# c = T()
# c.add_word('add 1')
# print(T().words)

# class Person(object):
#     kind = 'human'

#     def __init__(self):
#         self.x = 100

#     @classmethod
#     def what_is_your_kind(cls):
#         return cls.kind

#     @staticmethod
#     def about(year):
#         print('about human {}'.format(year))

# a = Person()
# b = Person
# print(a.what_is_your_kind())
# print(b.what_is_your_kind())
# Person.about(1999)

class Word(object):

    def __init__(self,text):
        self.text = text

    def __str__(self):
        return 'word!!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self,word):
        return self.text.lower() + word.text.lower()

    def __eq__(self,word):
        return self.text.lower() == word.text.lower()


w = Word('test')
w2 = Word('#########')
print(w)
print(len(w))
print(w+w2)
print(w==w2)
# o = Word(2)
# print(o)
