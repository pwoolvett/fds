from colorama import init
from colorama import Fore

class PrettyPrint(object):

    def __init__(self):
        init()

    def warn(self, text: str):
        print(Fore.YELLOW + text)

    def log(self, text: str):
        print(Fore.reset + text)

    def error(self, text: str):
        print(Fore.RED + text)

    def success(self, text: str):
        print(Fore.GREEN + text)
