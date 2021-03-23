class Player():
    """
    Class Player. Contains attributes:
    :param name: player's name
    :tupe name: str

    :param lives: player's lives left
    :type lives: int
    """
    def __init__(self, name, lives=1):
        self.name = name
        self.lives = lives

    def info(self):
        """
        Returns basic information about player.
        """
        # if (self.lives == 1):
        #     return f'My name is {self.name}. I have 1 life left'
        # else:
        #     return f'My name is {self.name}. I have {self.lives} lives left'
        lives = 'life' if (self.lives == 1) else 'lives'

        return f'My name is {self.name}. I have {self.lives} {lives} left'

    def __str__(self):
        return self.info()
