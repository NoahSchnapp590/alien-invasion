class GameStats():
    """Отслаживание статистики для игры Alien Invasion"""

    def __init__(self, settings):
        """Инициализирует статистику"""
        self.settings = settings
        self.reset_stats()
        self.game_active = False
    
    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходу игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0 