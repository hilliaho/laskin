class LausekkeenTarkistus():
    """Luokka, joka tarkistaa, onko annettu lauseke sellainen, jonka laskin osaa laskea
    """

    def __init__(self, numerot, kirjaimet, operaattorit):
        self.numerot = numerot
        self.kirjaimet = kirjaimet
        self.operaattorit = operaattorit

    def tarkista(self, lauseke):
        """Tarkistaa, että lauseke on sääntöjen mukainen

        Args:
            lauseke (merkkijono): tarkistettava lauseke
        """
        if "=" in lauseke:
            return self._tarkista_muuttujan_lisays(lauseke)
        if not (self._tarkista_sulut(lauseke) and self._tarkista_desimaalipisteet(lauseke) and self._tarkista_lausekkeen_jarjestys(lauseke)):
            return False
        return True

    def _tarkista_lausekkeen_jarjestys(self, lauseke):
        lauseke = lauseke.replace("**", "^")
        edellinen_merkki=""
        for merkki in lauseke:
            if merkki not in self.numerot and merkki not in self.kirjaimet and merkki not in self.operaattorit:
                return False
            if edellinen_merkki=="" or edellinen_merkki=="(":
                if merkki == "." or not (merkki in self.kirjaimet or merkki in self.numerot or merkki =="(" or merkki =="-"):
                    return False
            elif edellinen_merkki == ")":
                if merkki in self.numerot or merkki in self.kirjaimet or merkki == "(" or merkki == ".":
                    return False
            elif edellinen_merkki in self.operaattorit:
                if merkki == "." or not (merkki in self.kirjaimet or merkki in self.numerot or merkki =="(" ):
                    return False
            elif edellinen_merkki in self.numerot:
                if merkki == "(":
                    return False
            edellinen_merkki = merkki
        return True


    def _tarkista_muuttujan_lisays(self, lauseke):
        lauseke=lauseke.split("=")
        nimi = lauseke[0]
        arvo = lauseke[1]
        if len(nimi)==0 or len(arvo)==0:
            return False
        for merkki in arvo:
            if merkki not in self.numerot:
                return False
        return True

    def _tarkista_sulut(self, lauseke):
        pino = []
        for merkki in lauseke:
            if merkki == "(":
                pino.append("(")
            elif merkki == ")":
                if len(pino)==0:
                    return False
                pino.pop()
        if len(pino) != 0:
            return False
        return True

    def _tarkista_desimaalipisteet(self, lauseke):
        desimaalipisteet=0
        for merkki in lauseke:
            if merkki not in self.numerot:
                desimaalipisteet=0
            if merkki == ".":
                desimaalipisteet += 1
            if desimaalipisteet > 1:
                return False
        return True

