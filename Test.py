import os
from datetime import date
import openpyxl as op

from Exporter import Exporter
from Imp import Imp
from aircraft.Aircraft import Aircraft
import time
from FileMng import FileMng



if __name__ == "__main__":
    rel_path = r"aircraft/N25604_Aircraft_component_list.xlsx"
    In = Imp(rel_path)
    plane = In.get_Aircraft()
    FileMng(plane,2021)
    print(plane.get_smcrec("JAN"," Battery Pointer ELT"))
    Exporter(plane)