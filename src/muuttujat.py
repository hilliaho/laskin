class Muuttujat():
    def __init__(self):
        self.muuttujat = {}

    def lisaa_muuttuja(self, lauseke):
        lauseke = lauseke.split("=")
        nimi = str(lauseke[0])
        arvo = float(lauseke[1])
        self.muuttujat[nimi] = arvo
        print(self.muuttujat)

    def onko_muuttuja_olemassa(self, nimi):
        if str(nimi) in self.muuttujat:
            return True
        return False

    def arvo(self, nimi):
        if str(nimi) in self.muuttujat:
            return self.muuttujat[nimi]
        else:
            print("muuttujaa ei löydy")
            return False
