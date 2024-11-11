class Settings():
    """Класс для хранения всех настроек"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Настройки корабля
        self.ship_speed = 1 
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # Настройки пришельцев 
        self.alien_speed = 0.9
        self.alien_points = 50
        self.fleet_drop_speed = 10
        self.fleet_direction = 1