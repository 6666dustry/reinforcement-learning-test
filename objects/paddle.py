import pygame
import colors


class Paddle:
    def __init__(self, x, y, width, height, speed):
        """
        パドルクラスの初期化

        Args:
            x (int): パドルのx座標
            y (int): パドルのy座標
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self, screen_height):
        """
        パドルの移動を処理する

        Args:
            screen_height (int): ゲームスクリーンの高さ
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_s] and self.y < screen_height - self.height:
            self.y += self.speed

    def draw(self, screen):
        """
        パドルを描画する

        Args:
            screen (pygame.Surface): 描画対象のスクリーン
        """
        pygame.draw.rect(
            screen, colors.WHITE, (self.x, self.y, self.width, self.height)
        )
