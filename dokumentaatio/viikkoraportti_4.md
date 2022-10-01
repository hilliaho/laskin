# Viikkoraportti 4

Tällä viikolla olen lisännyt mahdollisuuden käyttäjälle lisätä omia muuttujia ja antaa niille arvoja, sekä käyttää niitä laskuissa.
Olen korjannut koodia niin, että laskin laskee vähennyslaskut oikein ja huomioi negatiiviset luvut. 
Olen lisännyt metodin, joka tarkistaa, onko käyttäjän antama lauseke oikeanlainen niin, ettei se aiheuta virhetilanteita laskimessa.
Olen myös lisännyt pari yksikkötestiä.

Vaikeinta oli saada negatiiviset luvut lisättyä, eli että esimerkiksi lauseke -8-1 tai (-3)^(-2) lasketaan oikein.
Tein tämän nyt niin, että lisäsin lausekkeeseen numeron 0 tarvittaviin kohtiin, niin että yllä olevista lausekkeista esimerkiksi tulisi 0-8-1 ja (0-3)^(0-2),
en tiedä olisiko tämän voinut tehdä jollain fiksummallakin tavalla.

Projektiin käytetty aikaa tällä viikolla 8 tuntia.
