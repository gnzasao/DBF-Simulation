import math
import numpy as np
import matplotlib.pyplot as plt
import time



"""
Za konkreten primer
....................
Premer trupa = 109mm
Dolžina trupa = 302mm
Dolžina repne palice = 862mm
Globina krila = 288mm
Span krila = 1732mm
Debelina Krila = 30mm
Span horizontal repa in višina vertical = 300mm
Globina repa = 150mm
Debelina repa = 30mm
.....................
#uporabljeno samo za konkretno preverjanje ali paše v škatlo:
krilo_x = 1.732/2
krilo_y = 0.288
palica_dolzina = 1.5
.........................
"""


# dimenzije je treba popraviti glede na spodnja dva komentarja
# trup: 6x3x3 inch
# rep: ustreza naslednjemu pogoju: (dolzina letala)/(sirina letala) = 12 (oz. 10-14)


# definicija vseh dimenzij in dimenzijskih intervalov
# vse v osnovnih enotah
vsota_dolzin = 1.5748
trup_x = 0.302
trup_y = 0.109
trup_z = 0.109
rep_x = 0.300
rep_y = 0.150
rep_z = 0.030
r_palice = (21.3 * 10**(-3))/2
x_min = 0.8
x_max = 1.6
ar_min = 4
ar_max = 10
S_min = 0.2
S_max = 1.2
min_dolzina = 0.6    # krila    
max_dolzina = 1.3
z_vs_y = 0.117
n = 30



""" 
def ali_ustreza_prostornina(dim_skatle):    #dim_skatle: (x, y, z)
    x, y, z = dim_skatle
    trup = create_trup_fix(trup_x, trup_y, trup_z)
    rep = create_rep_fix(rep_x, rep_y, rep_z)
    V_krila = krilo_x*krilo_y*0.030 * 4
    palica = create_palica(palica_dolzina)

    V_skupaj = trup['V'] + rep['V'] + V_krila['V'] + palica['V']

    return V_skupaj < x*y*z
 """






# naredi trup
def create_trup_fix(x, y, z):
    a = dict()
    a['x'] = x
    a['y'] = y
    a['z'] = z
    a['V'] = x*y*z
    return a


# naredi dva ista dela repa s skupno prostornino V
def create_rep_fix(x, y, z):    
    b = dict()
    b['x'] = x
    b['y'] = y
    b['z'] = z
    b['V'] = 2 * x*y*z      
    return b


# vsakemu izmed n x-ov priredi n S-ov (znotraj specifiranih intervalov) in za vsak tak par (x, S) naredi 4 krila s skupno prostornino V, skupaj torej n^2 kombinacij kril
# vrne list n^2-slovarjev, vsak slovar vsebuje dimenzije n kril (pri n razlicnih S in pri fiksnem x)
        	                   # i-ti slovar vsebuje 100 kril z dolzino x[i] in vsemi n povrsinami S 
def create_krila_S():
    kombinacije = []
    x = np.linspace(min_dolzina, max_dolzina, n)
    for i in range(n):
            S = np.linspace(S_min, S_max, n)
            y = S / x[i]
            z = z_vs_y * y
            ar = (2*x)**2 / S
            V = 4 * x[i]*y*z      # to so vsi mozni V-ji pri nekem (S, x) paru
            ar_vm = np.where(ar < 4, 11, ar)
            ar_ok = np.where(ar_vm > 10, 0, 1)
            V = V*ar_ok                 # v tem koraku izvršimo pogoj za ustrezen ar
            b = dict()
            b['x'] = x
            b['y'] = y
            b['z'] = z
            b['ar'] = ar_ok
            b['S'] = S
            b['V'] = V
            kombinacije.append(b)
    return kombinacije 



# naredi array velikosti n različnih dolžin palic (če je vhodni podatek x array velikosti n) / naredi palico dolžine x (če je vhodni podatek float)
def create_palica(x):
    V = x*(math.pi)*(r_palice)**2
    b = dict()
    b['x'] = x
    b['V'] = V
    return b















# ---------------------------------------------------------------------------------------------------------------------------------
# 1. DEL: katere konfiguracije ustrezajo prostornini škatle

ustrezajo = []
prostornine = np.array([0])
dolzine = np.array([0])
povrsine = np.array([0])
skatlaste_prostornine = np.array([0])
prostornine_kril = np.array([0])
xidim_skatla = np.array([0])
yidim_skatla = np.array([0])
xikrila = np.array([0])
yikrila = np.array([0])

trup = create_trup_fix(trup_x, trup_y, trup_z)
rep = create_rep_fix(rep_x, rep_y, rep_z)
x = np.linspace(x_min, x_max, n)                             # naredi n različnih dolžin palic
palica = create_palica(x)


# zunanji for loop: za vsako dolžino palice ustvari n^2 konfiguracij kril (n različnih dolžin kril, n različnih površin)
# notranji for loop: za vsako konfiguracijo izračuna, ali paše v škatlo po prostornini
for x_palice in palica['x']:
    krila = create_krila_S()
   
    xi = np.empty(n)
    xi.fill(x_palice)

    for krilo in krila:
        x_krila = krilo['x']
        y_krila = krilo['y']
        x_dim_skatle = np.where(x_krila < x_palice, x_palice, x_krila)       # škatla je dolga kot palica/krilo (odvisno, kaj je daljše), razmerje med debelino in globino škatle je z=0.117y
        y_dim_skatle = (vsota_dolzin - x_dim_skatle)/1.117                          # iz pogoja, da je z=0.117*y
        z_dim_skatle = 0.117*y_dim_skatle
        nekaj_V_skatle = x_dim_skatle*y_dim_skatle*z_dim_skatle


        V_celotna = palica['V'] + krilo['V'] + trup['V'] + rep['V']
        V_ustreza = np.where(V_celotna < nekaj_V_skatle, V_celotna, 0)
        prostornine_kril = np.append(prostornine_kril, krilo['V'])
        prostornine = np.append(prostornine, V_ustreza)
        dolzine = np.append(dolzine, xi)
        povrsine = np.append(povrsine, krilo['S'])
        skatlaste_prostornine = np.append(skatlaste_prostornine, nekaj_V_skatle)
        xidim_skatla = np.append(xidim_skatla, x_dim_skatle)
        yidim_skatla = np.append(yidim_skatla, y_dim_skatle)
        xikrila = np.append(xikrila, x_krila)
        yikrila = np.append(yikrila, y_krila)




# plotting
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_title(r'$V (x, S)$' + ' (ustrezajoča prostornina)')
ax.set_xlabel("x palice " + r'$[m]$')
ax.set_ylabel("S kril " + r'$[m^2]$')
ax.set_zlabel("V " + r'$[m^3]$')

mask = prostornine > 0
ax.scatter(dolzine[mask], povrsine[mask], prostornine[mask], label='V komponent')
ax.scatter(dolzine[mask], povrsine[mask], skatlaste_prostornine[mask], c='red', label='V škatle')
ax.set_zlim(0, np.amax(skatlaste_prostornine))
plt.legend()
plt.show()























# ------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. DEL: zlaganje v škatlo; katere konfiguracije, ki so prestale prvi del, gredo dejansko v škatlo po dimenzijah

krila_vskatlo_podolzini = np.where(xidim_skatla >= xikrila, 1, 0)
krila_vskatlo_posirini = np.where(yidim_skatla >= yikrila, 1, 0)  
krila_vskatlo_obedimenziji = krila_vskatlo_podolzini*krila_vskatlo_posirini

print(np.count_nonzero(krila_vskatlo_podolzini))
print(np.count_nonzero(krila_vskatlo_posirini))
print(np.count_nonzero(krila_vskatlo_obedimenziji))
indeksi_veljavnih_konfiguracij = np.nonzero(krila_vskatlo_obedimenziji)
print(indeksi_veljavnih_konfiguracij)
kateri_x = np.take(xikrila, indeksi_veljavnih_konfiguracij)
kateri_y = np.take(yikrila, indeksi_veljavnih_konfiguracij)
kateredolzinepalice = np.take(dolzine, indeksi_veljavnih_konfiguracij)
print(kateri_x)
print(kateri_y)
print(kateredolzinepalice)




# plotting
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_title(r'$V (x, S)$' + ' (krila grejo v škatlo)')
ax.set_xlabel("x palice " + r'$[m]$')
ax.set_ylabel("S kril " + r'$[m^2]$')
ax.set_zlabel("V " + r'$[m^3]$')

mask = prostornine > 0
ax.scatter(np.take(dolzine, indeksi_veljavnih_konfiguracij), np.take(povrsine, indeksi_veljavnih_konfiguracij), np.take(prostornine, indeksi_veljavnih_konfiguracij), label='V komponent')
ax.scatter(dolzine[mask], povrsine[mask], skatlaste_prostornine[mask], c='red', label='V škatle')
ax.set_xlim(np.amin(dolzine[mask]), np.amax(dolzine[mask]))
ax.set_ylim(np.amin(povrsine[mask]), np.amax(povrsine[mask])) 
ax.set_zlim(0, np.amax(skatlaste_prostornine))
plt.legend()
plt.show()