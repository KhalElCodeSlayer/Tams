class Operation:
    def __init__(self,opdict):
        self._summ = opdict
        if self._summ["T_rem"]== None:
            self._summ["T_rem"] = self._summ["NDH"] - self._summ["C_Tach"]
        self.update()



    def update(self):
        self._id = self._summ["Inspection"]
        self._freq = self._summ["Frequency"]
        self._hours = self._summ["Hours"]
        self._months = self._summ["Months"]
        self._HCW = self._summ["HCW"]
        self._DCW = self._summ["DCW"]
        self._C_Tach = self._summ["C_Tach"]
        self._NDH = self._summ["NDH"]
        self._NDD = self._summ["NDD"]
        self._T_Rem = self._summ["T_rem"]
        self.note = self._summ["Note"]

    def get_info(self,var):
        return self._summ[var]


    def update_info(self,id,info):
        if id in list(self._summ.keys()):
            self._summ[id] = info
            if id == "C_Tach":
                self._summ["T_rem"] = self._summ["NDH"] - self._summ["C_Tach"]
            self.update()

    def toString(self):
        return self._summ
