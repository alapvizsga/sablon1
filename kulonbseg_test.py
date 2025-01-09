import py1
def test_kulonbseg():
    assert py1.kulonbseg(3, 2) == 1
    assert py1.kulonbseg(2, 3) == 1
    assert py1.kulonbseg(0, 0) == 0
    assert py1.kulonbseg(0, 1) == 1
    assert py1.kulonbseg(1, 0) == 1
    assert py1.kulonbseg(1, 1) == 0
    assert py1.kulonbseg(1, 2) == 1
    assert py1.kulonbseg(2, 1) == 1
    assert py1.kulonbseg(2, 2) == 0
    assert py1.kulonbseg(2, 4) == 2
    assert py1.kulonbseg(4, 2) == 2
    assert py1.kulonbseg(3, 3) == 0
    assert py1.kulonbseg(3, 4) == 1
    assert py1.kulonbseg(4, 3) == 1
    assert py1.kulonbseg(4, 4) == 0
    assert py1.kulonbseg(4, 5) == 1
    assert py1.kulonbseg(5, 4) == 1
    assert py1.kulonbseg(5, 5) == 0
    assert py1.kulonbseg(5, 6) == 1
    assert py1.kulonbseg(6, 5) == 1
    assert py1.kulonbseg(6, 6) == 0
    assert py1.kulonbseg(6, 7) == 1
    assert py1.kulonbseg(7, 6) == 1
    assert py1.kulonbseg(7, 7) == 0
    assert py1.kulonbseg(7, 8) == 1
    assert py1.kulonbseg(8, 7) == 1
  