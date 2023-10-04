from lesson_package.tools import utils
# from ..tools import utils
def animalTalk(keyWord:str):
    if keyWord == 'animalSinger':
        return 'animalSing'
    else:
        return 'animalCry'

def animalSayTwice():
    return utils.say_twice('animalCry')


if __name__ == '__main__':
    print(animalTalk('animalSinger'))
    print('animal:',__name__)
