import os
import sys
import Imp
from Exporter import Exporter
from aircraft.Componento import Componento
from aircraft.Operation import Operation


def validateint(var):
    try:
        p = int(var)
        return type(1) == type(p)
    except:
        print("Invalid option!")
        return False


compov = {"Item": None, "P_No": None, "S_No": None, "Date": None, "RY": None, "RH": None, "Tot_I": None,
                "Past_T": None, "Curr_time": None, "AF_Hours": None, "L_Rem": None, "Date_rep": None,
                "Next_inspH": None, "Next_insp": None, "Type_mjr": None, "Time_mjr": None,"Remarks": None,"M_Cost":None}

opv = {"Inspection": None, "Frequency": None, "Hours": None, "Months": None, "HCW": None, "DCW": None,
            "C_Tach": None, "NDH": None, "NDD": None, "Note": None, "T_rem": None}
class Textui:
    def __init__(self, path):
        self.plane = Imp.Imp(path).get_Aircraft()
        self.DisplayMenu()

    def DisplayMenu(self):
        invalid = True
        print("\n~~~~Welcome to the Aircraft Maintenance System~~~~\n")
        print("Please choose what you would like to do\n")
        print("(1) Display Parts")
        print("(2) Display Status Report")
        print("(3) Display Expense")
        print("(4) Upload Data")
        print("(5) Update Data")
        print("(6) Update Operation info")
        print("(7) Add Component")
        print("(8) Add Operation")
        print("(9) Add Documentation ")
        print("(10) Alerts")
        print("(11) Maintenance List")
        print("(12) Get Documentation")
        print("(13) Input Flight")
        print("(14) Exit")
        while invalid:
            cho = input()
            if validateint(cho):
                if 0 < int(cho) < 15 :
                    invalid = False
                    cho = int(cho)
            else:
                print("Invalid input entered!")
        invalid = True
        if cho == 1:
            self.Display_parts()
            self.menuop()
        elif cho == 2:
            self.Display_status_report()
            self.menuop()
        elif cho == 3:
            self.Display_Expense()
            self.menuop()
        elif cho == 4:
            pthl = input("\nPlease enter the path of the file to be uploaded: ")
            self.Upload_data(pthl)
            self.menuop()
        elif cho == 5:
            self.Update_data()
            self.menuop()
        elif cho == 6:
            self.Update_Op_info()
            self.menuop()
        elif cho == 7:
            self.Add_Component()
            self.menuop()
        elif cho == 8:
            self.Add_Op()
            self.menuop()
        elif cho == 9:
            comp = input("\nPlease enter the serviced components' ID: ")
            docu = input("\nPlease enter the Documentation: ")
            self.Add_Documentation(comp, docu)
            self.menuop()
        elif cho == 10:
            time=input("\nPlease enter the maximum time until next inspection for the components: ")
            self.display_alerts(int(time))
            self.menuop()
        elif cho == 11:
            self.display_maintainList()
            self.menuop()
        elif cho == 12:
            fl= input("\nPlease enter the component ID: ")
            self.Get_doc(fl)
            self.menuop()
        elif cho == 13:
            ftime= input("\nPlease enter the flight time in hours ")
            self.calc_maintainTime(int(ftime))
            self.menuop()
        elif cho == 14:
            self.export("Data.xlsx")


    def menuop(self):
        print("\nWould you like to do go back to the menu?")
        invalid = True
        while invalid:
            hk = int(input("1 for yes, 0 to exit: "))
            if validateint(hk):
                if -1 < int(hk) <= 1:
                    invalid = False
                    hk = int(hk)
            else:
                print("Invalid input entered!")
        if hk == 1:
            self.DisplayMenu()
        elif hk == 0:
            self.export("Data.xlsx")
    
    def display_maintainList(self):
        self.plane.mainten_list()
        self.plane.mainten_num()

    def calc_maintainTime(self,ftime):
        self.plane.calc_air_mainten(ftime)

    def Display_parts(self):
        compdict = self.plane.get_info("Componentso")
        print(
            "The following info displayed is a summarized version of the parts information, including only the name, serial number,time to next inspection, remaining life and maintenance cost:")
        for i in list(compdict.keys()):
            print(f"Name:{i}, Serial No.:{compdict[i].get_info('S_No')}, Time to next inspection:{compdict[i].get_info('Next_inspH')}, Remaining life:{compdict[i].get_info('L_Rem')}, Maintenance Cost:{compdict[i].get_info('M_Cost')}\n")

    def Upload_data(self, pathl):
            Imp.Imp(pathl)

    def Update_data(self):
        print("~~~~Update Data~~~~")
        print("The list below contains a list of components that can be updated\n")
        print(list(self.plane.get_info("Componentso").keys()))
        comps = input("\nPlease enter the desired component: ")
        print("\nThe list below contains a list of elements that can be updated")
        print("Item,P_No,S_No,Date,RY,RH,Tot_I,Past_T,Curr_time,AF_Hours,L_Rem,Date_rep,Next_inspH,Next_insp,Type_mjr")
        choi = input("Please enter the desired element: ")
        info = input("Please enter the updated information: ")
        self.plane.update_compo_info(comps, choi, info)

    def Update_Op_info(self):
        print("~~~~Operation Update~~~~")
        print("The list below contains a list of operations that can be updated")
        print(list(self.plane.get_info("Operations").keys()))
        op = input("Please enter the desired operation: ")
        print("\nThe list below contains a list of elements that can be updated")
        print("Inspection,Frequency,Hours,Months,HCW,DCW,C_Tach,NDH,NDD,T_rem,Note")
        choip = input("Please enter the desired element: ")
        infop = input("Please enter the updated information: ")
        self.plane.update_operation_info(op, choip, infop)

    def Add_Component(self):
        self.new = Componento(compov.copy())
        co = input("Please enter the component that you wish to add: ")
        self.new.update_info("Item", co)
        self.plane.add_component(self.new)

    def Add_Op(self):
        self.newop = Operation(opv.copy())
        aop = input("Please enter the operation that you wish to add: ")
        self.newop.update_info("Inspection", aop)
        self.plane.add_operation(self.newop)

    def Add_Documentation(self, comp, doc):
        self.plane.update_compo_info(comp, "Remarks", doc)

    def display_alerts(self,time):
        compdict = self.plane.get_info("Componentso")
        compl = [compdict[i].toString() for i in compdict if compdict[i].toString()['Next_inspH'] != "NA" and compdict[i].toString()['Next_inspH'] <=time ]
        compl = sorted(compl, key=lambda k: int(k['Next_inspH']))
        print(f"\nNow printing an alert list for parts with a time until Next Inspection under {time}, sorted in ascended order:")
        for x in compl:
            print(f"Name:{x['Item']}, Serial No.:{x['S_No']}, Time until Next Inspection:{x['Next_inspH']}")

    def export(self,path):
        self.exporte = Exporter(path, self.plane)
        sys.exit()

    def Get_doc(self,id):
        print(self.plane.get_info("Componentso")[id].get_info("Remarks"))

    def Display_Expense(self):
        pass

    def Display_status_report(self):
        pass

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    rel_path = r"Data.xlsx"
    path = os.path.join(path,rel_path)
    ui = Textui(path)
    ui.display_alerts(2000)
