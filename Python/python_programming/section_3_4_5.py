import math
# print("test")

# a="test"
# b=a
# c=b
# print(c)
# num:int = 1
# name:str = 'Mike'
# int_name='1'
# new_num=int(int_name)

# print(num,type(num))
# print(name,type(name))
# print(new_num,type(new_num))


# print('Hi','Mike',sep=',',end=" \n")
# print('Hi','Mike',sep=',',end='¥n')

# print(5**2)

# result = math.sqrt(25)
# print(result)

# y= math.log(9)
# print(y)

# print(help(math))

# print('hello')
# print("hello")
# print('say "I dont \'t know"')
# print(r'C:\name\name')

# word = 'python'
# print(word[0])
# print(word[-1])
# print(word[0:2])
# print(len(word))

# s= 'My name is Mike, Hi Mike'
# print(s)
# print(s.startswith('My'))
# print(s.find('Mike'))
# print(s.rfind('Mike'))
# print(s.count('Mike'))
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.replace('Mike','Nancy'))

# numberList = [1,2,3,4,5,6,7]
# print(numberList)
# print(numberList[-4])
# print(numberList[4])
# print(numberList[:4])
# print(len(numberList))

# textList = ['a','b','c','d']
# print(textList)
# textList[0]= 'd'
# print(textList)

# numberListKai = [1,2,3,4,5,6,7]
# print(numberListKai.index(7,6))
# if 100 in numberListKai:
#     print('exist')

# x= [1,2,3,4,5,6,7,8,9,10]
# y= x
# x[0]=100
# print(x)
# print(y)

# x= [1,2,3,4,5,6,7,8,9,10]
# y= x.copy()
# x[0]=100
# print(x)
# print(y)

# seat =[]
# min = 0
# max = 5

# seat.append('p')
# if min <= len(seat) < max:
#     print(True)

# t= (1,2,3,4,5,6,7,8,9,10)
# print(type(t))

# num_tuple=(10,20)
# print(num_tuple)
# x,y=num_tuple
# print(x,y)

# i=10
# j=20
# tmp=i
# i=j
# j=tmp
# print(i,j)
# a=100
# b=200
# a,b=b,a
# print(a,b)

# d= {'x':10,'y':20}
# print(type(d))
# d['x']=100
# d['z']='ggg'
# print(d)
# print(d['x'])
# print(d.keys())
# print(d.values())
# d2={'x':1000,'j':2000}
# print(d2)
# d.update(d2)
# print(d)
# print(d.get('x'))
# x={'a':1}
# y=x.copy()
# y['a']=1000
# print(x)
# print(y)

# a={1,1,2,4,5,7,3}
# print(type(a),a)
# b={1,4,5,7,8,9,2}
# print(a-b)
# s={1,2,3,4,5}
# s.add(6)
# print(s)
# s.remove(6)
# print(s)
# s.clear()
# print(s)

# x=0
# if x<0:
#     print('negative')
# elif x==0:
#     print(x)
# else:
#     print('positive')
# print('end')
# y=[1,2,3]
# x=1
# if x in y:
#     print(x,'in',y)
# if 100 not in y:
#     print(x,' not in',y)
# is_ok = 0
# if is_ok:
#     print('ok')
# else:
#     print('No')
# is_Empty = None
# if is_Empty == None:
#     print('None')
# if is_Empty is None:
#     print('None')

# count = 0
# while count < 100:
#     # print(count)
#     # count+=1
#     if count > 10:
#         break
#     elif count ==5:
#         count+=2
#         continue
#     else:
#         print('else')
#     print(count)
#     count+=1
# while True:
#     word = input('Enter：')
#     if word == 'ok':
#         break
#     print('next')

# some_list = [1,2,3,4,5]
# for i in some_list:
#     print(i)
# for s in 'abcder':
#     print(s)
# for m in ['My','Name']:
#     if m == 'My':
#         print(m)
#         break
# else:
#     print('none')
# for i in range(2,10,3):
#     print(i)

# for i,fruit in enumerate(['apple','banana','orange']):
#     print(i,fruit)

# days =['mon','tue','wed']
# fruits = ['apple','banana','beer']
# for day, fruit in zip(days,fruits):
#     print(day,fruit)

# d = {'x':100,'y':200}
# for k,v in d.items():
#     print(k,':',v)

# def say_something():
#     s='jack'
#     print('hi')
#     return s

# r = say_something()
# print(r)

# def what_color(color):
#     print(color)

# def menu(e='beef',d='wine', c='ice'):
#     print(e,d,c)
# menu('chicken','bbb','yyy')

# def test_func(x,l=None):
#     if l is None:
#         l=[]
#     l.append(x)
#     return l

# r = test_func(100,[50,60])
# print(r)

# r = test_func(200)
# print(r)

# def say_something(word,*args):
#     print('word =',word)
#     for arg in args:
#         print(arg)
# t=('Mike','Nance','Jack')
# say_something('Hi',*t)

# def menu(food,*args,**kwargs):
#     print(food)
#     print(args)
#     for k,v in kwargs.items():
#         print(k,v)
# d = {
#     'entree':'beef',
#     'drink':'coffee'
# }
# t=('Mike','Nance','Jack')
# menu('aaaa',*t,**d)

# def outer(a,b):
#     def plus(c,d):
#         return c+d
#     r1=plus(a,b)
#     r2=plus(b,a)
#     print(r1,r2)
#     print(r1+r2)
# outer(1,2)

# def circle_area_func(pi):
#     def circle_area(radius):
#         return pi * radius * radius
#     return circle_area

# cal1 = circle_area_func(3.14)
# cal2 = circle_area_func(3.1456778)
# # print(circle_area_func(3.15))
# print(cal1(10))
# print(cal1(20))

# def print_more(func):
#     def wrapper(*args,**kwargs):
#         print('func',func.__name__)
#         print('args',args)
#         print('kwargs',kwargs)
#         result = func(*args,**kwargs)
#         print('result',result)
#         return result
#     return wrapper

# def print_info(func):
#     def wrapper(*args,**kwargs):
#         print('start')
#         result = func(*args,**kwargs)
#         print('end')
#         return result
#     return wrapper

# @print_info
# @print_more
# # @print_info
# def add_num(a,b):
#     return a+b

# r=add_num(10,20)
# print(r)

# l=['mon','tue','wed','thu','fri','sat','sun']

# def change_words(words,func):
#     for word in words:
#         print(func(word))

# def sample_func(word):
#     return word.capitalize()

# sample_func = lambda word: word.capitalize()

# change_words(l,lambda word: word.capitalize())

# l = ['Good morning','Good afternoon','Good night']

# for i in l:
#     print(i)

# print('#################')

# def counter(num=10):
#     for _ in range(num):
#         yield 'run'

# def greeting():
#     yield 'Good morning'
#     yield 'Good afternoon'
#     yield 'Good night'

# for g in greeting():
#     print(g)

# g = greeting()
# c=counter()
# print(next(g))
# print(next(c))
# print(next(c))
# print(next(g))

# t=(1,2,3,4,5)
# t2=(1,2,3,4,5)
# r=[i for i in t if i % 2 ==0]
# print(r)

# r2=[i*j for i in t for j in t2]
# print(r2)

# w = ['mon','tue','wed']
# f = ['coffee','milk','water']

# d={x:y for x,y in zip(w,f)}
# print(d)

# s = {i for i in range(10)}
# print(type(s))

# g = (i for i in range(10))
# print(type(g))
# print(next(g))
# print(next(g))

# animal = 'cat'

# def changeAnimalName():
#     # global animal
#     # animal = 'dog'
#     # print('local',animal)
#     print('local',locals())

# changeAnimalName()
# # print('global：',animal)
# print('global：',globals())

# l=[1,2,3]
# i=2

# try:
#     l[i]
# except IndexError as e:
#     print("Don't worry : {}".format(e))
# else:
#     print("done")
# finally:
#     print("clean up")
# print("last")

class UppercaseError(Exception):
    pass

def check():
    words = ['apple','orange','banana','PINEAPPLE']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
try:
    check()
except UppercaseError as e:
    print('Exception : {}'.format(e))
else:
    print('Done')
finally:
    print('Exit')
