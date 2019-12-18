"""This file contains the gear class that calculates gear metrics."""

class cgear:
    def __init__(self,pd_dia, num, tag):
        self.pd_dia = pd_dia
        if tag == "t":
            self.num_teeth = num
            self.mod = 0.0
        if tag == "m":
            self.mod = num
            self.num_teeth = self.pd_dia/self.mod
        
        self.lst1 = []
        # self.mod = 0.0 # Modulas
        self.od = 0.0  # Outside diameter
        self.rd = 0.0  # Root diameter
        self.ta = 0.0  # Tooth angle
        self.cp = 0.0  # Circular pitch
        self.td = 0.0  # Tooth depth
        self.pitch = 0.0 # Tooth pitch
        self.th = 0.0  # Tooth thickness

    def module(self):
        self.mod  = self.pd_dia/self.num_teeth
        self.lst1.append(self.mod)
        self.od = self.mod*(self.num_teeth + 2)
        self.lst1.append(self.od)
        self.rd = self.mod*(self.num_teeth -2.5)
        self.lst1.append(self.rd)
        self.ta = 360/self.num_teeth
        self.lst1.append(self.ta)
        self.cp = 3.1415 * self.mod
        self.lst1.append(self.cp)
        self.td = 2.25 * self.mod
        self.lst1.append(self.td)
        self.pitch = self.num_teeth/self.pd_dia
        self.lst1.append(self.pitch)
        #self.th = 1.5708* self.cp
        self.th = self.cp/2
        self.lst1.append(self.th)
        self.lst1.append(self.num_teeth)
        self.lst1.append(self.pd_dia)

    def ret_data(self):
        self.module()
        return self.lst1

