import os
from datetime import date
import openpyxl as op
from aircraft.Aircraft import Aircraft
import time


class FileMng:

    def __init__(self,aircraft: Aircraft,year):
        start = time.time()
        self.__months = ["JAN", "FEB", "MAR", "APRIL", "MAY", "JUNE", "JULY", "AUG", "SEPT", "OCT", "NOV", "DEC"]
        try:
            for i in self.__months:
                os.makedirs(f"Airplane/Operations/{year}/{i}")
                os.makedirs(f"Airplane/Components/{year}/{i}")

            print("pp")
            self.init_components(aircraft.get_info("Componentso"), year)
            print("ll")
            self.init_operations(aircraft.get_info("Operations"), year)
        except:
            pass
        print(time.time()-start)


    def init_components(self, compdict: dict, year):
        for i in self.__months:

            for k in compdict.keys():
                file = open(f"Airplane/Components/{year}/{i}/{k}.txt", "w+")
                file.close()


    def init_operations(self, opdict: dict, year):
        for i in self.__months:
            for k in opdict.keys():
                file = open(f"Airplane/Operations/{year}/{i}/{k}.txt", "w+")
                file.close()


