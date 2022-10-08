import unittest

from shunting_yard import ShuntingYard

class TestiShuntingYard(unittest.TestCase):
    def setUp(self):
        numerot = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        kirjaimet = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "å", "a", "s",
                          "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "z", "x", "c", "v", "b", "n", "m"]
        self.shunting_yard=ShuntingYard(numerot, kirjaimet)

    def testi_lausekkeen_muuntaminen_toimii_oikein(self):
        lauseke = self.shunting_yard.muunna("3+4*(2-1)")
        self.assertEqual(lauseke, ["3", "4", "2", "1", "-", "*", "+"])
        
