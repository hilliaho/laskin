import unittest

from lausekkeen_tarkistus import LausekkeenTarkistus


class TestiLausekkeenTarkistus(unittest.TestCase):

    def setUp(self):
        operaattorit = ["+", "-", "*", "/", "^", "=", "(", ")"]
        numerot = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        kirjaimet = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "å", "a", "s",
                          "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "z", "x", "c", "v", "b", "n", "m"]
        self.lausekkeen_tarkistus = LausekkeenTarkistus(
            numerot, kirjaimet, operaattorit)

    def testi_oikeanlainen_lauseke_hyvaksytaan(self):
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("1+2"), True)

    def testi_tunnistamaton_merkki(self):
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("1,2"), False)
