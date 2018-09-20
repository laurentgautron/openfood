

from tables import Tables
from datas import Datas
import os

class Main:

    def __init__(self):

        self.empty = os.path.isfile('openfoodbase.json')
        self.datas = Datas()
        self.tables = Tables()

    def openfood(self):

        if not self.empty:
            os.system('clear')
            Tables.remove()
            lisTable = self.tables.make_list_sql_create()
            Tables.creation(lisTable)
            self.datas.mkjsonfile()


if __name__ == '__main__':
    main = Main()
    main.openfood()