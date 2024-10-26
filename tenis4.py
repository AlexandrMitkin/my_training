import arcade
from arcade import draw_line, draw_text

# pipfrom arcade.examples.array_backed_grid import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong Game"


class Ball(arcade.Sprite):
    numder_bottom = 0
    numder_bar = 0

    def __init__(self):
        super().__init__("ball2.png", 0.3)
        self.change_x = 3
        self.change_y1 = 3
        self.change_y = self.change_y1

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.bottom < 1:
            Ball.numder_bottom += 1
            draw_text(text=str(Ball.numder_bottom), start_x=200, start_y=200, color=[255, 0, 0], )

        if self.right >= SCREEN_WIDTH or self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT or self.bottom <= 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    bar_x = 0

    def __init__(self):
        super().__init__("bar2.png", 0.4)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0
        Bar.bar_x = self.center_x


class Bar2(arcade.Sprite):
    def __init__(self):
        super().__init__("bar2.png", 0.4)

    def update(self):
        self.center_x = Bar.bar_x
        # self.center_x += self.change_x
        # if self.right >= SCREEN_WIDTH:
        #     self.right = SCREEN_WIDTH
        # if self.left<=0:
        #     self.left=0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.bar2 = Bar2()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.bar2.center_x = SCREEN_WIDTH / 2
        self.bar2.center_y = SCREEN_HEIGHT / 5 - 10
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        # self.bar2.draw()
        self.ball.draw()
        draw_text(text=str(Ball.numder_bottom), start_x=200, start_y=200, color=[155, 0, 0], )
        draw_text(text=str(Ball.numder_bar), start_x=200, start_y=150, color=[0, 155, 0], )

    def update(self, delta):
        if arcade.check_for_collision(self.bar2, self.ball):
            self.ball.change_y = -self.ball.change_y1
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = self.ball.change_y1
            Ball.numder_bar += 1
            draw_text(text=str(Ball.numder_bar), start_x=200, start_y=150, color=[0, 255, 0], )

        self.ball.update()
        self.bar.update()
        self.bar2.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.bar.change_x = -5
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.bar.change_x = 0


if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
