def is_palindrome(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    normalized = text.replace(" ", "").lower()
    return normalized == normalized[::-1]


print(is_palindrome("kajak"))