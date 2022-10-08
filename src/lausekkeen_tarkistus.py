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
        for merkki in lauseke:
            if merkki not in self.numerot and merkki not in self.kirjaimet and merkki not in self.operaattorit:
                print("error")
                return False
        return True
