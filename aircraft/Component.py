class Component:
    def __init__(self, compdict):
        self._summ = compdict
        self._summ["M_Cost"] = None
        self.update()

    def update(self):
        self._id = self._summ["Item"]
        self._P_No = self._summ["P_No"]
        self._S_No = self._summ["S_No"]
        self._Date = self._summ["Date"]
        self._RY = self._summ["RY"]
        self._RM = self._summ["RM"]
        self._RH = self._summ["RH"]
        self._RO = self._summ["RO"]
        self._Tot_I = self._summ["Tot_I"]
        self._Past_T = self._summ["Past_T"]
        self._Comp_Cycle = self._summ["Comp_cycle"]
        self._Date_CW = self._summ["Date_CW"]
        self._T_Remove = self._summ["T_Remove"]
        self._Sched_Remove = self._summ["Sched_Remove"]
        self._T_RemH = self._summ["T_RemH"]
        self._T_remD = self._summ["T_remD"]
        self._maint_cost = self._summ["M_Cost"]

    def get_info(self, var):
        return self._summ[var]

    def update_info(self, id, info):
        if id in list(self._summ.keys()):
            self._summ[id] = info
            self.update()

    def toString(self):
        return self._summ
