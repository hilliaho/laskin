import unittest

from lausekkeen_tarkistus import LausekkeenTarkistus


class TestiLausekkeenTarkistus(unittest.TestCase):

    def setUp(self):
        operaattorit = ["+", "-", "*", "/", "^", "=", "(", ")"]
        numerot = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        kirjaimet = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "å", "a", "s",
                          "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "z", "x", "c", "v", "b", "n", "m"]
        self.lausekkeen_tarkistus = LausekkeenTarkistus(
            numerot, kirjaimet, operaattorit)

    def testi_hyvaksyttavat_lausekkeet(self):
        self.assertEqual(
            self.lausekkeen_tarkistus.tarkista("sin(1.234+2)"), ['sin', '(', '1.234', '+', '2', ')'])
        self.assertEqual(self.lausekkeen_tarkistus.tarkista(
            "72-8"), ['72', '-', '8'])
        self.assertEqual(self.lausekkeen_tarkistus.tarkista(
            "-(1+20.5)*5"), ['-', '(', '1', '+', '20.5', ')', '*', '5'])
        self.assertEqual(self.lausekkeen_tarkistus.tarkista(
            "cos(9.345)-2.2"), ['cos', '(', '9.345', ')', '-', '2.2'])
        self.assertEqual(self.lausekkeen_tarkistus.tarkista(
            "-2**5"), ['-', '2', '^', '5'])
        self.assertEqual(self.lausekkeen_tarkistus.tarkista(
            "-(1+(2*x)/16)-koira"), ['-', '(', '1', '+', '(', '2', '*', 'x', ')', '/', '16', ')', '-', 'koira'])

    def testi_tunnistamaton_merkki(self):
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("1,2"), False)
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("6%40"), False)
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("2<4"), False)

    def testi_muuttujan_lisays_hyvaksytaan(self):
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("x=252987"), True)
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("a=23.456"), True)

    def testi_virheelliset_lausekkeet(self):
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("1--2"), False)
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("(.2+2)"), False)
        self.assertEqual(
            self.lausekkeen_tarkistus.tarkista("(1+2)(3-4)"), False)
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("5(4-2)1"), False)
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("3.14.5"), False)
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("1*(1+3"), False)
        self.assertEqual(self.lausekkeen_tarkistus.tarkista(")1+0("), False)
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("x="), False)
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("x=a"), False)
        self.assertEqual(self.lausekkeen_tarkistus.tarkista("=9"), False)
