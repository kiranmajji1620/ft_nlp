from source import area

def test_square1():
    result = area.square(5)
    assert result == 25

def test_square2():
    result = area.square(9)
    assert result == 81

def test_square3():
    result = area.square(10)
    assert result == 100


# We like to check the outputs for different test cases.
# Combine all things into one

import pytest

@pytest.mark.parametrize("test_input, expected_output", 
                         [
                             (5, 25),
                             (9, 81),
                             (10, 100)
                         ])
def test_square(test_input, expected_output):
    result = area.square(test_input)
    assert result == expected_output

def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (5, 7, 12),
    (-2, 2, 0),
])
def test_addition(a, b, expected):
    assert add(a, b) == expected

# Without expected output
@pytest.mark.parametrize("a, b", [
    (2, 3),
    (5, 7),
    (2, 2),
])
def test_positive_numbers(a, b):
    assert a > 0
    assert b > 0

