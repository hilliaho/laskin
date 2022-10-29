class Muuttujat():
    def __init__(self):
        self.muuttujat = {}

    def lisaa_muuttuja(self, lauseke):
        nimi = str(lauseke[0])
        if "." in lauseke[2]:
            arvo = float(lauseke[2])
        else:
            arvo = int(lauseke[2])
        self.muuttujat[nimi] = arvo

    def onko_muuttuja_olemassa(self, nimi):
        if str(nimi) in self.muuttujat:
            return True
        return False

    def arvo(self, nimi):
        if str(nimi) in self.muuttujat:
            return self.muuttujat[nimi]
        return False
