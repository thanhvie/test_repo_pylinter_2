import app


def test_add():
    assert app.add(3, 4) == 7
    assert app.add(3.5, 4) == 7
    assert app.add(3.9, 4) == 7
    assert app.add(3.9, 4.1) == 8


def test_to_sentence():
    assert app.to_sentence('apple') == 'Apple.'
    assert app.to_sentence('Apple trees') == 'Apple trees.'
    assert app.to_sentence('Apple trees.') == 'Apple trees.'
