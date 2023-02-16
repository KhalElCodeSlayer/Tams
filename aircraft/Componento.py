class Componento:
    def __init__(self, compodict):
        self._summ = compodict
        self.update()

    def update(self):
        self._id = self._summ["Item"]
        self._P_No = self._summ["P_No"]
        self._S_No = self._summ["S_No"]
        self._Date = self._summ["Date"]
        self._RY = self._summ["RY"]
        self._RH = self._summ["RH"]
        self._Tot_I = self._summ["Tot_I"]
        self._Past_T = self._summ["Past_T"]
        self._Curr_time = self._summ["Curr_time"]
        self._AF_Hours = self._summ["AF_Hours"]
        self._L_Rem = self._summ["L_Rem"]
        self._Date_rep = self._summ["Date_rep"]
        self._Next_inspH = self._summ["Next_inspH"]
        self._Next_insp = self._summ["Next_insp"]
        self._Type_mjr = self._summ["Type_mjr"]
        self._Remarks = self._summ["Remarks"]
        self._maint_cost = self._summ["M_Cost"]

    def get_info(self, var):
        return self._summ[var]

    def update_info(self, id, info):
        if id in list(self._summ.keys()):
            self._summ[id] = info
            if id == "Curr_time" and type(self._summ["L_Rem"]) != type(" "):

                self._summ["L_Rem"] = self._summ["AF_Hours"] - self._summ["Curr_time"]
            self.update()

    def toString(self):
        return self._summ
