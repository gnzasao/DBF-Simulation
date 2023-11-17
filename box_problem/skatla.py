# 1. step: preverim za različne kombinacije, ali skupna PROSTORNINA manjša od prostornine škatle
# 2. step: poiščem najboljše take kombinacije (optimiziram)
# 3. step: optimiziram ZLAGANJE; pri tem bodo nekatere kombinacije iz točk 1 in 2 izločene.


 
import random
import math


# vse v osnovnih enotah
V = 1.5748
krila_x = 0
krila_y = 0
krila_S = 0
ar = 5
st_decimalk = 4



# Izračun za eno krilo! (v škatli potrebujemo dva para kril, torej 4 krila)
def kombinacije_krila(quantity=10000):
    krila_S = 0
    ar = 5
    kandidati = []
    for i in range(quantity):
        krila_x = random.random() * 2.5
        krila_y = random.random() * 1
        krila_z = random.random() * 0.5
        if krila_x < 1:
            continue
        krila_S = krila_x*krila_y
        ar = krila_x**2 / krila_S
        krila_V = krila_S * krila_z
        if 0.4 < krila_S < 1.2 and 4 < ar < 10:
            a = dict()
            a["x"] = round(krila_x, st_decimalk)
            a['y'] = round(krila_y, st_decimalk)
            a['z'] = round(krila_z, st_decimalk)
            a['S'] = round(krila_S, st_decimalk)
            a['ar'] = round(ar, st_decimalk)
            a['V'] = round(krila_V, st_decimalk)
            kandidati.append(a)
    return kandidati





def kombinacije_trup(quantity=5000):
    kandidati = []
    for i in range(quantity):
        trup_x = random.random() * 3
        trup_y = random.random() * 1
        trup_z = random.random() * 0.5
        trup_V = trup_x * trup_y * trup_z
        if trup_V > V * 4/5:
            continue
        b = dict()
        b['x'] = round(trup_x, st_decimalk)
        b['y'] = round(trup_y, st_decimalk)
        b['z'] = round(trup_z, st_decimalk)
        b['V'] = round(trup_V, st_decimalk)
        kandidati.append(b)
    return kandidati


def kombinacije_rep():
    pass
        

# source: https://www.engineeringtoolbox.com/pvc-cpvc-pipes-dimensions-d_795.html
def antena(quantity=1000):
    kandidati = []
    x = 0
    r = (21.3 * 10e-3)/2
    for i in range(quantity):
        x = random.random() * 1.6
        V = x*math.pi*r**2
        c = dict()
        c['x'] = round(x, st_decimalk)
        c['V'] = round(V, st_decimalk)
        kandidati.append(c)
    return kandidati






def create_krila(x=1.5, y=0.5, z=0.3, S=0.75, ar=3):      # 4x
    pass

def create_trup(x=1.5, y=0.5, z=0.3):
    pass


def create_rep(x=0.3, y=0.15, z=0.05):     # 2x
    pass


def create_palica(x=1.5, r=(21.3 * 10e-3)/2):
    a = dict()
    a['x'] = x
    a['V'] = x*math.pi*r**2
    return a




def gre_v_skatlo(V, krila, trup, palica, rep):
    V_krila = create_krila(x=krila['x'], y=krila['y'], z=krila['z'])
    V_trup = create_trup(x=trup['x'], y=trup['y'], z=trup['z'])
    V_rep = create_rep(x=rep['x'], y=rep['y'], z=rep['z'])
    V_palica = create_palica(x=palica['x'])

    V_skupaj = V_krila + V_trup + V_rep + V_palica
    return V_skupaj < V









def create_krila_dana_S(x, S):     # 4 krila
    kandidati = []
    spodnja_meja = 0.5
    dodatek = x - spodnja_meja
    for i in range(1000):
        x = random.random()*dodatek + spodnja_meja
        y = S/x
        ar = x**2 / S
        if ar < 4 or ar > 10:
            continue
        z = 0.07
        V_kril = x*y*z
        a = dict()
        a["x"] = round(x, st_decimalk)
        a['y'] = round(y, st_decimalk)
        a['z'] = round(z, st_decimalk)
        a['V'] = 4 * round(V_kril, st_decimalk)

        kandidati.append(a)
    return kandidati




def create_trup_fix(x):
    a = dict()
    x = x
    y = 0.15
    z = 0.15
    a['x'] = x
    a['y'] = y
    a['z'] = z
    a['V'] = x*y*z
    return a


def create_rep_fix():     # 2 ista dela repa
    b = dict()
    x=0.3
    y=0.15
    z=0.05
    b['x'] = x
    b['y'] = y
    b['z'] = z
    b['V'] = 2 * x*y*z
    return b











# assumam da bo dolzina skatle enaka dolzini antene (later postrani antena), vemo dolzino antene in povrsino kril
def gre_notri(x, S):
    ustrezajo = []
    kandidati_krila = create_krila_dana_S(x, S)
    trup = create_trup_fix(2*x/3)
    rep = create_rep_fix()
    palica = create_palica(x=x)

    for krilo in kandidati_krila:
        V_skupaj = krilo['V'] + trup['V'] + rep['V'] + palica['V']
        if V_skupaj > V:
            continue
        ustrezajo.append(krilo)
    return ustrezajo

























# Radi bi dosegli da pri dani dolzini antene in povrsini kril vemo, ce lahko zlozimo avijon v skatlo al ne



def main():
    krila = kombinacije_krila(1000)
    trupi = kombinacije_trup()
    palice = antena()
    print(len(krila))
    print(len(trupi))
    print(len(palice))
    kombinacije = []
    skupaj = len(krila)* len(trupi) * len(kombinacije)
    print(skupaj)
    count = 0

    for krilo in krila:
        print('krilo št ', count)
        count+=1
        for trup in trupi:
            for palica in palice:
                if palica['x'] < krilo['x'] or palica['x'] < trup['x']:   #izlocim vse tiste, kjer je x palice manjsi x trupa ali x krila, ker to je brezveze
                    continue
                elif palica['V'] + trup['V'] + 4*krilo['V'] > V:
                    continue
                kombinacija = (krilo, trup, palica)
                kombinacije.append(kombinacija)
    urejene_kombinacije = sorted(kombinacije, key=lambda x: x[2]['x'], reverse=True)  #sortiram po dolžini palice
    return urejene_kombinacije
    







x = kombinacije_krila(1000)

y = kombinacije_trup()

z = antena()



""" a = main()
with open('rezultati.txt', 'w') as f:
    for kombinacija in a:
        f.write(str(kombinacija))
        f.write('\n')
f.close() """





a = gre_notri(x=1.6, S=0.4)
a = sorted(a, key=lambda x: x['x'], reverse=True)

with open('gre-notri.txt', 'w') as f:
    for kombinacija in a:
        f.write(str(kombinacija))
        f.write('\n')
f.close()









vse = []
for i in range(9):
    povrsina = 0.4 + i*0.1
    for i in range(11):
        x = 1 + 0.05*i
        a = gre_notri(x=x, S=povrsina)
        vse.append(a)

vse_venem = []
for ustrezajoce in vse:
    for kombinacija in ustrezajoce:
        vse_venem.append(kombinacija)


allinone = sorted(a, key=lambda x: x['x'], reverse=True)






with open('gre-notri-vse.txt', 'w') as f:
    for kombinacija in allinone:
        f.write(str(kombinacija))
        f.write('\n')
f.close()

# narisi funkcijo V(x, y) za fiksen x-antene in S kril, kjer x kril manjsi ali enak x-antene.



# najprej daj tako kot zgoraj, nato probaj se multivariable function narest V(krila_x, ...), potem dass pogooj V < V_skatle in preveris ostale pogoje: S kril, ar ...

# 1.5m zaradi same skatle. Za krila pa nekje od 0.4 - 1.2 m2 povrsine pri cemer lahko spreminjamo ar kril med 4-10.