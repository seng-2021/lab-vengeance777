#!/usr/bin/python
# -*- coding: utf-8

'''
Unit tests for mycrypt function. Basically ROT13, but also
capitalize or uncapitalize, and for numbers, replace with shifted
versions.

tr 'A-Za-z0-9=!"#€%&/()' 'n-za-mN-ZA-M=!"#€%&/()0-9'

If characters outside allowed ones are used as input, raise ValueError.
'''

import timeit
import pytest
import mycrypt


@pytest.mark.parametrize("test_input,expected", [
    ("a", "N"),
    ("b", "O"),
    ("abc", "NOP"),
    ("abc123", 'NOP!"#'),
    ("4", u'€')
])
def test_encode(test_input, expected):
    '''Verify that strings given above match the expected results'''
    assert(mycrypt.encode(test_input)) == expected


@pytest.mark.parametrize("test_input", [
    '123', '!"#','abc'])
def test_encode_decode(test_input):
    '''Verify that decoding an encoded string returns original string'''
    assert(mycrypt.decode(mycrypt.encode(test_input))) == test_input


@pytest.mark.parametrize("invalid_input", ['+','åäö'])
def test_invalid_char(invalid_input):
    '''Invalid characters should result in ValueError'''
    with pytest.raises(ValueError):
        mycrypt.encode(invalid_input)

@pytest.mark.parametrize("invalid_input", [])
def test_invalid_types(invalid_input):
    """Invalid parameter types should raise TypeError."""
    with pytest.raises(TypeError):
        mycrypt.encode(invalid_input)


def test_timing():
    '''Test whether encoding runs in approximately constant time, repetitions
    kept low to make test fast, use smallest measured time.

    Note: Tests like this need quite a bit of thought when used as a unit test,
    they are non-deterministic and might fail randomly.

    Hint: pad your string to max length and only return wanted length
    '''
    timing1 = min(timeit.repeat('mycrypt.encode("a")',
                                'import mycrypt', repeat=3, number=30))
    timing2 = min(timeit.repeat('mycrypt.encode("a"*1000)',
                                'import mycrypt', repeat=3, number=30))
    assert 0.95 * timing2 < timing1 < 1.05 * timing2

## Added tests and parametrizes

def test_encode_too_long():
    """Test that encoding a string longer than 1000 characters raises ValueError."""
    long_string = "a" * 1001
    with pytest.raises(ValueError):
        mycrypt.encode(long_string)

@pytest.mark.parametrize("test_input,expected", [
    ("", ""),  # Empty string
    ("A" * 1000, "N" * 1000),  # Exactly 1000 characters
])
def test_edge_cases(test_input, expected):
    """Verify edge cases for encoding."""
    assert mycrypt.encode(test_input) == expected

@pytest.mark.parametrize("invalid_input", ["abc123+", "abcåäö"])
def test_mixed_invalid_char(invalid_input):
    """Mixed valid and invalid characters should result in ValueError."""
    with pytest.raises(ValueError):
        mycrypt.encode(invalid_input)

# Combine tests for invalid types into one
@pytest.mark.parametrize("invalid_input", [None, 123, 5.5, [1, 2, 3], {"key": "value"}])
def test_invalid_type_cases(invalid_input):
    """Unified test to ensure invalid types raise TypeError."""
    with pytest.raises(TypeError):
        mycrypt.encode(invalid_input)

def test_encode_non_ascii_letter():
    """Verify that encoding non-ASCII alphabetic characters raises a ValueError."""
    with pytest.raises(ValueError):
        mycrypt.encode("å")

def test_coverage_for_empty_param():
    """Manually call encode() with None to verify that it raises a TypeError."""
    with pytest.raises(TypeError):
        mycrypt.encode(None)

@pytest.mark.parametrize("invalid_input", [None, 123, 5.5, [1, 2, 3], {"key": "value"}])
def test_invalid_types_wrapper(invalid_input):
    """Provide parameters to ensure test_invalid_types is covered."""
    test_invalid_types(invalid_input)  # Call the restricted function
