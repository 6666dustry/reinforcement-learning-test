from objects.paddle import Paddle
from objects.ball import Ball
import colors


class Game:
    def __init__(self, width, height):
        """
        ゲームの初期化とパラメータの設定を行うクラス

        Args:
            width (int): ゲームウィンドウの幅
            height (int): ゲームウィンドウの高さ
        """
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 60
        self.paddle_speed = 5
        self.ball_size = 10
        self.reset()

    def reset(self):
        """
        ゲームをリセットし、パドルとボールの初期位置を設定する
        """
        # パドルの初期位置
        paddle_y = self.height // 2 - self.paddle_height // 2
        # 左側のパドル
        self.paddle1 = Paddle(
            30, paddle_y, self.paddle_width, self.paddle_height, self.paddle_speed
        )
        # 右側のパドル
        self.paddle2 = Paddle(
            self.width - 30 - self.paddle_width,
            paddle_y,
            self.paddle_width,
            self.paddle_height,
            self.paddle_speed,
        )
        # ボールの初期位置
        ball_x = self.width // 2 - self.ball_size // 2
        ball_y = self.height // 2 - self.ball_size // 2
        # ボール
        self.ball = Ball(ball_x, ball_y)

    def update(self):
        """
        ゲームの状態を更新する
        """
        self.paddle1.move(self.height)
        self.paddle2.move(self.height)
        self.ball.move(self.width, self.height)
        self.check_collisions()
        self.check_out_of_bounds()

    def check_collisions(self):
        """
        パドルとボールの衝突をチェックし、反射させる
        """
        if self.ball.collides_with(self.paddle1) or self.ball.collides_with(
            self.paddle2
        ):
            self.ball.bounce_horizontal()

        if self.ball.hits_wall(self.height):
            self.ball.bounce_vertical()

    def check_out_of_bounds(self):
        """
        ボールが範囲外に出た場合、ゲームをリセットする
        """
        if self.ball.is_out_of_bounds(self.width):
            self.reset()

    def draw(self, screen):
        """
        ゲームの要素を描画する

        Args:
            screen (pygame.Surface): 描画対象のスクリーン
        """
        self.paddle1.draw(screen)
        self.paddle2.draw(screen)
        self.ball.draw(screen)

    def get_background_color(self):
        """
        ゲームの背景色を取得する

        Returns:
            tuple: RGB値で表される背景色。今は黒です。
        """
        return colors.BLACK
