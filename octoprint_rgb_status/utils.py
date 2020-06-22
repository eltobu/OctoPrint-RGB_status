# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from math import sqrt


def blend(a, b, t):
    return sqrt((1-t)*pow(a, 2) + t * pow(b, 2))


def blend_colors(color1, color2, percentage):
    return (
       int(blend(color1[0], color2[0], percentage)),
       int(blend(color1[1], color2[1], percentage)),
       int(blend(color1[2], color2[2], percentage))
   )


def hex_to_rgb(h):
    if h is None:
        return (0, 0, 0)
    h = h[1:7]
    return tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))


def rgb_to_raw(c):
	return (int(pow(c[0], 2) / 256), int(pow(c[1], 2) / 256), int(pow(c[2], 2) / 256))
