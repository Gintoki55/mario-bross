import math
import time
import turtle
import random
import os
from itertools import product
# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(800, 600)
delay = 0.1
# 900, 600
wn.tracer(0)
# register for pip_L
turtle.register_shape("images/pip_L.gif")
# register for flags
turtle.register_shape("images/flag.gif")
turtle.register_shape("images/flag1.gif")
# register for clowds
turtle.register_shape("images/clowd.gif")
# register for  young_clowd
turtle.register_shape("images/young_clowd.gif")
# register for tress
turtle.register_shape("images/trees.gif")
# register for montain
turtle.register_shape("images/young_mon.gif")
turtle.register_shape("images/monTain.gif")
# register for coins
turtle.register_shape("images/coins.gif")
turtle.register_shape("images/coins2.gif")
turtle.register_shape("images/coins3.gif")
# mario character
turtle.register_shape("images/mario_jump1.gif")
turtle.register_shape("images/mario_jump.gif")
turtle.register_shape("images/mario_r1.gif")
#turtle.register_shape("images/mario_r2.gif")
turtle.register_shape("images/mario_r3.gif")
turtle.register_shape("images/mario_r4.gif")
turtle.register_shape("images/mario_r5.gif")
turtle.register_shape("images/mario_dead.gif")
turtle.register_shape("images/mario_l1.gif")
#turtle.register_shape("images/mario_l2.gif")
turtle.register_shape("images/mario_l3.gif")
turtle.register_shape("images/mario_l4.gif")
turtle.register_shape("images/mario_l5.gif")
# register for jumping wall
turtle.register_shape("images/jump.gif")
turtle.register_shape("images/jump3.gif")
# register for enemy turtle
turtle.register_shape("images/turtle_left1.gif")
turtle.register_shape("images/turtle_left2.gif")
turtle.register_shape("images/turtle_right1.gif")
turtle.register_shape("images/turtle_right2.gif")
turtle.register_shape("images/turtle.dead.gif")

# register for enemy movement
turtle.register_shape("images/enemy_left.gif")
turtle.register_shape("images/enemy_right.gif")
turtle.register_shape("images/enemy_dead.gif")
# register for keys
turtle.register_shape("images/killer.gif")
turtle.register_shape("images/killer2.gif")
# register for words
turtle.register_shape("images/words.gif")
turtle.register_shape("images/helper.gif")
# castle
turtle.register_shape("images/castle.gif")
# fire left and right turtle_register
turtle.register_shape("images/fire.left.gif")
turtle.register_shape("images/fire.right.gif")
# boss character turtle_register
turtle.register_shape("images/boss.gif")
turtle.register_shape("images/boss2.gif")
turtle.register_shape("images/boss3.gif")
turtle.register_shape("images/boss4.gif")
turtle.register_shape("images/boss.right.gif")
turtle.register_shape("images/boss2.right.gif")
turtle.register_shape("images/boss3.right.gif")
turtle.register_shape("images/boss4.right.gif")
# types
turtle.register_shape("images/kull.gif")
turtle.register_shape("images/pip.gif")
turtle.register_shape("images/firewater.gif")
turtle.register_shape("images/fire.down.gif")
turtle.register_shape("images/fire.gif")
turtle.register_shape("images/s6.gif")
turtle.register_shape("images/rrr.gif")
turtle.register_shape("images/glock.gif")



# pen for sprite and for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.playing = False

gravity = -0.5
gravity1 = -0.1
gravity3 = -1
jumping = False
camera_on = False

levels = [""]

level_1 = [
    "                    cccccccccccccccccccc        ",
    "                    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     ",
]


levels.append(level_1)




class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 1
        self.state = "splash"
        self.score = 0
        self.playing = False


    def start(self):
        self.state = "playing"

    def restart(self):
        player.goto(0, 300)
        player.is_alive = True
        player.direction = "right"
        game.playing = False


    def set_glock(self):
        # first one
        glocks.append (Glock (7505, 170, width=34, height=34))
        # 2 one
        glocks.append (Glock (7540, 210, width=34, height=34))
        glocks.append (Glock (7540, 170, width=34, height=34))

        # 3 one
        glocks.append (Glock (7575, 245, width=34, height=34))
        glocks.append (Glock (7575, 210, width=34, height=34))
        glocks.append (Glock (7575, 170, width=34, height=34))

        # 4 one
        glocks.append (Glock (7610, 280, width=34, height=34))
        glocks.append (Glock (7610, 245, width=34, height=34))
        glocks.append (Glock (7610, 210, width=34, height=34))
        glocks.append (Glock (7610, 170, width=34, height=34))

        # 5 one
        glocks.append (Glock (7645, 315, width=34, height=34))
        glocks.append(Glock(7645, 280, width=34, height=34))
        glocks.append(Glock(7645, 245, width=34, height=34))
        glocks.append(Glock(7645, 210, width=34, height=34))
        glocks.append(Glock(7645, 170, width=34, height=34))

        # 6 one
        glocks.append (Glock (7680, 350, width=34, height=34))
        glocks.append (Glock (7680, 315, width=34, height=34))
        glocks.append (Glock (7680, 280, width=34, height=34))
        glocks.append (Glock (7680, 245, width=34, height=34))
        glocks.append (Glock (7680, 210, width=34, height=34))
        glocks.append (Glock (7680, 170, width=34, height=34))

        # 7 one
        glocks.append (Glock (7715, 385, width=34, height=34))
        glocks.append (Glock (7715, 350, width=34, height=34))
        glocks.append (Glock (7715, 315, width=34, height=34))
        glocks.append (Glock (7715, 280, width=34, height=34))
        glocks.append (Glock (7715, 245, width=34, height=34))
        glocks.append (Glock (7715, 210, width=34, height=34))
        glocks.append (Glock (7715, 170, width=34, height=34))

        # 8 one

        glocks.append (Glock (7750, 420, width=34, height=34))
        glocks.append (Glock (7750, 385, width=34, height=34))
        glocks.append (Glock (7750, 350, width=34, height=34))
        glocks.append (Glock (7750, 315, width=34, height=34))
        glocks.append (Glock (7750, 280, width=34, height=34))
        glocks.append (Glock (7750, 245, width=34, height=34))
        glocks.append (Glock (7750, 210, width=34, height=34))
        glocks.append (Glock (7750, 170, width=34, height=34))

        # last one
        glocks.append (Glock (7785, 420, width=34, height=34))
        glocks.append (Glock (7785, 385, width=34, height=34))
        glocks.append (Glock (7785, 350, width=34, height=34))
        glocks.append (Glock (7785, 315, width=34, height=34))
        glocks.append (Glock (7785, 280, width=34, height=34))
        glocks.append (Glock (7785, 245, width=34, height=34))
        glocks.append (Glock (7785, 210, width=34, height=34))
        glocks.append (Glock (7785, 170, width=34, height=34))

    def set_lavas(self):
        # lave objects
        lavas.append(Block(3600, -200, width=3800, height=300))
        real_lavas.append(Block(2900, -50, 50, 50))
        real_lavas.append(Block(3020, -50, 50, 50))
        real_lavas.append(Block(3130, -50, 50, 50))
        real_lavas.append(Block(3230, -50, 50, 50))
        real_lavas.append(Block(3330, -50, 50, 50))
        real_lavas.append(Block(3430, -50, 50, 50))
        real_lavas.append(Block(3530, -50, 50, 50))
        real_lavas.append(Block(3630, -50, 50, 50))
        real_lavas.append(Block(3730, -50, 50, 50))
        real_lavas.append(Block(3830, -50, 50, 50))
        real_lavas.append(Block(3930, -50, 50, 50))
        real_lavas.append(Block(4030, -50, 50, 50))
        real_lavas.append(Block(4130, -50, 50, 50))
        real_lavas.append(Block(4230, -50, 50, 50))
        real_lavas.append(Block(4330, -50, 50, 50))
        real_lavas.append(Block(4430, -50, 50, 50))
        real_lavas.append(Block(4530, -50, 50, 50))
        real_lavas.append(Block(4630, -50, 50, 50))
        real_lavas.append(Block(4730, -50, 50, 50))
        real_lavas.append(Block(4830, -50, 50, 50))
        real_lavas.append(Block(4930, -50, 50, 50))
        real_lavas.append(Block(5030, -50, 50, 50))
        real_lavas.append(Block(5130, -50, 50, 50))
        real_lavas.append(Block(5230, -50, 50, 50))
        # lava objects part 2
        lavas.append(Block(5330, -200, width=3800, height=300))
        real_lavas.append(Block(5560, -50, 50, 50))
        real_lavas.append(Block(5680, -50, 50, 50))
        real_lavas.append(Block(5770, -50, 50, 50))
        real_lavas.append(Block(5870, -50, 50, 50))
        real_lavas.append(Block(5970, -50, 50, 50))
        real_lavas.append(Block(6070, -50, 50, 50))
        real_lavas.append(Block(6170, -50, 50, 50))
        real_lavas.append(Block(6270, -50, 50, 50))
        real_lavas.append(Block(6370, -50, 50, 50))
        real_lavas.append(Block(6470, -50, 50, 50))
        real_lavas.append(Block(6570, -50, 50, 50))

    def set_fireball(self):
        # flat objects
        hold_objects.append(Holding(3500, 500, 10, 0.1))
        flats.append(Flat(3500, -100, 34, 34))
        hold_objects.append(Holding(3500, -200, 10, 0.1))

        hold_objects.append(Holding(4400, 500, 10, 0.1))
        flats.append(Flat(4400, 400, 34, 34))
        hold_objects.append(Holding(4400, -200, 10, 0.1))

        hold_objects.append(Holding(5000, 500, 10, 0.1))
        flats.append(Flat(5000, 400, 34, 34))
        hold_objects.append(Holding(5000, -200, 10, 0.1))

        hold_objects.append(Holding(5150, 500, 10, 0.1))
        flats.append(Flat(5150, -100, 34, 34))
        hold_objects.append(Holding(5150, -200, 10, 0.1))


class Sprite():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dx = 1
        self.dy = 1
        self.friction = 0.7
        self.playing = True

    def is_close(self, other):
        a = self.x - other.x
        b = self.y - other.y
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 30:
            return True
        else:
            return False
    def collision_hulk(self, other):
        # player is above
        if self.y < other.y:
            self.dy = 0
            self.y = other.y - other.height / 2 - self.height / 2

        # player is below
        elif self.y > other.y:
            self.dy = 0
            self.y = other.y + other.height / 2 + self.height / 2

    def collision(self, other):
        # player to left
        if self.x < other.x - other.width / 2 and self.dx > 0:
            self.dx = 0
            self.x = other.x - other.width / 2 - self.width / 2

        # player to right
        elif self.x > other.x + other.width / 2 and self.dx < 0:
            self.dx = 0
            self.x = other.x + other.width / 2 + self.width / 2

            # player is above
        elif self.y > other.y:
            self.dy = 0
            self.y = other.y + other.height / 2 + self.height / 2

        # player is below
        elif self.y < other.y:
            self.dy = 0
            self.y = other.y - other.height / 2 - self.height / 2


    def setup_border(self, level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                screen_x = 2150 + (x * 34)
                screen_y = 200 - (y * 34)
                character = level[y][x]

                if character == "c":
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    screen_x = 3000 + (x * 33)
                    screen_y = 250 - (y * 33)
                    blocks_A.append(Block_Air(screen_x, screen_y, 33, 33))

                if character == "A":
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    screen_x = 4900 + (x * 33)
                    screen_y = 168 - (y * 33)
                    Cracks.append(Cracked_wall(screen_x, screen_y, 33, 33))

    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("square")
        pen.color("grey")  # Set the color to brown
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()

    def goto(self, x, y):
        self.x = x
        self.y = y

    def is_aabb_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return x_collision and y_collision


class Player(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.direction = "stop"       
        self.gold = 0
        self.score = 0
        self.frame = 0
        self.frames_left = ["images/mario_l3.gif", "images/mario_l4.gif", "images/mario_l5.gif", "images/mario_l4.gif"]
        self.frames_right = ["images/mario_r3.gif", "images/mario_r4.gif", "images/mario_r5.gif", "images/mario_r4.gif"]
        self.is_alive = True
        self.timer = 0
        self.start_timer = False
        self.playing = False
    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)


        if self.direction == "stop":
            self.dx = 0
            pen.shape("images/mario_l1.gif")

        elif self.direction == "left":
            pen.shape("images/mario_l1.gif")  
            player.animation22()


        elif self.direction == "right":
            pen.shape("images/mario_r1.gif")
            player.animation()


        elif self.direction == "up":
            pen.shape("images/mario_jump.gif")

        elif self.direction == "down":
            pen.shape("images/mario_dead.gif")

        else:
            pen.shape("images/mario_r1.gif")

        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()


    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += gravity

    def jump(self):
        if player.is_alive:
            self.direction = "up"
            os.system("afplay sounds/smb_jump-super.wav&")
            global jumping
            jumping = True
            if jumping and player.y < 300:
                self.dy += 9
                if self.dy > 10:
                    self.dy = 10

            elif player.x > 7450 and player.y < 400:
                self.dy += 9
                if self.dy > 10:
                    self.dy = 10
            else:
                if jumping and player.y < 0:
                    self.dy = 0


    def left(self):
        if player.is_alive:
            self.direction = "left"
            self.dx -= 3
            if self.dx < -10:
                self.dx = -10
            self.frame += 1


    def right(self):
        if player.is_alive:
            self.direction = "right"
            self.dx += 3
            if self.dx > 10:
                self.dx = 10
            self.frame += 1

    def move(self):
        self.direction = "right"
        self.dx += 2
        if self.dx > 5:
            self.dx = 5
        self.frame += 1



    def player_dead_by_enemy(self):
        if not game.playing:
            os.system("afplay sounds/smb_mariodie.wav&")
            game.playing = True
        self.direction = "down"
        print("you dead")
        player.is_alive = False
        player.start_timer = True



    def restart(self):
        player.goto(0, 100)
        player.is_alive = True
        player.direction = "right"
        self.start_timer = False
        game.playing = False
        Cracked_wall.playing = False
        PIP_L.playing = False
        Key.playing = False
        Flag.playing = False
        player.playing = False


        player.gold = 0
        enemies.clear()
        enemies2.clear()
        # enemies
        enemies.append(Enemy2(700, 70, 24, 24))
        enemies.append(Enemy2(560, 70, 24, 24))

        # enemies2
        enemies2.append(Enemy3(2000, 130, 24, 24))
        enemies2.append(Enemy3(2300, 130, 24, 24))
        # enemy animation

        for smart in enemies2:
            smart.animation1()
        for enemy in enemies:
            enemy.animation()




    def animation(self):
        if self.frame >= len(self.frames_right):
            self.frame = 0
        pen.shape(self.frames_right[self.frame])


    def animation22(self):
        if self.frame >= len(self.frames_left):
            self.frame = 0
        pen.shape(self.frames_left[self.frame])




    def time(self):
        if self.start_timer:
            self.timer += 1
            if self.timer > 20:
                self.timer = 0
                player.restart()



class Block(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = False

    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.color("#B7410E")
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.shape("images/rrr.gif")
        pen.shape("square")
        pen.stamp()

    def render_0(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.color("green")
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.shape("images/firewater.gif")
        pen.stamp()



class Block_Air(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = False


    def render_Block_Air(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.color("pink")
        pen.shape("images/rrr.gif")
        pen.stamp()

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += gravity

    def jump(self):
        self.dy += 4
        if self.dy > 4:
            self.dy = 4

class Jumping_wall(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.frame = 0
        self.frames = ["images/jump.gif", "images/jump3.gif"]
        self.playing = False

    def render_jumping_wall(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.color("red")
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.shape(self.frames[self.frame])
        pen.stamp()


class Cracked_wall(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = False

    def render_cracked_wall(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.color("green")
        pen.shape("images/kull.gif")
        pen.shapesize(self.height / 20, self.width / 20)
        pen.stamp()



class Glock(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = True

    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        #pen.shape("square")
        pen.shape("images/glock.gif")
        pen.color("blue")
        pen.stamp()


class Coins(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.frame = 0
        self.frames = ["images/coins.gif", "images/coins2.gif", "images/coins3.gif", ]
        self.playing = True
    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape(self.frames[self.frame])
        pen.color("gold")
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()



    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += gravity

    def jump(self):
        self.dy += 4
        if self.dy > 4:
            self.dy = 4

    def animation(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        # Assuming 'pen' and 'wn' are globally accessible
        pen.shape(self.frames[self.frame])
        wn.ontimer(self.animation, 250)

class Pip(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = True

    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("images/pip.gif")
        pen.color("red")
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()



class Flat(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.frame = 0
        self.frames = ["images/fire.down.gif", "images/fire.gif"]
        self.shape_changed = False
        self.playing = True

    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape(self.frames[self.frame])
        pen.color("grey")
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += gravity1

    def jump(self):
        self.dy += 12
        if self.dy > 12:
            self.dy = 12

class Words(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.playing = True

    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("images/words.gif")
        pen.color("white")
        pen.stamp()

    def render_1(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("images/helper.gif")
        pen.color("white")
        pen.stamp()

    def render_2(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.hideturtle()
        pen.color("white")
        pen.clear()
        pen.shape("square")
        pen.write("Boss is Not Having a good day ", font=("Trebuchet MS", 24, "normal"))
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()


class Montain(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = True

    def render_b(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("images/monTain.gif")
        pen.stamp()

    def render_d(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("images/young_mon.gif")
        pen.stamp()


class Key(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.frame = 0
        self.frames = ["images/killer.gif", "images/killer2.gif"]
        self.playing = False
    def render_99(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape(self.frames[self.frame])
        pen.color("blue")
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()

    def animation(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        pen.shape(self.frames[self.frame])
        wn.ontimer(self.animation, 300)


class Tress(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = True

    def render_p(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("images/trees.gif")
        pen.stamp()



class Clowds(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = True

    def render_c(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("images/young_clowd.gif")
        pen.stamp()

    def render_A(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("images/clowd.gif")
        pen.stamp()


class Castle(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = True

    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("images/castle.gif")

        pen.stamp()


class PIP_L(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = False

    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("square")
        pen.color("yellow")
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.shape("images/pip_L.gif")
        pen.stamp()


class Flag1(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = True

    def render_flag1(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("images/flag1.gif")
        pen.stamp()

class Flag(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = False

    def render_flag(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("images/flag.gif")
        pen.stamp()

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += gravity

    def move_flag(self):
        flag.dy += 17
        if flag.dy > 17:
            flag.dy = 17





class Holding(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.playing = True

    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape("square")
        pen.color("black")
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()


class Enemy(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.direction = ""
        self.frame = 0
        self.left_animation_frames = ["images/boss.gif", "images/boss2.gif", "images/boss3.gif", "images/boss4.gif"]
        self.right_animation_frames = ["images/boss.right.gif", "images/boss2.right.gif", "images/boss3.right.gif", "images/boss4.right.gif"]
        self.playing = False

    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)

        if self.is_close(player):
            if player.x < self.x:
                self.direction = "left"
                pen.shape(self.left_animation_frames[self.frame])

            else:
                self.direction = "right"
                pen.shape(self.right_animation_frames[self.frame])

        else:
            pen.shape(self.left_animation_frames[self.frame])

        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()

    def animation(self):
        self.frame += 1
        if self.frame >= len(self.left_animation_frames):
            self.frame = 0
        pen.shape(self.left_animation_frames[self.frame])
        wn.ontimer(self.animation, 500)

    def is_close(self, other):
        a = self.x - other.x
        b = self.y - other.y
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 650:
            return True
        else:
            return False

    def is_close2(self, other):
        a = self.x - other.x
        b = self.y - other.y
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 250:
            return True
        else:
            return False

    def move3(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += gravity1


        if fighter1.is_close(player):
            missile.bulletstate = "fire"
            if player.x < self.x:
                self.direction = "left"
                if self.direction == "left":
                    self.dx -= 0.3
                    if self.dx < -1.5:
                        self.dx = -1.5
                    missile.direction = "left"

            elif player.x < self.x + 50 or player.y > self.y + 100:
                missile.goto(self.x, self.y)
                missile.bulletstate = "ready"
                missile.hidden = True



            elif player.x > fighter1.x:
                if self.direction == "right":
                    self.dx += 0.3
                    if self.dx > 1.5:
                        self.dx = 1.5
                    missile.direction = "right"




class Enemy2(Enemy):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.direction = ""
        self.frame = 0
        self.frames = ["images/enemy_left.gif", "images/enemy_right.gif"]
        self.timer = 0
        self.start_timer = False
        self.playing = True
    def render_normal(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)

        if self.direction == "stop":
            pen.shape("images/enemy_dead.gif")

        else:
            pen.shape(self.frames[self.frame])

        pen.color("red")
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()

    def animation(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        pen.shape(self.frames[self.frame])
        wn.ontimer(self.animation, 400)


    def update(self):
        if self.direction != "stop":
            self.x += self.dx
            self.y += self.dy
            self.dy += gravity1
            self.dx -= 0.2
            if self.dx < -2:
                self.dx = 2

    def time(self):
        if self.start_timer:
            self.timer += 1
            if self.timer > 20:
                self.timer = 0
                self.goto(1000, 1000)


    def enemy_killed_by_player(self):
        enemy.start_timer = True
        os.system("afplay sounds/smb_stomp.wav&")
        print("you really did!!!")
        enemy.direction = "stop"
        player.dy += 5
        if player.dy > 5:
            player.dy = 5
        player.gold += 10
        print(player.gold)




class Enemy3(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.direction = random.choice(["left", "right"])
        self.frame = 0
        self.left_frames = ["images/turtle_left2.gif", "images/turtle_left1.gif"]
        self.right_frames = ["images/turtle_right2.gif", "images/turtle_right1.gif"]
        self.timer = 0
        self.start_timer = False
        self.playing = True
    def render_smart(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x - x_offset, self.y - y_offset)

        if self.direction == "left":
            pen.shape(self.left_frames[self.frame])

        elif self.direction == "right":
            pen.shape(self.right_frames[self.frame])

        elif self.direction == "stop":
            pen.shape("images/turtle.dead.gif")


        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()


    def move2(self):
        if self.direction != "stop":
            self.x += self.dx
            self.y += self.dy
            self.dy += gravity1
            if self.direction == "left":
                self.dx -= 0.2
                if self.dx < -2:
                    self.dx = -2
            elif self.direction == "right":
                self.dx += 0.2
                if self.dx > 2:
                    self.dx = 2
            else:
                self.direction = "stop"

    def animation1(self):
        self.frame += 1
        if self.frame >= len(self.left_frames):
            self.frame = 0
        pen.shape(self.left_frames[self.frame])
        wn.ontimer(self.animation1, 500)

    def time(self):
        if self.start_timer:
            self.timer += 1
            if self.timer > 20:
                self.timer = 0
                self.goto(1000, 1000)

    def smart_killed_by_player(self):
        smart.start_timer = True
        os.system("afplay sounds/smb_kick.wav&")
        print("you really did!!!")
        smart.direction = "stop"
        player.dy += 5
        if player.dy > 5:
            player.dy = 5
        player.gold += 10
        print(player.gold)

class Missile(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.direction = "stop"
        self.bulletstate = "ready"
        self.frame = 0
        self.frames = ["images/fire.left.gif", "images/fire.right.gif"]
        self.hidden = False
        self.timer = 0
        self.start_timer = False
        self.playing = False


    def render(self, pen, x_offset, y_offset):
        pen.penup()
        pen.goto(self.x + 15 - x_offset, self.y + 20 - y_offset)
        pen.shape(self.frames[self.frame])
        pen.color("blue")
        pen.shapesize(self.height / 20, self.width / 20)  # Set the size of the square
        pen.stamp()


    def move(self):
        if self.direction == "left":
            self.frame = 0
            self.dx -= 1
            if self.dx < -6:
                self.dx = -6

        elif self.direction == "right":
            self.frame = 1
            self.dx += 1
            if self.dx > 6:
                self.dx = 6



    def time(self):
        if self.start_timer:
            self.timer += 1
            if self.timer > 1:
                self.timer = 0
                self.goto(1000, 1000)



class Camera():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        if camera_on:
            self.x = x
            self.y = y

# lists
blocks = []
blocks_A = []
walls = []
Cracks = []
glocks = []
coins = []
pips = []
hold_objects = []
lavas = []
real_lavas = []
flats = []
missiles = []
words = []
helper = []
jj = []
keys = []
young_mon = []
monTain = []
trees = []
clowds = []
young_clowds = []
enemies = []
enemies2 = []
flags = []
flags1 = []
pip11 = []
# objects
player = Player(3600, 300, 24, 55)
player.setup_border(level_1)
# enemy objects

# boss
fighter1 = Enemy(6400, 200, 40, 60)
enemies3 = [fighter1]
fighter1.animation()

# enemies
enemies.append(Enemy2(700, 70, 24, 24))
enemies.append(Enemy2(560, 70, 24, 24))

# enemies2
enemies2.append(Enemy3(2000, 130, 24, 24))
enemies2.append(Enemy3(2300, 130, 24, 24))
# enemy animation

for smart in enemies2:
    smart.animation1()
for enemy in enemies:
    enemy.animation()

# missile objects
missile = Missile(fighter1.x, fighter1.y, 12, 12)
missiles.append(missile)

# game objects
game = Game(0, 0)
game.set_glock()
game.set_lavas()
game.set_fireball()

# castle
blocks.append(Castle(8600, 335, 34, 34))
flags1.append(Flag1(8050, 330, 24, 24))
flags.append(Flag(8030, 250, 34, 34))
hold_objects.append(Holding(8030, 200, 30, 0.1))
hold_objects.append(Holding(8030, 500, 30, 0.1))
# keys objects
keys.append(Key(6650, 170, 24, 24))
for key in keys:
    key.animation()
# words
words.append(Words(8260, 530, 24, 24))
helper.append(Words(5300, 175, 24, 24))
helper.append(Words(8470, 370, 24, 24))
jj.append(Words(5200, 270, 0.1, 0.1))


# blocks objects
blocks.append(Sprite(200, -150, width=1500, height=400))
blocks.append(Sprite(2000, -150, width=1700, height=400))

blocks.append(Sprite(5400, -100, width=250, height=500))
blocks.append(Sprite(5400, 700, width=250, height=500))

blocks.append(Sprite(7600, -101, width=2000, height=500))
blocks.append(Sprite(8900, -101, width=2000, height=500))

# block_L objects
pip11.append(PIP_L(9060, 215, width=100, height=34))
# blocks_air objects
blocks_A.append(Block_Air(525, 220, 34, 34))
blocks_A.append(Block_Air(600, 220, 34, 34))
blocks_A.append(Block_Air(675, 220, 34, 34))

# coins objects
coins.append(Coins(563, 220, 34, 31))
coins.append(Coins(600, 350, 34, 31))
coins.append(Coins(638, 220, 34, 31))


for coin in coins:
    coin.animation()
# hold objects
hold_objects.append(Holding(525, 203, 10, 0.1))
hold_objects.append(Holding(563, 205, 10, 0.1))
hold_objects.append(Holding(600, 203, 10, 0.1))
hold_objects.append(Holding(638, 205, 10, 0.1))
hold_objects.append(Holding(675, 204, 10, 0.1))
hold_objects.append(Holding(600, 320, 10, 0.1))
hold_objects.append(Holding(3970, 240, 700, 0.1))

# jumping_wall objects
walls.append(Jumping_wall(3000, 100, 60, 24))
walls.append(Jumping_wall(3200, 150, 60, 24))
walls.append(Jumping_wall(3400, 200, 60, 24))
walls.append(Jumping_wall(4500, 250, 60, 24))
walls.append(Jumping_wall(4700, 200, 60, 24))
walls.append(Jumping_wall(4900, 150, 60, 24))

# pips objects
pips.append(Pip(1400, 120, 60, 137))
pips.append(Pip(1800, 120, 60, 137))
pips.append(Pip(2500, 120, 60, 137))
pips.append(Pip(7000, 220, 60, 137))

# monTain
monTain.append(Montain(-250, 90, 24, 24))
monTain.append(Montain(800, 90, 24, 24))
monTain.append(Montain(2200, 90, 24, 24))

# young_mon
young_mon.append(Montain(100, 70, 24, 24))
young_mon.append(Montain(700, 70, 24, 24))
young_mon.append(Montain(2200, 70, 24, 24))

# trees
trees.append(Tress(-450, 70, 24, 24))
trees.append(Tress(350, 70, 24, 24))
trees.append(Tress(1600, 70, 24, 24))


# young_clowds
young_clowds.append(Clowds(-200, 370, 24, 24))
young_clowds.append(Clowds(-70, 390, 24, 24))
young_clowds.append(Clowds(1000, 390, 24, 24))
young_clowds.append(Clowds(1100, 370, 24, 24))
young_clowds.append(Clowds(2100, 390, 24, 24))
young_clowds.append(Clowds(2200, 370, 24, 24))


# double clowds
clowds.append(Clowds(1700, 500, 24, 24))
clowds.append(Clowds(1760, 500, 24, 24))

# clowds

clowds.append(Clowds(100, 500, 24, 24))
clowds.append(Clowds(700, 500, 24, 24))
clowds.append(Clowds(2900, 500, 24, 24))

# camera objects
camera = Camera(player.x, player.y)


wn.listen()


wn.onkeypress(player.right, "Right")
wn.onkeypress(player.left, "Left")
wn.onkeypress(player.jump, "space")
wn.onkeypress(game.start, "s")
wn.onkeypress(game.start, "S")



while True:
    pen.clear()
    if game.state == "splash":
        pen = turtle.Turtle()
        pen.shape("images/s6.gif")
        pen.penup()
        pen.goto(-10, 0)
        pen.stamp()
        pen.hideturtle()
        wn.update()
    elif game.state == "playing":
        for j in jj:
            j.render_2(pen, camera.x, camera.y)


        for flag in flags:
            flag.render_flag(pen, camera.x, camera.y)
            flag.update()


        for flag1 in flags1:
            flag1.render_flag1(pen, camera.x, camera.y)

        for young in young_clowds:
            young.render_c(pen, camera.x, camera.y)
        for big in clowds:
            big.render_A(pen, camera.x, camera.y)

        for t in trees:
            t.render_p(pen, camera.x, camera.y)

        for y in young_mon:
            y.render_d(pen, camera.x, camera.y)

        for m in monTain:
            m.render_b(pen, camera.x, camera.y)

        for key in keys:
            key.render_99(pen, camera.x, camera.y)

        for help in helper:
            help.render_1(pen, camera.x, camera.y)

        for word in words:
            word.render(pen, camera.x, camera.y)


        for flat in flats:
            flat.update()
            flat.render(pen, camera.x, camera.y)

        for lava in real_lavas:
            lava.render_0(pen, camera.x, camera.y)

        for lava in lavas:
            lava.render(pen, camera.x, camera.y)

        for pip in pips:
            pip.render(pen, camera.x, camera.y)

        for hold in hold_objects:
            hold.render(pen, camera.x, camera.y)

        for coin in coins:
            coin.render(pen, camera.x, camera.y)

        for glock in glocks:
            glock.render(pen, camera.x, camera.y)

        for crack in Cracks:
            crack.render_cracked_wall(pen, camera.x, camera.y)


        for wall in walls:
            wall.render_jumping_wall(pen, camera.x, camera.y)

        for air in blocks_A:
            air.render_Block_Air(pen, camera.x, camera.y)

        for block in blocks:
            block.render(pen, camera.x, camera.y)


    # setting for player
        player.render(pen, camera.x, camera.y)
        player.update()
        player.time()

        for p_L in pip11:
            p_L.render(pen, camera.x, camera.y)
            if player.is_aabb_collision(p_L):
                if not p_L.playing:
                    os.system("afplay sounds/smb_pipe.wav&")
                    p_L.playing = True



    # active the method of collision
        for block in blocks:
            if player.is_aabb_collision(block):
                player.dx *= player.friction
                player.collision(block)

        for air in blocks_A:
            air.update()
            if player.is_aabb_collision(air):
                player.dx *= player.friction
                player.collision_hulk(air)
                if player.y < air.y:
                    player.dy = 0
                    player.y = air.y - air.height / 2 - player.height / 2
                    air.jump()
                    os.system("afplay sounds/smb_bump.wav&")


        for wall in walls:
            if player.is_aabb_collision(wall):
                player.dx *= player.friction
                player.collision(wall)
                player.dy += 20
                wall.frame = 1
            else:
                wall.frame = 0

        for crack in Cracks:
            if player.is_aabb_collision(crack):
                player.dx *= player.friction
                player.collision_hulk(crack)

        for glock in glocks:
            if player.is_aabb_collision(glock):
                player.dx *= player.friction
                player.collision(glock)

        for coin in coins:
            coin.update()
            if player.is_aabb_collision(coin):
                player.collision(coin)
                player.dx *= player.friction
                if player.y < coin.y:
                    player.dy = 0
                    player.y = coin.y - coin.height / 2 - player.height / 2
                    coin.jump()
                    os.system("afplay sounds/smb_coin.wav&")
                    player.gold += 10
                    print(player.gold)

            for hold in hold_objects:
                for flag in flags:
                    if flag.is_aabb_collision(hold):
                        flag.collision(hold)
                    if player.is_aabb_collision(flag):
                        player.collision(flag)
                        flag.move_flag()
                        if not flag.playing:
                            os.system("afplay sounds/smb_flagpole.wav&")
                            flag.playing = True


            for hold in hold_objects:
                if coin.is_aabb_collision(hold):
                    coin.collision(hold)

            for hold in hold_objects:
                for block_air in blocks_A:
                    if block_air.is_aabb_collision(hold):
                        block_air.collision(hold)

        for pip in pips:
            if player.is_aabb_collision(pip):
                player.dx *= player.friction
                player.collision(pip)

        for hold in hold_objects:
            for flat in flats:
                if flat.is_aabb_collision(hold):
                    flat.collision(hold)
                    if flat.y > hold.y:
                        flat.dy = 0
                        flat.y = hold.y + hold.height / 2 + flat.height / 2
                        flat.jump()
                    flat.frame += 1
                    if flat.frame >= len(flat.frames):
                        flat.frame = 0
                    pen.shape(flat.frames[flat.frame])

        fighter1.render(pen, camera.x, camera.y)
        fighter1.move3()
        for crack in Cracks:
            if fighter1.is_aabb_collision(crack):
                fighter1.dx *= fighter1.friction
                fighter1.collision_hulk(crack)
                if fighter1.is_close2(player):
                    fighter1.dy += 4
                    if fighter1.dy > 4:
                        fighter1.dy = 4

        for missile in missiles:
            if not missile.hidden:
                missile.render(pen, camera.x, camera.y)
                missile.time()
            missile.move()

        if missile.bulletstate == "fire":
            if not fighter1.playing:
                os.system("afplay sounds/smb_bowserfire.wav&")
                fighter1.playing = True
            missile.hidden = False
            missile.x += missile.dx
            missile.y += missile.dy
        elif missile.bulletstate == "ready":
            fighter1.playing = False
            missile.hidden = True
            missile.x = fighter1.x
            missile.y = fighter1.y

        if missile.x > 6600:
            fighter1.playing = False
            missile.goto(fighter1.x, fighter1.y)
            missile.bulletstate = "ready"
        elif missile.x < 5400:
            fighter1.playing = False
            missile.goto(fighter1.x, fighter1.y)
            missile.bulletstate = "ready"

        for smart in enemies2:
            smart.render_smart(pen, camera.x, camera.y)
            smart.move2()
            smart.time()

            for block in blocks:
                if smart.is_aabb_collision(block):
                    smart.dx *= smart.friction
                    smart.collision(block)

            for pip in pips:
                if smart.is_aabb_collision(pip):
                    smart.collision(pip)
                    smart.direction = random.choice(["left", "right"])

        for enemy in enemies:
            enemy.render_normal(pen, camera.x, camera.y)
            enemy.update()
            enemy.time()
            for block in blocks:
                if enemy.is_aabb_collision(block):
                    enemy.collision(block)
                    enemy.dx *= enemy.friction
            if player.is_close(enemy):
                player.collision(enemy)
                player.player_dead_by_enemy()

            elif player.is_aabb_collision(enemy):
                player.collision_hulk(enemy)
                enemy.enemy_killed_by_player()

        for smart in enemies2:
            if player.is_close(smart):
                player.collision(smart)
                player.player_dead_by_enemy()

            elif player.is_aabb_collision(smart):
                player.collision_hulk(smart)
                smart.smart_killed_by_player()


        for fighter in enemies3:
            if player.is_close(fighter):
                player.collision(fighter)
                player.player_dead_by_enemy()

        for fighter in enemies3:
            for key in keys:
                for crack in Cracks:
                    if player.is_aabb_collision(key):
                        if not key.playing:
                            os.system("afplay sounds/smb_bowserfalls.wav&")
                            key.playing = True
                        print("boss dead")
                        crack.y += crack.dy
                        crack.dy -= 10
                        player.gold += 100
                        print(player.gold)




        # flat here
        for flat in flats:
            if player.is_aabb_collision(flat):
                player.collision(flat)
                player.player_dead_by_enemy()

        for missile in missiles:
            if player.is_aabb_collision(missile):
                player.collision(missile)
                player.player_dead_by_enemy()
                missile.start_timer = True



        # setting for camera movement
        # check limit of camera y
        camera.update(player.x, player.y)
        if camera.y < 200:
            camera.y = 200
        elif camera.y > 240:
            camera.y = 240
        # to start the player in center of map
        camera_on = True
        camera.x = player.x

        if player.x > 8100:
            player.move()
            if not player.playing:
                os.system("afplay sounds/smb_stage_clear.wav&")
                player.playing = True

        if player.x > 8400:
           camera.x = 8400

        if player.x > 9200:
            player.restart()


        # change the place where the player is
        if player.x < -340:
            player.x = -340
            camera.x = player.x
            player.dx = 0

        if player.y < -101 and not game.playing:
            os.system("afplay sounds/smb_mariodie.wav&")
            game.playing = True
    # fall from the ground
        if player.y < -100:
            player.dy += 10
            print("you die")
            player.is_alive = False
            player.direction = "down"
            if player.dy > 10:
                player.start_timer = True





    wn.update()