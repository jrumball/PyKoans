#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
#    sides_set = sorted(set([a,b,c]))
#    len_sides_set = len(sides_set)
    
    sides = sorted([a,b,c])
    
    if sides[0] <= 0:
        raise TriangleError('Sides can not be less than or equal to 0 (zero)')
    elif sides[0] + sides [1] <= sides[2]:
        raise TriangleError('Invalid sides')
    
    len_sides = len(set(sides))
    if len_sides == 1:
        return 'equilateral'
    elif len_sides == 2:
        return 'isosceles'
    else:
        return 'scalene'
    


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
