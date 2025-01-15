import py1
from unittest.mock import patch

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

def test_no_max_usage():
    # A max függvény átmeneti letiltása
    with patch("builtins.max", side_effect=RuntimeError("A max() függvény használata nem engedélyezett.")):
        try:
            py1.nagyobb(5, 3)  # Próbáljuk futtatni a függvényt
        except RuntimeError as e:
            pytest.fail(f"Nem engedélyezett függvény használata: {str(e)}")
