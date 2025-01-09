import py1
def test_nagyobb():
    assert py1.nagyobb(12, -8) == 12
    assert py1.nagyobb(-12, -8) == -8
    assert py1.nagyobb(12, 8) == 12
    assert py1.nagyobb(-12, 8) == 8
    assert py1.nagyobb(12, 12) == 12
    assert py1.nagyobb(-12, -12) == -12
    assert py1.nagyobb(0, 0) == 0
    assert py1.nagyobb(0, 12) == 12
    assert py1.nagyobb(0, -12) == 0
    assert py1.nagyobb(12, 0) == 12
    