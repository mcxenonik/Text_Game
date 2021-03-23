from classes import Player
import pytest


def test_creat_player():
    player = Player('Jurek Ogorek')

    assert player.get_name() == 'Jurek Ogorek'
    assert player.get_lives() == 1


def test_creat_player_with_lives():
    player = Player('Jurek Ogorek', 4)

    assert player.get_name() == 'Jurek Ogorek'
    assert player.get_lives() == 4


def test_creat_player_with_negative_lives():
    with pytest.raises(ValueError):
        player = Player('Jurek Ogorek', -1)

    player = Player('Jurek Ogorek')

    assert player.get_lives() == 1


def test_introduce():
    player = Player('Jurek Ogorek', 3)

    assert player.info() == 'My name is Jurek Ogorek. I have 3 lives left'

    player = Player('Jurek Ogorek', 1)

    assert player.info() == 'My name is Jurek Ogorek. I have 1 life left'


def test_introduce_as_str():
    player = Player('Jurek Ogorek', 3)

    assert str(player) == player.info()

    player = Player('Jurek Ogorek', 1)

    assert str(player) == player.info()


def test_set_name():
    player = Player('Jurek Ogorek')

    assert player.get_name() == 'Jurek Ogorek'

    player.set_name('Karolina Malina')

    assert player.get_name() == 'Karolina Malina'


def test_set_name_empty():
    player = Player('Jurek Ogorek')

    with pytest.raises(ValueError):
        player.set_name('')


def test_set_name_lowercase():
    player = Player('Jurek Ogorek')

    assert player.get_name() == 'Jurek Ogorek'

    player.set_name('karOlIna maLINa')

    assert player.get_name() == 'Karolina Malina'


def test_set_lives():
    player = Player('Jurek Ogorek')

    assert player.get_lives() == 1

    player.set_lives(2)

    assert player.get_lives() == 2


def test_set_lives_zero():
    player = Player('Jurek Ogorek')

    assert player.get_lives() == 1

    player.set_lives(0)

    assert player.get_lives() == 0


def test_set_lives_negative():
    player = Player('Jurek Ogorek')

    assert player.get_lives() == 1

    with pytest.raises(ValueError):
        player.set_lives(-1)
