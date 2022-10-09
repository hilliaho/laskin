class Kayttoliittyma():

    def syote(self):
        """pyytää käyttäjältä syötettä

        Returns:
            lauseke (merkkijono): käyttäjän antama syöte
        """
        lauseke = input("lauseke: ")
        return lauseke

    def tulos(self, tulos):
        """tulostaa laskutoimituksen tuloksen

        Args:
            tulos (liukuluku): laskimella laskettu tulos
        """
        print(tulos)
