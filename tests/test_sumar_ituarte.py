from funciones.sumar_ituarte import sumar_ituarte

def test_sumar_ituarte():
    assert sumar_ituarte(3, 5) == 8
    assert sumar_ituarte(-2, 2) == 0
