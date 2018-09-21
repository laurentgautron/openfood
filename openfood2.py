

from tables import Tables
from datas import Datas
import os

class Main:

    def __init__(self):

        self.empty = os.path.isfile('openfoodbase.json')
        self.datas = Datas()
        
    def openfood(self):

        if not self.empty:
            os.system('clear')
            Tables.remove()
            self.datas.mkjsonfile()
        Tables.creation()
        Tables.bonjour()
        Tables.fill_tables()



if __name__ == '__main__':
    main = Main()
    main.openfood()