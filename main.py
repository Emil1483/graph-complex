import pygame
from screen import screen
from numpy import arange
import math

import point


def f(x, a):
    if x == 0:
        x = 0.01
    r = math.sqrt(x.real ** 2 + x.imag ** 2)
    theta = math.atan2(x.imag, x.real)
    b = math.log(r) + theta * 1j
    exponent = b + a * (x - b)
    return math.e ** exponent

# def sin(x, t):
#     a = x.real
#     b = x.imag

#     result = math.sin(a) * math.cosh(b) + 1j * math.cos(a) * math.sinh(b)

#     return x + t * (result - x)

# def f(x, t):
#     angle = math.pi * 9.5
#     return x * (1 + t * (math.e**(1j * angle) - 1))


# def f(x, t):
#     if x.real <= 1:
#         return None

#     sum = 0
#     for i in range(10):
#         sum += 1 / x ** i
#     return x + t * (sum - x)

input_range = 10
dt = input_range / 64
line_dt = input_range / 5
scale = 100

points = []

# horizontal lines
for j in arange(-input_range, input_range + line_dt, line_dt):
    for i in arange(-input_range, input_range + dt, dt):
        new_point = point.Point(i + j * 1j, f)

        if round(j, 5) == 0:
            new_point.set_color((50, 255, 0))

        if i > -input_range:
            new_point.add_friend(points[-1])

        points.append(new_point)

# vertical lines
for i in arange(-input_range, input_range + line_dt, line_dt):
    for j in arange(-input_range, input_range + dt, dt):
        new_point = point.Point(i + j * 1j, f)

        if round(i, 5) == 0:
            new_point.set_color((255, 100, 0))

        if j > -input_range:
            new_point.add_friend(points[-1])

        points.append(new_point)

# for j in arange(-input_range, input_range + dt, dt):
#     for i in arange(-input_range, input_range + dt, dt):
#         new_point = point.Point(i + j * 1j, f)

#         if round(i, 5) == 0:
#             new_point.set_color((255, 100, 0))

#         if round(j, 5) == 0:
#             new_point.set_color((50, 255, 0))

#         if i > -input_range:
#             new_point.add_friend(points[-1])

#         if j > -input_range:
#             index = -math.ceil(input_range * 2 / dt + 1)
#             new_point.add_friend(points[index])

#         points.append(new_point)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for point in points:
        point.show(scale)

    for point in points:
        point.update()

    pygame.display.flip()

pygame.quit()
