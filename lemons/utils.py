from lemons.error import Error
import math
import os
import random
 
"""
Utils ->
  list_prod
  point_distance
"""

class Utils:
  def list_prod(list_to_prod):
    val = 1
    for i in list_to_prod:
      val *= i
    return val
  
#______________________________________________________________________

  def point_distance(point1, point2):
    wrong_dim = Error("dimensions dont match")
    if len(point1) == len(point2):
      p1 = point1
      p2 = point2
      dimensions = len(point1)
    else:
      wrong_dim.custom()
    distance = 0.0
    for i in range(dimensions):
      sub = p1[i] - p2[i]
      distance += (sub * sub)
    return math.sqrt(distance)
    
#______________________________________________________________________

#end
