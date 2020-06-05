import argparse

class cmdInterface(object):
    def __init__(self):
        super(cmdInterface, self).__init__()
        self.__parse = argparse.ArgumentParser()
        self.__arguements()
        self.__seconds = None

    def __arguements(self):
        self.__parse.add_argument('-s')

    def getArgs(self):
        return self.__parse.parse_args()