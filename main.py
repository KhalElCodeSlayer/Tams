import aircraft
import Imp
import os

if __name__ == "__main__":
    Pt=os.path.join(os.getcwd(),"aircraft/N25604_Aircraft_component_list.xlsx")
    plane = Imp.Imp(Pt).get_Aircraft()
    plane.mainten_list()
    plane.mainten_num()