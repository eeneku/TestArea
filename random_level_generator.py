# -*- coding: utf-8 -*-
__author__ = 'eeneku'

import random
import pyglet
import math

from pyglet.gl import *

key_state = pyglet.window.key.KeyStateHandler()

SEED = 'mika'

window = pyglet.window.Window(1280, 720)
red_image = pyglet.image.load("red.png")
white_image = pyglet.image.load("white.png")
tile_set = pyglet.image.load("road_tiles2.png")
hex_test = pyglet.image.load("Hex Tiles/Fire.png")
hex_test.anchor_x = 55
hex_test.anchor_y = 64

window.push_handlers(key_state)

hex_width = 110
hex_height = 128

print(128*0.75)
print(int(math.sqrt(3)/2*128))

hex_spacing_y = 96
hex_spacing_x = 110

N = 1
S = 10
W = 100
E = 1000
NW = 2
NE = 20
SE = 200
SW = 2000

directions = {
    (1, 0): E,
    (-1, 0): W,
    (0, -1): S,
    (0, 1): N,
    (1, 1): NE,
    (-1, 1): NW,
    (-1, -1): SW,
    (1, -1): SE
}

tile_size = 32

tiles = {}
tiles[NW+E] = tile_set.get_region(0, 0, tile_size, tile_size)
tiles[NE+W] = tile_set.get_region(32, 0, tile_size, tile_size)
tiles[NW+SW] = tile_set.get_region(64, 0, tile_size, tile_size)
tiles[NE+SE] = tile_set.get_region(96, 0, tile_size, tile_size)

tiles[SW+E] = tile_set.get_region(0, 32, tile_size, tile_size)
tiles[SE+W] = tile_set.get_region(32, 32, tile_size, tile_size)
tiles[NW+NE] = tile_set.get_region(64, 32, tile_size, tile_size)
tiles[SW+SE] = tile_set.get_region(96, 32, tile_size, tile_size)

tiles[W+E] = tile_set.get_region(0, 64, tile_size, tile_size)
tiles[N+E] = tile_set.get_region(32, 64, tile_size, tile_size)
tiles[N+W] = tile_set.get_region(64, 64, tile_size, tile_size)
tiles[SW+NE] = tile_set.get_region(96, 64, tile_size, tile_size)
tiles[N+SE] = tile_set.get_region(128, 64, tile_size, tile_size)
tiles[N+SW] = tile_set.get_region(160, 64, tile_size, tile_size)

tiles[S+N] = tile_set.get_region(0, 96, tile_size, tile_size)
tiles[S+E] = tile_set.get_region(32, 96, tile_size, tile_size)
tiles[S+W] = tile_set.get_region(64, 96, tile_size, tile_size)
tiles[NW+SE] = tile_set.get_region(96, 96, tile_size, tile_size)
tiles[S+NE] = tile_set.get_region(128, 96, tile_size, tile_size)
tiles[S+NW] = tile_set.get_region(160, 96, tile_size, tile_size)

print(len(tiles))


class Node(object):
    """
    This class here represents a single node in my generated structure.
    """

    def __init__(self, prv_node, nodes):
        if prv_node:
            self.prev_node = prv_node
            self.x = prv_node.get_next_pos()[0]
            self.y = prv_node.get_next_pos()[1]
        else:
            self.prev_node = None
            self.x = 0
            self.y = 0

        self.nodes = nodes

        self.next_x = 0
        self.next_y = 0

        self.tile = None

    def randomise_next_pos(self):
        free_positions = []

        for y in range(-1, 1+1):
            for x in range(-1, 1+1):

                if not (self.x+x, self.y+y) in self.nodes:
                    free_positions.append((x, y))

        if len(free_positions):
            seed = SEED
            seed += str(self.x)
            seed += str(self.y)
            seed += str(len(self.nodes))

            random.seed(seed.encode('hex'))
            random.shuffle(free_positions)
            self.set_next(free_positions.pop())
            self._mark_surrounding_nodes(free_positions)

            if self.prev_node:
                prev_dir = directions[-(self.x-self.prev_node.x),
                                      -(self.y-self.prev_node.y)]
                next_dir = directions[(self.next_x, self.next_y)]
                self.tile = tiles[prev_dir+next_dir]

            return True
        else:
            return False

    def set_next(self, (x, y)):
        self.next_x = x
        self.next_y = y

    def get_next_pos(self):
        return self.x+self.next_x, self.y+self.next_y

    def get_pos(self, x=0, y=0):
        return self.x+x, self.y+y

    def _mark_surrounding_nodes(self, free_positions):
        if self.next_x == 0:
            if (-1, self.next_y) in free_positions:
                free_positions.remove((-1, self.next_y))
            if (0, self.next_y) in free_positions:
                free_positions.remove((0, self.next_y))
            if (1, self.next_y) in free_positions:
                free_positions.remove((1, self.next_y))
        elif self.next_y == 0:
            if (self.next_x, -1) in free_positions:
                free_positions.remove((self.next_x, -1))
            if (self.next_x, 0) in free_positions:
                free_positions.remove((self.next_x, 0))
            if (self.next_x, 1) in free_positions:
                free_positions.remove((self.next_x, 1))

        for pos in free_positions:
            self.nodes[(self.x+pos[0], self.y+pos[1])] = 'reserved'


def random_value(seed=''):
    if seed and isinstance(seed, (str, unicode)):
        random.seed(seed.encode('hex'))

    return random.random()


def add_new_node(prev_node):
    if not prev_node:
        new_node = Node(None, nodes)
    else:
        new_node = Node(prev_node, nodes)

    nodes[new_node.get_pos()] = new_node

    if not new_node.randomise_next_pos():
        return None
    else:
        return new_node

base_value = random_value(SEED)
nodes = {}
prev_node = None
route_length = int(0 + base_value * 100)

print("route length: " + str(route_length))

for i in range(route_length):
    prev_node = add_new_node(prev_node)
    if not prev_node:
        break

print('map set')

fps = pyglet.clock.ClockDisplay()

world_x = 0
world_y = 0


def update(dt):
    global world_y, world_x

    if key_state[pyglet.window.key.UP]:
        world_y -= 100 * dt
    if key_state[pyglet.window.key.DOWN]:
        world_y += 100 * dt
    if key_state[pyglet.window.key.RIGHT]:
        world_x -= 100 * dt
    if key_state[pyglet.window.key.LEFT]:
        world_x += 100 * dt


@window.event
def on_draw():
    window.clear()

    pyglet.gl.glPushMatrix()
    pyglet.gl.glTranslatef(world_x, world_y, 0)

    for node in nodes:
        if nodes[node] == 'reserved':
            white_image.blit(500+node[0]*tile_size, 360+node[1]*tile_size)
        else:
            if nodes[node].tile:
                nodes[node].tile.blit(500+node[0]*tile_size, 360+node[1]*tile_size)

    pyglet.gl.glPopMatrix()
    pyglet.gl.glLoadIdentity()

    x = 160
    y = 160



    fps.draw()

pyglet.clock.schedule(update)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

pyglet.app.run()