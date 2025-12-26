import pytest

from Is_A_Palindrome import is_a_palindrome


@pytest.mark.parametrize(
    "text, expected",
    [
        ("racecar", True),
        ("RaceCar", True),
        ("never odd or even", True),
        ("Never Odd Or Even", True),
        ("a", True),
        ("", True),
        ("hello", False),
        ("python", False),
        ("Was it a rat I saw", False),  # punctuation not ignored yet
    ],
)
def test_is_palindrome_valid_strings(text, expected):
    assert is_a_palindrome(text) is expected


@pytest.mark.parametrize(
    "bad_input",
    [
        123,
        None,
        True,
        False,
        ["a", "b"],
        {"text": "racecar"},
        (1, 2, 1),
    ],
)
def test_is_palindrome_rejects_non_string_input(bad_input):
    with pytest.raises(TypeError):
        is_a_palindrome(bad_input)
