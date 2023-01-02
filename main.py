from stadion import Stadion
import datetime

def fajl(stadionok):
    f = open(stadionok,"r",encoding='utf-8')
    fejlec = f.readline().strip()
    sorok = f.readlines()
    f.close()
    f_feldolgozas(sorok)

stad = []


def f_feldolgozas(sorok):
    i = 0
    while (i < len(sorok)):
        sor = sorok[i].strip().split(';')
        stad.append((Stadion(sor[0], sor[1], sor[2], sor[3], sor[4])))
        #print(stad)
        i += 1

def new_york(city):
    db = 0
    i = 0
    while(i < len(stad)):
        if stad[i].varos == city:
            db += 1
        i += 1
    print(f'\nA New York-i stadionok száma: {db}')
    #print(type(stad))

def csapatok():
    print(f'\nÖsszes csapat száma: {Stadion.csapatszam}')

def regiek():
        regi_csapat_db = 0
        i = 0
        regi_csapatok_lista = []
        regi_csapatok_txt = ""
        while(i < len(stad)):
            if datetime.date.fromisoformat(stad[i].elsom) < datetime.date(1900, 1, 1):
                regi_csapat_db += 1
                regi_csapatok_lista.append(stad[i].nev)
            i += 1
        print(f'\n1900.01.01 előtt már volt mérkőzése {regi_csapat_db} csapatnak:')
        #print(regi_csapatok_lista)
        c = 0
        while(c < len(regi_csapatok_lista)):
            if c == len(regi_csapatok_lista):
                regi_csapatok_txt = regi_csapatok_txt + regi_csapatok_lista[c]
            else:
                regi_csapatok_txt = regi_csapatok_txt + regi_csapatok_lista[c] + '\n'
            c += 1
        print(regi_csapatok_txt)

def buffalo(city):
    db = 0
    i = 0
    while(i < len(stad)):
        if stad[i].varos == city:
            db = db + int(stad[i].csapat)
        i += 1
    print(f'\nA Buffalo-i csapatok száma: {db}')
    #print(type(stad))

def ketezer():
    db = 0
    stadion_db = 0
    i = 0
    while(i < len(stad)):
        datum = datetime.date.fromisoformat(stad[i].utolsom)
        if int(datum.year) < 2000:
            db = db + int(stad[i].csapat)
            stadion_db += 1
        i += 1
    print(f'2000 óta nem volt mérkőzés {db} csapatnál.')
    print(f'2000 óta nem volt mérkőzés {stadion_db} stadionban.')

fajl("stadionok.txt")
csapatok()
new_york("New York")
regiek()
ketezer()
buffalo("Buffalo")



