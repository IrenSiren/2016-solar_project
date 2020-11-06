# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def sign(x):
    if x >= 0:
        return 1
    else:
        return -1


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        else:
            r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
            body.Fx += sign(obj.x - body.x) * body.m * obj.m * gravitational_constant / r ** 2
            body.Fy += sign(obj.y - body.y) * body.m * obj.m * gravitational_constant / r ** 2


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    ay = body.Fy / body.m

    body.x += body.Vx * dt + ax * 0.5 * dt ** 2
    body.Vx += ax * dt

    body.y += body.Vy * dt + ay * 0.5 * dt ** 2
    body.Vy += ay * dt
    print(body.x, body.y, body.Vx, body.Vy, ax, ay)

def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
