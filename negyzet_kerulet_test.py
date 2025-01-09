import py1
def test_negyzet_kerulet():
    assert py1.negyzet_kerulet(5) == 20
    assert py1.negyzet_kerulet(5.1) == 20.4
    assert py1.negyzet_kerulet(0) == 0
    assert py1.negyzet_kerulet(0.5) == 2
    
    