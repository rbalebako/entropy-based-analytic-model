"""Tests for Shannon entropy calculation."""

import math

import pytest

from entropy import shannon_entropy


def test_empty_dataset():
    assert shannon_entropy([]) == 0.0


def test_single_element():
    assert shannon_entropy([1]) == 0.0


def test_single_unique_value():
    assert shannon_entropy([42, 42, 42]) == 0.0


def test_two_equal_probabilities():
    # Two equally likely outcomes => entropy = 1 bit
    result = shannon_entropy([0, 1])
    assert math.isclose(result, 1.0)


def test_uniform_distribution():
    # Four equally likely outcomes => entropy = 2 bits
    data = [1, 2, 3, 4]
    result = shannon_entropy(data)
    assert math.isclose(result, 2.0)


def test_non_uniform_distribution():
    # p(0)=0.75, p(1)=0.25 => H = -(0.75*log2(0.75) + 0.25*log2(0.25))
    data = [0, 0, 0, 1]
    expected = -(0.75 * math.log2(0.75) + 0.25 * math.log2(0.25))
    result = shannon_entropy(data)
    assert math.isclose(result, expected)


def test_string_data():
    # Equal frequencies of 'a' and 'b' => 1 bit
    result = shannon_entropy(list("aabb"))
    assert math.isclose(result, 1.0)


def test_entropy_is_non_negative():
    data = [1, 1, 2, 3, 3, 3, 4]
    assert shannon_entropy(data) >= 0.0


def test_entropy_bounded_by_log2_unique_values():
    # Entropy <= log2(number of unique values)
    data = [1, 1, 2, 3, 4, 4]
    unique_values = len(set(data))
    assert shannon_entropy(data) <= math.log2(unique_values) + 1e-9
