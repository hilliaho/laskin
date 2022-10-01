class Muuttujat():
    def __init__(self):
        self.muuttujat = []

    def lisaa_muuttuja(self, lauseke):
        lauseke=lauseke.split("=")
        nimi=lauseke[0]
        arvo=lauseke[1]
        for muuttuja in self.muuttujat:
            if muuttuja[0]==nimi:
                muuttuja[1]=arvo
                return
        self.muuttujat.append([nimi,arvo])