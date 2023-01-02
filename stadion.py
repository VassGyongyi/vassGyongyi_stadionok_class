

class Stadion:
    csapatszam = 0
    def __init__(self, nev, varos, csapat, elsom, utolsom):
        self.nev = nev
        self.varos = varos
        self.csapat = csapat
        self.elsom = elsom
        self.utolsom = utolsom
        if csapat:
            type(self).csapatszam = type(self).csapatszam + int(self.csapat)


    def __str__(self):
      return f"{self.nev}:{self.varos},{self.csapat},{self.elsom},{self.utolsom}"


