import unittest

from muuttujat import Muuttujat


class TestiMuuttujat(unittest.TestCase):
    def setUp(self):
        self.muuttujat = Muuttujat()

    def testi_muuttuja_tallentuu(self):
        self.muuttujat.lisaa_muuttuja(['x', '=', '9.0'])
        self.assertEqual(self.muuttujat.muuttujat, {'x': 9.0})

    def testi_muuttuja_on_olemassa(self):
        self.muuttujat.lisaa_muuttuja(['y', '=', '2'])
        self.assertEqual(self.muuttujat.onko_muuttuja_olemassa("y"), True)

    def testi_muuttuja_ei_ole_olemassa(self):
        self.assertEqual(self.muuttujat.onko_muuttuja_olemassa("z"), False)

    def testi_muuttujan_arvo_on_oikea(self):
        self.muuttujat.lisaa_muuttuja(['koira', '=', '56'])
        self.assertEqual(self.muuttujat.arvo("koira"), 56)
