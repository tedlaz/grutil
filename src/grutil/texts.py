def grup(text: str) -> str:
    """A function who returns the characters capitalized. Specal Greek characters are handled in order to make string comparisons"""
    uptext = text.upper()
    replaces = {
        "Ά": "Α",
        "Έ": "Ε",
        "Ή": "Η",
        "Ί": "Ι",
        "Ϊ": "Ι",
        "Ό": "Ο",
        "Ϋ": "Υ",
        "Ύ": "Υ",
        "Ώ": "Ω",
    }
    return "".join(replaces.get(letter, letter) for letter in uptext)
