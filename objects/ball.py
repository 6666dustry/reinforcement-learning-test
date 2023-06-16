import pygame
import random
import colors


class Ball:
    def __init__(
        self,
        x,
        y,
    ):
        """
        ボールクラスの初期化

        Args:
            x (int): ボールのx座標
            y (int): ボールのy座標
        """
        self.x = x
        self.y = y
        self.size = 10
        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.choice([-2, 2])

    def move(self, screen_width, screen_height):
        """
        ボールの移動を処理する

        Args:
            screen_width (int): ゲームスクリーンの幅
            screen_height (int): ゲームスクリーンの高さ
        """
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce_horizontal(self):
        """
        ボールの水平方向の反射を処理する
        """
        self.speed_x = -self.speed_x

    def bounce_vertical(self):
        """
        ボールの垂直方向の反射を処理する
        """
        self.speed_y = -self.speed_y

    def collides_with(self, paddle):
        """
        ボールがパドルと衝突しているかを判定する

        Args:
            paddle (Paddle): 衝突を判定するパドルオブジェクト

        Returns:
            bool: ボールとパドルが衝突している場合はTrue、そうでない場合はFalse
        """

        return (
            self.x + self.size >= paddle.x
            and self.x <= paddle.x + paddle.width
            and self.y + self.size >= paddle.y
            and self.y <= paddle.y + paddle.height
        )

    def hits_wall(self, screen_height):
        """
        ボールが壁に衝突したかを判定する

        Args:
            screen_height (int): ゲームスクリーンの高さ

        Returns:
            bool: ボールが壁に衝突している場合はTrue、そうでない場合はFalse
        """
        return self.y <= 0 or self.y >= screen_height - self.size

    def is_out_of_bounds(self, screen_width):
        """
        ボールが範囲外に出たかを判定する

        Args:
            screen_width (int): ゲームスクリーンの幅

        Returns:
            bool: ボールが範囲外に出た場合はTrue、そうでない場合はFalse
        """
        return self.x <= 0 or self.x >= screen_width - self.size

    def draw(self, screen):
        """
        ボールを描画する

        Args:
            screen (pygame.Surface): 描画対象のスクリーン
        """
        pygame.draw.ellipse(
            screen, colors.WHITE, (self.x, self.y, self.size, self.size)
        )
