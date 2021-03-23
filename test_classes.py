from classes import Player


def test_creat_player():
    player = Player('Jurek Ogorek')

    assert player.name == 'Jurek Ogorek'
    assert player.lives == 1


def test_creat_player_with_lives():
    jurek = Player('Jurek Ogorek', 4)

    assert jurek.name == 'Jurek Ogorek'
    assert jurek.lives == 4


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


def test_compare_players():
    jurek = Player('Jurek Ogorek')
    karolina = Player('Karolina Malina')

    assert not (jurek == karolina)
