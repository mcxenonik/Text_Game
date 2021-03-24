class Player():
    """
    Class Player. Contains attributes:
    :param name: player's name
    :tupe name: str

    :param lives: player's lives left
    :type lives: int
    """
    def __init__(self, name, lives=1):
        if (not name):
            raise ValueError('Name cannot be empty')
        if (int(lives) < 0):
            raise ValueError('Lives cannot be negative')

        self._lives = int(lives)
        self._name = str(name)

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if (not new_name):
            raise ValueError('Name cannot be empty')

        self._name = str(new_name).title()

    def get_lives(self):
        return self._lives

    def set_lives(self, new_lives):
        self._lives = max(0, int(new_lives))

    def info(self):
        """
        Returns basic information about player.
        """
        lives = 'life' if (self._lives == 1) else 'lives'

        return f'My name is {self._name}. I have {self._lives} {lives} left'

    def __str__(self):
        return self.info()


class Enemy():
    """
    Class Enemy. Contains attributes:
    :param name: enemy's name
    :tupe name: str

    :param health: enemy's health left
    :type health: int
    """
    def __init__(self, name, health=1):
        if (not name):
            raise ValueError('Name cannot be empty')
        if (int(health) < 0):
            raise ValueError('Health cannot be negative')

        self._name = str(name)
        self._health = int(health)

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if (not new_name):
            raise ValueError('Name cannot be empty')

        self._name = str(new_name).title()

    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = max(0, int(new_health))

    def take_damage(self, damage):
        """
        Reduces health of enemy by damage.
        """
        if (int(damage) <= 0):
            raise ValueError('Damage cannot be zero or negative')

        self._health -= min(damage, self._health)

    def is_alive(self):
        """
        Checks if enemy is alive or not.
        """
        return self._health > 0

    def info(self):
        """
        Returns basic information about enemy.
        """
        points = 'point' if (self._health == 1) else 'points'

        return f'My name is {self._name}. I have {self._health} health {points} left'

    def __str__(self):
        return self.info()
