from grutil.text import grup

def test_grup():
    assert grup("ΑΕΗΪΙΟΫΥΩ") == "ΑΕΗΪΙΟΫΥΩ"
    assert grup("δοκιμή") == "ΔΟΚΙΜΗ"
    assert grup("τα πάντα όλα") == "ΤΑ ΠΑΝΤΑ ΟΛΑ"