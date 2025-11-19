import pytest

from grutil.texts import grup


@pytest.mark.parametrize(
    "input_text,expected_output",
    [
        ("Καλημέρα", "ΚΑΛΗΜΕΡΑ"),
        ("Καλησπέρα", "ΚΑΛΗΣΠΕΡΑ"),
        ("Καληνύχτα", "ΚΑΛΗΝΥΧΤΑ"),
        ("Άνθρωπος", "ΑΝΘΡΩΠΟΣ"),
        ("Ελλάδα", "ΕΛΛΑΔΑ"),
        ("Ήλιος", "ΗΛΙΟΣ"),
        ("Ίριδα", "ΙΡΙΔΑ"),
        ("Ϊκαρος", "ΙΚΑΡΟΣ"),
        ("Όμορφος", "ΟΜΟΡΦΟΣ"),
        ("Ύμνος", "ΥΜΝΟΣ"),
        ("Ϋδρογόνο", "ΥΔΡΟΓΟΝΟ"),
        ("Ώρα", "ΩΡΑ"),
        ("Δοϊράνη special", "ΔΟΙΡΑΝΗ SPECIAL"),
    ],
)
def test_grup(input_text, expected_output):
    assert grup(input_text) == expected_output
