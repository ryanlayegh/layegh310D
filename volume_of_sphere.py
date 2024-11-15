# -*- coding: utf-8 -*-
"""volume_of_sphere.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QFRAK5MtLeLpYaYh2UhzRFSh_975hS0u
"""

import math
def calculate_volume_of_sphere(radius):
    volume= (4/3) * math.pi * radius**3
    return volume

radii = [30, 40]
for radius in radii:
    volume = calculate_volume_of_sphere(radius)
    print(f" Sphere with radius {radius} has a volume of {volume:.2f}")