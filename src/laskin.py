from kayttoliittyma import Kayttoliittyma
from laskutoimitukset import Laskutoimitukset
from shunting_yard import ShuntingYard
from muuttujat import Muuttujat
from lausekkeen_tarkistus import LausekkeenTarkistus
import math


class Laskin():
    """Luokka, joka vastaa laskimen sovelluslogiikasta
    """

    def __init__(self):
        """Luokan konstruktori
        """
        self.operaattorit = ["+", "-", "*", "/", "^", "=", "(", ")"]
        self.numerot = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        self.kirjaimet = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "å", "a", "s",
                          "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "z", "x", "c", "v",
                           "b", "n", "m"]
        self.kayttoliittyma = Kayttoliittyma()
        self.muuttujat = Muuttujat()
        self.laskutoimitukset = Laskutoimitukset(
            self.muuttujat, self.numerot, self.kirjaimet, self.operaattorit)
        self.shunting_yard = ShuntingYard(self.numerot, self.kirjaimet)
        self.lausekkeen_tarkistus = LausekkeenTarkistus(
            self.numerot, self.kirjaimet, self.operaattorit)

    def aloita(self):
        """Pyörittää laskimen toimintaa silmukan avulla
        """
        
        while True:
            self.muuttujat.lisaa_muuttuja(['pi', '=', str(math.pi)])
            lauseke = self.kayttoliittyma.syote()
            if self.lausekkeen_tarkistus.tarkista(lauseke) is False:
                print("virheellinen syöte")
                continue
            if lauseke == "-1":
                break

            lauseke = self._lausekkeen_muunto(lauseke)
            if "=" in lauseke:
                self.muuttujat.lisaa_muuttuja(lauseke)
                continue
            postfix_lauseke = self.shunting_yard.muunna(lauseke)
            self.kayttoliittyma.tulos(
                self.laskutoimitukset.laske(postfix_lauseke))
        

    def _lausekkeen_muunto(self, lauseke):
        lauseke = lauseke.replace(" ", "")
        lauseke = lauseke.replace("**", "^")
        merkkijono=""
        uusi_lauseke=[]
        edellinen_merkki=""

        for merkki in lauseke:
            if merkki not in self.numerot and edellinen_merkki == "numero":
                uusi_lauseke.append(merkkijono)
                merkkijono=""
            elif merkki not in self.kirjaimet and edellinen_merkki == "kirjain":
                if merkkijono in ("sin", "cos", "tan"):
                    uusi_lauseke.append(merkkijono)
                else:
                    uusi_lauseke.append(merkkijono)
                merkkijono=""

            if merkki in self.numerot:
                merkkijono += merkki
                edellinen_merkki = "numero"
            elif merkki in self.kirjaimet:
                merkkijono += merkki
                edellinen_merkki = "kirjain"
            elif merkki in self.operaattorit:
                uusi_lauseke.append(merkki)
                edellinen_merkki = "operaattori"
        if edellinen_merkki == "numero":
            uusi_lauseke.append(merkkijono)
        elif edellinen_merkki == "kirjain":
            uusi_lauseke.append(merkkijono)

        
        return uusi_lauseke

            






