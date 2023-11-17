# Razredi

## class Part

### objektni atributi
- **pozicija** ... numpy array dolžine 3, 'pozicija (x, y, z) težišča tega dela', 
- **funkcija** ... str, 'funkcija, ki jo opravlja ta del (levo krilo, trup itd.)', 
- **masa** ... float, 'masa'
- **C_upora** ... float, 'koeficient upora čelno (tj. v smeri x osi)'
- **mvm** ... dict, npr. mvm["I_xx"] = 1, 'vztrajnostni momenti tega dela okoli glavnih osi, glede na težišče tega dela'



## class Kvader (extends Part) 
### dodatni objektni atributi
- **a, b, c** ... float, 'dimenzije kvadra v x, y, z smeri'



## class Valj (extends Part)
### dodatni objektni atributi
- **r, h** ... float, 'dimenziji valja, radij in višina, poljubna orientacija'
- **os** ... "x", "y" ali "z", 'pove, v smeri katere koordinatne osi leži glavna os valja'



## class Krogla (extends Part)
### dodatni objektni atributi
- **r** ... float, 'radij krogle'



## class Tocka (extends Part)
/





## class Fuselage
### razredni atributi 
(popisujejo celotno letalo)
- **parts** ... dict, 'vsi narejeni objekti shranjeni'
- **masa** ... float, 'masa celotnega letala'
- **tezisce** ... numpy array dolžine 3, 'pozicija (x, y, z) težišča celotnega letala (vseh delov skupaj)'
- **mvm** ... dict, npr. mvm["I_xx"] = 1, 'vztrajnostni momenti celega letala okoli glavnih osi, glede na težišče letala', ```{"I_xx": I_xx, "I_yy": I_yy, "I_zz": I_zz}```


### objektni atributi
- **nos** ... objekt razreda Part 
- **levo_krilo** ... objekt razreda Part 
- **desno_krilo** ... objekt razreda Part 
- **glavni_del** ... objekt razreda Part 
- **rep** ... objekt razreda Part 
- **args** ... objekti razreda Part, 'poljubno možno dodatnih delov' 



<br/>
<br/>


# Ostalo

## Predpostavke:
- deli so homogeni
- deli so geometričnih oblik: kvader, valj
- lastne osi vztrajnostnega momenta vseh delov so vzdolž koordinatnih osi (tenzor mvm diagonalne oblike)
- letalo je orientirano v smeri x osi, krila ležijo v xy ravnini
- vse enote so osnovne SI

## Opombe
- izbira koordinatnega izhodišča je poljubna
- še za dodati: druge oblike teles (npr. tetraeder)
