import numpy as np
import matplotlib.pyplot as plt
import plotting as ris



class Part:
    def __init__(self, pozicija, masa, C_upora, mvm, ime='') -> None:
        self.pozicija = np.array(pozicija, dtype='float64')
        self.ime = ime
        self.masa = masa
        self.C_upora = C_upora
        self.mvm = mvm


class Kvader(Part):
    def __init__(self, pozicija, masa, mvm, a, b, c, C_upora=1, ime='') -> None:
        super().__init__(pozicija, masa, C_upora, mvm, ime)
        self.a = a
        self.b = b
        self.c = c
        # self.mvm = self.izracunaj_mvm()
        self.mvm = mvm 

    def izracunaj_mvm(self):
        pass


class Valj(Part):
    def __init__(self, pozicija, masa, mvm, r, h, os='x', C_upora=0.6, ime='') -> None:
        super().__init__(pozicija, masa, C_upora, mvm, ime)
        self.r = r
        self.h = h
        self.os = os
        # self.mvm = self.izracunaj_mvm()
        self.mvm = mvm

    def izracunaj_mvm(self):
        pass


class Krogla(Part):
    def __init__(self, pozicija, masa, mvm, r, C_upora=0.4, ime='') -> None:
        super().__init__(pozicija, masa, C_upora, mvm, ime)
        self.r = r
        # self.mvm = self.izracunaj_mvm()
        self.mvm = mvm


    def izracunaj_mvm(self):
        pass


class Tocka(Part):
    def __init__(self, pozicija, masa, mvm=0, C_upora=1, ime='') -> None:
        super().__init__(pozicija, masa, C_upora, mvm, ime)
        # self.mvm = self.izracunaj_mvm() todo (na podlagi ploskovne gostote)
        self.mvm = mvm
    
    # todo
    def izracunaj_mvm(self): 
        pass











class Fuselage():
    parts = {}
    masa = None
    mvm = None
    tezisce = None
    names = {'nos', 'levo krilo', 'desno krilo', 'glavni del', 'rep'}
    def __init__(self, *args, nos=None, levo_krilo=None, desno_krilo=None, rep=None, glavni_del=None) -> None:
        self.nos = nos
        self.levo_krilo = levo_krilo
        self.desno_krilo = desno_krilo
        self.glavni_del = glavni_del
        self.rep = rep

        Fuselage.parts['nos'] = self.nos
        Fuselage.parts['levo krilo'] = self.levo_krilo
        Fuselage.parts['desno krilo'] = self.desno_krilo
        Fuselage.parts['glavni_del'] = self.glavni_del
        Fuselage.parts['rep'] = self.rep
        for i, part in enumerate(args):
            Fuselage.parts[f'part_{i}'] = part

        
        Fuselage.masa = sum([part.masa for part in Fuselage.parts.values() if part != None])
        Fuselage.tezisce = Fuselage.update_tezisce()
        Fuselage.mvm = Fuselage.update_mvm_cel()
        print([part.masa for part in Fuselage.parts.values() if part != None])

    
    @classmethod
    def update_tezisce(cls): 
        """ Izračuna težišče letala. """
        r_tezisca = np.array([0, 0, 0], dtype='float64')
        for part in cls.parts.values():
            if part == None: continue
            r_tezisca += part.masa * part.pozicija
        cls.tezisce_poz = r_tezisca / cls.masa


    @classmethod
    def update_mvm_cel(cls):
        """ Izračuna masni vztrajnostni moment letala glede na težišče letala. """
        I_xx, I_yy, I_zz = 0, 0, 0
        for part in cls.parts.values():
            if part == None: continue
            mvm_part = part.mvm
            I_xx += mvm_part["I_xx"]
            I_yy += mvm_part["I_yy"]
            I_zz += mvm_part["I_zz"]
        cls.mvm = {"I_xx": I_xx, "I_yy": I_yy, "I_zz": I_zz}


    @classmethod
    def get_parts(cls):
        return cls.parts


    @classmethod
    def plot_parts(cls, ax):
        """ Prikaže vse dele. """
        for part in cls.parts.values():
            if isinstance(part, Kvader):
                ris.plot_kvader(ax, part)
            elif isinstance(part, Valj):
                ris.plot_valj(ax, part)
            elif isinstance(part, Tocka):
                ris.plot_tocka(ax, part)


    @classmethod
    def sila_upora(cls):
        """ Izračuna silo upora za celotno letalo (čelni veter v smeri x osi). """
        v = 1
        rho = 1
        sila = 0
        for part_name in cls.parts:
            if part_name in {'nos', 'levo krilo', 'desno krilo', 'glavni del', 'rep'}:
                part = cls.parts[part_name]
                if part == None: continue
                sila += 1/2*part.C_upora*(part.b*part.c)*rho*v**2
        return sila

    









# Primer programa ------------------------------------------------------------------------------------------------------

kvader1 = Kvader(np.array([0, 0, 0]), 1, {"I_xx": 1, "I_yy": 2, "I_zz": 1}, 10, 3, 1.5, ime='glavni del')
valj1 = Valj(np.array([0, 0, 0]), 1, {"I_xx": 1, "I_yy": 2, "I_zz": 1}, 1, 3)
kvader2 = Kvader(np.array([1, 3.5, 0]), 1, {"I_xx": 1, "I_yy": 2, "I_zz": 1}, 2, 4, 1, ime='desno krilo')
kvader3 = Kvader(np.array([1, -3.5, 0]), 1, {"I_xx": 1, "I_yy": 2, "I_zz": 1}, 2, 4, 1, ime='levo krilo')
kvader4 = Kvader(np.array([-3.5, 0, 2]), 1, {"I_xx": 1, "I_yy": 2, "I_zz": 1}, 1.5, 0.5, 3, ime='rep')
potnik = Tocka(np.array([0, 0, 0]), 1, mvm={"I_xx": 1, "I_yy": 1, "I_zz": 1})



letalo = Fuselage(valj1, potnik, glavni_del=kvader1, desno_krilo=kvader2, levo_krilo=kvader3, rep=kvader4)
print("Sila upora:", Fuselage.sila_upora(), "N")




# Risanje -------------------------------------------------------------------------------------------------------------

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

Fuselage.plot_parts(ax)

x_min = y_min = z_min = -5
x_max = y_max = z_max = 5
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_zlim(z_min, z_max)
plt.savefig('aircraft_geometry.png')