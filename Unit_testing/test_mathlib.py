import pytest
from .mathlib import calc_mul,calc_sum,calc_square


def test_calc_sum():
    result=calc_sum(10,3)
    assert  result == 13

def test_calc_mul():
    r=calc_mul(10,3)
    assert  r==30

#use this when there is a similarity
@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (10, 100)
                         ]
                         )
def test_calc_square(test_input, expected_output):
    result = calc_square(test_input)
    assert result == expected_output

#custom markers
@pytest.mark.windows
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True

#run from terminal p.test -v
#custom markers pytest -m mac -v /pytest -m "not windows" -v