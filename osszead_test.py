import py1
def test_osszead():
    assert py1.osszead(14, -8) == 6
    assert py1.osszead(-14, 8) == -6
    assert py1.osszead(-14, -8) == -22
    assert py1.osszead(14, 8) == 22