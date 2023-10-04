# import math
import sys
import builtins
# import lesson_package.utils
# from lesson_package.tools import utils
# from lesson_package.utils import say_twice
# from lesson_package.talk import human
# from lesson_package.talk import animal
# from lesson_package.talk import *
# from collections import defaultdict
# from termcolor import colored
import config
import lesson_package.talk.animal



# print(sys.argv)
# print(sys.stdin.name)
# for i in sys.argv:
#     print(i)
# r = lesson_package.utils.say_twice("hello")
# r = utils.say_twice("hello")
# r = say_twice("hello")
# h = human.humanTalk('singer')
# print(r)
# print(human.humanTalk('singer'))
# print(human.humanSayTwice())
# print(animal.animalTalk('animalSinger'))
# print(animal.animalSayTwice())
# utils.say_twice("hello")
# print(globals())

# builtins.print()

# ranking = {'A':100,'B':92,'C':95}
# # for key in ranking:
# #     print(key)
# print(sorted(ranking,key=ranking.get,reverse=True))

# s="fdjsafigjhjfdssdfklhdskj"
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 0
#     d[i]+=1
# print(d)

# f = {}
# for i in s:
#     f.setdefault(i,0)
#     f[i]+=1
# print(f)

# h = defaultdict(int)

# for i in s:
#     h[i] +=1
# print(h)
# print(h['f'])

# print(colored('test','red'))

def main():
  lesson_package.talk.animal.animalTalk('aaaa')
# print('lesson:',__name__)

if __name__ == '__main__':
  main()
