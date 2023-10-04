from lesson_package.tools import utils
# from ..tools import utils
def humanTalk(keyWord:str):
    if keyWord == 'singer':
        return 'sing'
    else:
        return 'cry'

def humanSayTwice():
    return utils.say_twice('cry')
