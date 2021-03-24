from classes import Player, Enemy
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
        Player('Jurek Ogorek', -1)


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

    player.set_lives(-1)

    assert player.get_lives() == 0


def test_enemy_creat():
    enemy = Enemy('Piekielny Demon')

    assert enemy.get_name() == 'Piekielny Demon'
    assert enemy.get_health() == 1


def test_enemy_creat_with_health():
    enemy = Enemy('Piekielny Demon', 4)

    assert enemy.get_name() == 'Piekielny Demon'
    assert enemy.get_health() == 4


def test_enemy_creat_with_negative_health():
    with pytest.raises(ValueError):
        Enemy('Piekielny Demon', -1)


def test_enemy_introduce():
    enemy = Enemy('Piekielny Demon', 3)

    assert enemy.info() == 'My name is Piekielny Demon. I have 3 health points left'

    enemy = Enemy('Piekielny Demon', 1)

    assert enemy.info() == 'My name is Piekielny Demon. I have 1 health point left'


def test_enemy_introduce_as_str():
    enemy = Enemy('Piekielny Demon', 3)

    assert str(enemy) == enemy.info()

    enemy = Enemy('Piekielny Demon', 1)

    assert str(enemy) == enemy.info()


def test_enemy_set_name():
    enemy = Enemy('Piekielny Demon')

    assert enemy.get_name() == 'Piekielny Demon'

    enemy.set_name('Lodowy Olbrzym')

    assert enemy.get_name() == 'Lodowy Olbrzym'


def test_enemy_set_name_empty():
    enemy = Enemy('Piekielny Demon')

    with pytest.raises(ValueError):
        enemy.set_name('')


def test_enemy_set_name_lowercase():
    enemy = Enemy('Piekielny Demon')

    assert enemy.get_name() == 'Piekielny Demon'

    enemy.set_name('LoDOwy OlBrZym')

    assert enemy.get_name() == 'Lodowy Olbrzym'


def test_enemy_set_health():
    enemy = Enemy('Piekielny Demon')

    assert enemy.get_health() == 1

    enemy.set_health(2)

    assert enemy.get_health() == 2


def test_enemy_set_health_zero():
    enemy = Enemy('Piekielny Demon')

    assert enemy.get_health() == 1

    enemy.set_health(0)

    assert enemy.get_health() == 0


def test_enemy_set_health_negative():
    enemy = Enemy('Piekielny Demon')

    assert enemy.get_health() == 1

    enemy.set_health(-1)

    assert enemy.get_health() == 0


def test_enemy_take_damage():
    enemy = Enemy('Piekielny Demon', 10)

    assert enemy.get_health() == 10

    enemy.take_damage(5)

    assert enemy.get_health() == 5


def test_enemy_take_lethal_damage():
    enemy = Enemy('Piekielny Demon', 10)

    assert enemy.get_health() == 10

    enemy.take_damage(12)

    assert enemy.get_health() == 0


def test_enemy_take_negative_damage():
    enemy = Enemy('Piekielny Demon', 10)

    with pytest.raises(ValueError):
        enemy.take_damage(-3)


def test_enemy_is_alive():
    enemy = Enemy('Piekielny Demon', 10)

    assert enemy.is_alive()


def test_enemy_is_not_alive():
    enemy = Enemy('Piekielny Demon', 10)
    enemy.take_damage(10)

    assert not (enemy.is_alive())
