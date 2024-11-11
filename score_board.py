import pygame.font
from pygame.sprite import Group

from ship import Ship

class ScoreBoard():
    """Класс для вывода игровой информации"""
    def __init__(self, screen, settings, stats):
        """Инициализирует атрибуты подсчёта очков"""
        self.screen = screen 
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.stats = stats 

        # Настройки шрифта для вывода счёта
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка исходного изображения 
        self.prep_score()

    def prep_score(self):
        """Преобразует текущий счёт в графическое изображение"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, None)
        
        # Вывод счёта в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right + 1850
        self.score_rect.top = 20
    
    def show_score(self):
        """Выводит счёт на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        