#!/usr/bin/local/python3
from math import sin, cos, sqrt, atan2, radians
from functools import reduce

print("Santa!")

home = (68.07361, 29.31527)


def distance(point1, point2):
    r = 6378
    lat1 = radians(point1[0])
    lon1 = radians(point1[1])
    lat2 = radians(point2[0])
    lon2 = radians(point2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    return r * c

def run_around_distance(route):
    route_acc = reduce(
        lambda acc, point: (point, acc[1] + distance(point, acc[0])),
            route, (home, 0))
    return route_acc[1] + distance(home, route_acc[0])
    
    

print("Home - p1 - home:" + str(distance(home, (40.733034,-86.762233)) * 2))
print("moi: " + str(run_around_distance(
    [(40.733034,-86.762233)]
    )))

