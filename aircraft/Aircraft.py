import Imp


class Aircraft:
    def __init__(self, airdict, compdict, compodict, opdict):
        self._summ = airdict
        self._tach = self._summ["Tach"]
        self._summ["F_Time"] = 6405.4
        self._F_time = self._summ["F_Time"]
        self._components = compdict
        self._operations = opdict
        self._componentso = compodict
        self.update()

    def update(self):
        self._mcost = self._summ["M_Cost"]
        self._make = self._summ["Aircraft Make"]
        self._model = self._summ["Model"]
        self._serial_no = self._summ["Serial #"]
        self._registration_no = self._summ["Registration #"]
        self._dop = self._summ["Date made"]
        self._hobbs = self._summ["Hobbs adjust"]
        self._due_insp = self._summ["NEXT INSP DUE"]
        self._Rem_T = self._summ["Time Remaining To Next Insp."]
        if self._tach != self._summ["Tach"]:
            self._tach = self._summ["Tach"]
            for i in self._operations:
                self._operations[i].update_info("C_Tach", self._tach)
        elif self._F_time != self._summ["F_Time"]:
            self._F_time = self._summ["F_Time"]
            for i in self._componentso:
                self._componentso[i].update_info("Curr_time", self._F_time)

    def get_info(self, var):
        if var == "Components":
            return self._components
        elif var == "Operations":
            return self._operations
        elif var == "Componentso":
            return self._componentso
        elif var in list(self._summ.keys()):
            return self._summ[var]
        return None

    def get_dict(self):
        return self._summ

    def update_air_info(self, id, info):
        if id in self._summ:
            self._summ[id] = info
            self.update()

    def update_comp_info(self, compid, id, info):
        if compid in list(self._components.keys()):
            self._components[compid].update_info(id, info)
            return True
        else:
            return False
        pass

    def update_compo_info(self, compoid, id, info):
        if compoid in list(self._componentso.keys()):
            self._componentso[compoid].update_info(id, info)
            return True
        else:
            return False
        pass

    def update_operation_info(self, opid, id, info):
        if opid in list(self._operations.keys()):
            self._operations[opid].update_info(id, info)
            return True
        else:
            return False

    def add_component(self, component):
        if component.get_info("Item") not in list(self._componentso.keys()):
            self._componentso[component.get_info("Item")] = component
        else:
            print(f"Are you sure you would like to override the information for {component.get_info('Item')}?")


    def init_mrec(self,crec,orec):
        self.crec = crec
        self.orec = orec

    def get_mmcrec(self, month):
        return self.crec[month]

    def get_smcrec(self, month,component):
        return self.get_mmcrec(month)[component]

    def add_mcrec(self,year,month,component,info):
        #info variable is a list of strings
        #make this reset the counter in the excel file too please
        if component in self.crec[month].keys():
            print(self.crec[month].keys())
            self.crec[month][component].update({info[0]:{"ID":info[1],"Cost":info[2],"Comments":info[3]}})
            print(self.crec[month][component])

    def add_ocrec(self,year,month,operation,info):
        #info variable is a list of strings
        #make this reset the counter in the excel file too please
        if operation in self.orec[month].keys():
            print(self.orec[month].keys())
            self.orec[month][operation].update({info[0]:{"ID":info[1],"Cost":info[2],"Comments":info[3]}})
            print(self.orec[month][operation])




    def add_operation(self, operation):
        if operation.get_info("Inspection") not in list(self._operations.keys()):
            self._operations[operation.get_info("Inspection")] = operation
        else:
            print(f"Are you sure you would like to override the information for {operation.get_info('Inspection')}?")

    def pto_String(self):
        print("Aircraft information:\n")
        for i in self._summ:
            print(F"{i}: {self._summ[i]}")
        print(f"\n\nAircraft Components:")
        for i in self._componentso:
            print(F"{i}: {self._componentso[i].toString()}\n")
        print(f"\n\nAircraft Operations:")
        for i in self._operations:
            print(F"{i}: {self._operations[i].toString()}\n")

    def mainten_num(self):
            mnum=0
            for co in self._componentso.values():
                if int( 0 if co.get_info("Next_inspH") is None else co.get_info("Next_inspH") )<=100:
                    mnum+=1
            print("\n Maintenance Number of Aircraft "+self.get_info("Registration #") +": "+str(mnum))
            return  mnum

    def mainten_list(self):
        i=1
        colist=list(self._componentso.values())
        mlist=list(map(lambda a:a.get_info("Item"),sorted(colist,key=lambda x: x.get_info("Next_inspH"))))
        print("\nThis a list of components by descending maintenance priority for Aircraft "+self.get_info("Registration #") +".\n")
        for m in mlist:
            print(" "+str(i)+". "+m)
            i+=1

    def calc_air_mainten(self,fhours):
        for co in self._componentso.values():
            inf=int( 0 if co.get_info("Next_inspH") is None else co.get_info("Next_inspH"))-fhours
            co.update_info("Next_inspH", inf)