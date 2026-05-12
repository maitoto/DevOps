from app import saluer

def test_saluer_retourne_message():
    resultat = saluer("Mohamed Bellahcene")
    assert "Mohamed Bellahcene" in resultat
    assert "Bonjour" in resultat

def test_saluer_vide():
    resultat = saluer("")
    assert isinstance(resultat, str)