import marimo

__generated_with = "0.10.7"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""![](wesselenyi.png)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Két szám összege. (2 pont)
        - Írj egy függvényt __osszead__ néven,
        - amely két számot kap és
        - visszatér a két szám összegével.
        """
    )
    return


@app.cell
def _():
    def osszead(szam1, szam2):
        """ A függvény két számot kap és 
            visszatér a két szám összegével.
        """
        # YOUR CODE HERE
        raise NotImplementedError()
    return (osszead,)


@app.cell
def _(osszead):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert osszead(14, -8) == 6
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Melyik a kisebb? (2 pont)
        - Írj egy függvényt __kisebb__ néven,
        - amely két számot kap és
        - visszatér a kisebbel.
        """
    )
    return


@app.cell
def _():
    def kisebb(szam1, szam2):
        """ A függvény két számot kap és 
            visszatér a kisebbel.
        """
        # YOUR CODE HERE
        raise NotImplementedError()
    return (kisebb,)


@app.cell
def _(kisebb):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert kisebb(10, -7) == -7
    assert kisebb(-10, 7) == -10
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Melyik a nagyobb? (2 pont)
        - Írj egy függvényt __nagyobb__ néven,
        - amely két számot kap és
        - visszatér a nagyobbal.
        """
    )
    return


@app.cell
def _():
    def nagyobb(szam1, szam2):
        """ A függvény két számot kap és 
            visszatér a nagyobbal.
        """
        # YOUR CODE HERE
        raise NotImplementedError()
    return (nagyobb,)


@app.cell
def _(nagyobb):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert nagyobb(12, -8) == 12
    assert nagyobb(-12, -8) == -8
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Számtani közép (2 pont)
        - Írj __szamtani_kozep__ néven függvényt,
        - amely két számot kap bemenetként és
        - visszatér a számtani középpel.
        """
    )
    return


@app.cell
def _():
    def szamtani_kozep(szam1, szam2):
        """ A függvény két számot kap és 
            visszatér a számtani középpel.
        """
        # YOUR CODE HERE
        raise NotImplementedError()
    return (szamtani_kozep,)


@app.cell
def _(szamtani_kozep):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert szamtani_kozep(3, 5) == 4.0
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Négyzet kerülete (2 pont)
        - Írj __negyzet_kerulet__ néven függvényt,
        - amely egy négyzet oldalhosszát kapja bemenetként és
        - visszatér a négyzet kerületével.
        """
    )
    return


@app.cell
def _():
    def negyzet_kerulet(oldal):
        """ A függvény egy négyzet oldalhosszát kapja bemenetként és 
            visszatér a négyzet kerületével.
        """
        # YOUR CODE HERE
        raise NotImplementedError()
    return (negyzet_kerulet,)


@app.cell
def _(negyzet_kerulet):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert negyzet_kerulet(5.1) == 20.4
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Négyzet területe (2 pont)
        - Írj __negyzet_terulet__ néven függvényt,
        - amely egy négyzet oldalhosszát kapja bemenetként és
        - visszatér a négyzet területével.
        """
    )
    return


@app.cell
def _():
    def negyzet_terulet(oldal):
        """ A függvény egy négyzet oldalhosszát kapja bemenetként és 
            visszatér a négyzet területével.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (negyzet_terulet,)


@app.cell
def _(negyzet_terulet):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert negyzet_terulet(5.0) == 25.0
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Téglalap kerülete (2 pont)
        - Írj __teglalap_kerulet__ néven függvényt, 
        - amely egy téglalap oldalhosszait kapja bemenetként és 
        - visszatér a téglalap kerületével.
        """
    )
    return


@app.cell
def _():
    def teglalap_kerulet(oldal1, oldal2):
        """ A függvény egy téglalap oldalhosszait kapja bemenetként és 
            visszatér a téglalap kerületével.
        """
        # YOUR CODE HERE
        raise NotImplementedError()
    return (teglalap_kerulet,)


@app.cell
def _(teglalap_kerulet):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert teglalap_kerulet(5, 6) == 22
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Téglalap területe (2 pont)
        - Írj __teglalap_terulet__ néven függvényt,
        - amely egy téglalap oldalhosszait kapja bemenetként és
        - visszatér a téglalap területével.
        """
    )
    return


@app.cell
def _():
    def teglalap_terulet(oldal1, oldal2):
        """ A függvény egy téglalap oldalhosszait kapja bemenetként és 
            visszatér a téglalap területével.
        """
        # YOUR CODE HERE
        raise NotImplementedError()
    return (teglalap_terulet,)


@app.cell
def _(teglalap_terulet):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert teglalap_terulet(5, 6) == 30
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Két szám különbsége (2 pont)
        - Írj __kulonbseg__ néven függvényt,
        - amely két számot kap bemenetként és
        - visszatér a két szám különbségével.
        """
    )
    return


@app.cell
def _():
    def kulonbseg(szam1, szam2):
        """ A függvény két számot kap bemenetként és 
            visszatér a két szám különbségével.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (kulonbseg,)


@app.cell
def _(kulonbseg):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert kulonbseg(5, 6) == -1
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Maradékos osztás (2 pont)
        - Írj egy __maradek__ nevü függvényt,
        - amely két számot kap bemenetként és
        - visszatér a két szám osztásának maradékával.
        """
    )
    return


@app.cell
def _():
    def maradek(szam1, szam2):
        """ A függvény két számot kap bemenetként és 
            visszatér a két szám osztásának maradékával.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (maradek,)


@app.cell
def _(maradek):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert maradek(9, 4) == 1
    assert maradek(8, 4) == 0
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Páros szám (2 pont)
        - Írj egy __paros__ nevü függvényt,
        - amely egy számot kap bemenetként, majd
        - True-val tér vissza, ha a szám páros és
        - False-al tér vissza, ha a szám páratlan.
        """
    )
    return


@app.cell
def _():
    def paros(szam):
        """ A függvény egy számot kap bemenetként, 
            majd True-val tér vissza, ha a szám páros és 
            False-al ha a szám páratlan.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (paros,)


@app.cell
def _(paros):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert paros(9) == False
    assert paros(8) == True
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Kettővel osztható (2 pont)
        - Írj egy __kettovel_oszthato__ nevü függvényt,
        - amely egy számot kap bemenetként és
        - True-val tér vissza, ha a szám kettővel osztható és
        - False-al tér vissza ha nem.
        """
    )
    return


@app.cell
def _():
    def kettovel_oszthato(szam):
        """ A függvény egy számot kap bemenetként és 
            True-val tér vissza, ha a szám kettővel osztható és 
            False-al ha nem.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (kettovel_oszthato,)


@app.cell
def _(kettovel_oszthato):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert kettovel_oszthato(12) == True
    assert kettovel_oszthato(13) == False
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Hárommal osztható (2 pont)
        - Írj egy __harommal_oszthato__ nevü függvényt,
        - amely egy számot kap bemenetként és
        - True-val tér vissza, ha a szám hárommal osztható és
        - False-al  tér vissza ha nem.
        """
    )
    return


@app.cell
def _():
    def harommal_oszthato(szam):
        """ A függvény egy számot kap bemenetként és 
            True-val tér vissza, ha a szám hárommal osztható és 
            False-al ha nem.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (harommal_oszthato,)


@app.cell
def _(harommal_oszthato):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert harommal_oszthato(15) == True
    assert harommal_oszthato(16) == False
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Héttel osztható (2 pont)
        - Írj egy __hettel_oszthato__ nevü függvényt ,
        - amely egy számot kap bemenetként és
        - True-val tér vissza, ha a szám héttel osztható és
        - False-al tér vissza ha nem.
        """
    )
    return


@app.cell
def _():
    def hettel_oszthato(szam):
        """ A függvény egy számot kap bemenetként és 
            True-val tér vissza, ha a szám héttel osztható és 
            False-al ha nem.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (hettel_oszthato,)


@app.cell
def _(hettel_oszthato):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert hettel_oszthato(21) == True
    assert hettel_oszthato(22) == False
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Kocka térfogat (2 pont)
        - Írj egy __kocka_terfogat__ nevü függvényt,
        - amely bemenetként megkapja a kocka oldal hosszúságát és
        - a kocka térfogatával tér vissza.
        """
    )
    return


@app.cell
def _():
    def kocka_terfogat(oldal):
        """ A függvény bemenetként megkapja a kocka oldal hosszúságát és 
            a kocka térfogatával tér vissza.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (kocka_terfogat,)


@app.cell
def _(kocka_terfogat):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert kocka_terfogat(2) == 8
    assert kocka_terfogat(3) == 27
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Téglatest térfogat (2 pont)
        - Írj egy __teglatest_terfogat__ nevü függvényt,
        - amely bemenetként megkapja a téglatest oldalainak hosszúságát és
        - a téglatest térfogatával tér vissza.
        """
    )
    return


@app.cell
def _():
    def teglatest_terfogat(a, b, c):
        """ A függvény bemenetként megkapja a téglatest oldalainak hosszúságát és 
            a téglatest térfogatával tér vissza.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (teglatest_terfogat,)


@app.cell
def _(teglatest_terfogat):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert teglatest_terfogat(2, 3, 4) == 24
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Derékszögü háromszög területe (2 pont)
        - Írj egy __derekszogu_haromszog_terulet__ nevü függvényt,
        - amely bemenetként megkapja a befogók hosszát és a
        - háromszög területével tér vissza.
        """
    )
    return


@app.cell
def _():
    def derekszogu_haromszog_terulet(befogo1, befogo2):
        """ A függvény bemenetként megkapja a befogók hosszát és 
            a háromszög területével tér vissza.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (derekszogu_haromszog_terulet,)


@app.cell
def _(derekszogu_haromszog_terulet):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert derekszogu_haromszog_terulet(3, 4) == 6
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Derékszögü háromszög átfogója (2 pont)
        - Írj egy __derekszogu_haromszog_atfogo__ nevü függvényt,
        - amely bemenetként megkapja a befogók hosszát és
        - az átló hosszával tér vissza.
        """
    )
    return


@app.cell
def _():
    def derekszogu_haromszog_atfogo(befogo1, befogo2):
        """ A függvény bemenetként megkapja a befogók hosszát és 
            az átló hosszával tér vissza.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (derekszogu_haromszog_atfogo,)


@app.cell
def _(derekszogu_haromszog_atfogo):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert derekszogu_haromszog_atfogo(3, 4), 5.0
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Négyzet átlója (2 pont)
        - Írj egy __negyzet_atloja__ nevü függvényt,
        - amely bemenetként megkapja a négyzet oldalának hosszát és
        - az átló hosszával tér vissza.
        """
    )
    return


@app.cell
def _():
    def negyzet_atloja(oldal):
        """ A függvény bemenetként megkapja a négyzet oldalának hosszát és 
            az átló hosszával tér vissza.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (negyzet_atloja,)


@app.cell
def _(negyzet_atloja):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert round(negyzet_atloja(10),5) == round(14.142135623730951,5)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Téglalap átlója (2 pont)
        - Írj egy "__teglalap_atloja__" nevü függvényt,
        - amely bemenetként megkapja az oldalak hosszát és
        - az átló hosszával tér vissza.
        """
    )
    return


@app.cell
def _():
    def teglalap_atloja(a, b):
        """ A függvény bemenetként megkapja az oldalak hosszát és 
            az átló hosszával tér vissza.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (teglalap_atloja,)


@app.cell
def _(teglalap_atloja):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.

    assert teglalap_atloja(3, 4) == 5.0
    assert teglalap_atloja(6, 8) == 10.0
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ### Feladat: Abszolútérték (2 pont)
        - Írj egy __abszolut__ nevü függvényt, 
        - amely a bemenő paraméterként kapott szám 
        - abszolút értékével tér vissza.
        """
    )
    return


@app.cell
def _():
    def abszolut(szam):
        """ A függvény a bemenő paraméterként kapott szám 
            abszolút értékével tér vissza.
        """    
        # YOUR CODE HERE
        raise NotImplementedError()
    return (abszolut,)


@app.cell
def _(abszolut):
    # Ellenőrizd a függvényt a cella futtatásával! 
    # Az assert csak hiba esetén ad visszajelzést.assert abszolut( 3) == 3

    assert abszolut(-7) == 7
    assert abszolut( 0) == 0
    return


@app.cell
def _(mo):
    mo.md(r"""---""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
