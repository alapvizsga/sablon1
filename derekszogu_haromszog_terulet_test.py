import py1
def test_derekszogu_haromszog_terulet():
    assert py1.derekszogu_haromszog_terulet(3, 4) == 6
    assert py1.derekszogu_haromszog_terulet(5, 12) == 30
    assert py1.derekszogu_haromszog_terulet(9, 12) == 54
    assert py1.derekszogu_haromszog_terulet(15, 8) == 60
    assert py1.derekszogu_haromszog_terulet(7, 24) == 84
    assert py1.derekszogu_haromszog_terulet(21, 20) == 210
    assert py1.derekszogu_haromszog_terulet(27, 36) == 486
    assert py1.derekszogu_haromszog_terulet(35, 12) == 210
    assert py1.derekszogu_haromszog_terulet(45, 28) == 630
    assert py1.derekszogu_haromszog_terulet(63, 16) == 504
    assert py1.derekszogu_haromszog_terulet(77, 36) == 1386
    assert py1.derekszogu_haromszog_terulet(99, 20) == 990
    assert py1.derekszogu_haromszog_terulet(105, 28) == 1470
    assert py1.derekszogu_haromszog_terulet(117, 44) == 2574
    assert py1.derekszogu_haromszog_terulet(135, 92) == 6210
    assert py1.derekszogu_haromszog_terulet(147, 44) == 3234
    assert py1.derekszogu_haromszog_terulet(153, 100) == 7650
    assert py1.derekszogu_haromszog_terulet(165, 52) == 4290
