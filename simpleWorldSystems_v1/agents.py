__author__ = 'usuallycwdillon@github.io'

from abc import ABCMeta


class Agent(object):
    """

    """
    __metaclass__ = ABCMeta

    def __init__(self, type):
        self.type = ''
        self.has_suzern = []
        self.has_tribute = []
        self.has_territory = []
        

    def deliberatesWith(self, other, temp):
        self.links[other] = temp
        other.links[self] = temp

    def warWith(self, other):
        pass

    def treatWith(self, other):
        pass




    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType


class Kingdom(Agent):
    """
    :param type
    """
    def __init__(self, type):
        self.type = 'Kingdom'


class Empire(Agent):
    """
    :param type
    """
    def __init__(self, type):
        self.type = 'Empire'

class War(object, belig, opp):
    beligerant = beligerant
    opponent = opp

    def consume():
