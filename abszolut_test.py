import py1
def test_abszolut():
    assert py1.abszolut(5) == 5
    assert py1.abszolut(-5) == 5
    assert py1.abszolut(0) == 0
    assert py1.abszolut(1.5) == 1.5
    assert py1.abszolut(-1.5) == 1.5
    assert py1.abszolut(0.0) == 0.0
    assert py1.abszolut(0.1) == 0.1
    assert py1.abszolut(-0.1) == 0.1
    