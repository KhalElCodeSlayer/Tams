import sys
import os
from Imp import Imp
from aircraft import Aircraft

def validateint(var):
    try:
        return int(var)
    except:
        print("Invalid option!")
        return False

class BackupUI:
    def __init__(self,path):
        self.airplane = Imp(path).get_Aircraft()
        print(self.airplane.get_dict())

    def display(self):
        invalid = True
        print("~~~~Welcome to the Aircraft Maintenance System~~~~")
        print("PLease choose what you would like to do")
        print("(1) Display parts")
        print("(2) Display status report")
        print("(3) Display Expense")
        print("(4) Upload data")
        print("(5) Update Data")
        print("(6) Add Documentation ")
        print("(7) Alerts")
        print("(8) Exit")
        while invalid:
            cho = input()
            if validateint(cho):
                if 0 < int(cho) < 9:
                    invalid = False
                    cho = int(cho)
            else:
                print("Invalid input entered!")
        invalid = True
        if cho == 1:
            self.displayparts()


        elif cho == 7:
            while invalid:
                time = input("Please input the maximum time remaining to be shown in the alerts:")
                if validateint(time):
                    if 0 < int(time):
                        invalid = False
                        time = int(time)
                else:
                    print("Invalid input entered!")
            self.display_alerts(time)



    def displayreport(self,id):
        pass

    def displayparts(self):
        compdict = self.airplane.get_info("Componentso")
        print("The following info displayed is a summarized version of the parts information, including only the name, serial number, remaining life and maintenance cost:")
        for i in list(compdict.keys()):
            print(f"Name:{i}, Serial No.:{compdict[i].get_info('S_No')}, Remaining life:{compdict[i].get_info('L_Rem')}, Maintenance Cost:{compdict[i].get_info('M_Cost')}\n")


    def display_alerts(self,time):
        compdict = self.airplane.get_info("Componentso")
        compl = [compdict[i].toString() for i in compdict if compdict[i].toString()['L_Rem'] != "NA" and compdict[i].toString()['L_Rem'] < time ]
        compl = sorted(compl, key=lambda k: int(k['L_Rem']))
        print(f"Now printing an alert list for parts with a remaining life under {time}, sorted in ascended order:")
        for x in compl:
            print(f"Name:{x['Item']}, Serial No.:{x['S_No']}, Remaining life:{x['L_Rem']}")




if __name__ == "__main__":
    path = os.path.dirname(__file__)
    rel_path = "Data.xlsx"
    path = os.path.join(path,rel_path)
    print(path)
    ui = BackupUI(path)
    ui.display_alerts(2000)
