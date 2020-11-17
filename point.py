import math
import pygame
from screen import screen

class Point:
    anim_value = 0
    dt = 0.005
    friends = None
    color = (255, 255, 255)

    def __init__(self, value, func):
        self.value = value
        self.func = func
        self.friends = []
    
    def set_color(self, color):
        self.color = color

    def add_friend(self, friend):
        self.friends.append(friend)

    def update(self):
        self.anim_value = min(1, self.anim_value + self.dt)

    def pos(self, scale):
        w, h = screen.get_size()

        value = -0.5 * math.cos(self.anim_value * math.pi) + 0.5

        trans = self.func(self.value, value)
        if trans is None: return None

        pos = scale * trans + w * 0.5 + h * 0.5j
        return (int(round(pos.real)), int(round(pos.imag)))

    def show(self, scale):
        my_pos = self.pos(scale)
        if my_pos is None: return

        for friend in self.friends:
            friend_pos = friend.pos(scale)
            if friend_pos is None: return

            my_brightness = sum(self.color) / 3
            friend_brightness = sum(friend.color) / 3
            color = self.color if my_brightness >= friend_brightness else friend.color

            pygame.draw.line(screen, color, my_pos, friend_pos)
