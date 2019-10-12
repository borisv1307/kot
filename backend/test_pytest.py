import backend.int_dec  # The code to test


def test_increment():
    assert backend.int_dec.increment(3) == 4


def test_decrement():
    assert backend.int_dec.decrement(3) == 2
