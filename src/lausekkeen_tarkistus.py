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
        operaattoreita_perakkain = 0
        desimaalipisteet_lkm = 0
        sulut_lkm = 0
        for merkki in lauseke:
            if merkki not in self.numerot and merkki not in self.kirjaimet and merkki not in self.operaattorit:
                return False
            if merkki in self.operaattorit:
                operaattoreita_perakkain += 1
                if operaattoreita_perakkain == 2:
                    return False
            else:
                operaattoreita_perakkain = 0
            if merkki == ".":
                desimaalipisteet_lkm += 1
                if desimaalipisteet_lkm == 2:
                    return False
            if merkki == "(":
                sulut_lkm += 1
            if merkki == ")":
                sulut_lkm -= 1
        if sulut_lkm != 0:
            return False
        return True
