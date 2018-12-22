#!/usr/local/bin/python3
from math import sin, cos, sqrt, atan2, radians
from functools import reduce
import sys
import itertools
import functools

print('Santa is on the way!')

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
    home = (68.07361, 29.31527)
    route_acc = reduce(
        lambda acc, point: (point[1], acc[1] + distance(point[1], acc[0])),
            route, (home, 0))
    return route_acc[1] + distance(home, route_acc[0])

def split_to_runs(perm, weight_limit = 10000000):
    all_runs = [] 
    run = []
    current_limit = weight_limit
    for entry in perm:
        if (current_limit >= entry[1]): 
            run.append((entry[0], entry[2]))
            current_limit = current_limit - entry[1]
        else:
            all_runs.append(run);
            run = [(entry[0], entry[2])]
            current_limit = weight_limit - entry[1]
    all_runs.append(run)
    return all_runs

def evaluate_permutation(perm):
    runs = split_to_runs(perm)
    return reduce(
        lambda acc, run: run_around_distance(run) + acc,
        runs, float(0)
        ), runs

def print_route(route, filename = 0):
    if(filename == 0):
        print('; '.join([recipient for recipient, point in run]))
    else:
        with open(sys.path[0] + filename, 'w') as f:
            for run in route:
                print('; '.join([recipient for recipient, point in run]), file=f)
            

data = []        
with open(sys.path[0] + '/../nicelist.txt', 'r') as file:
    for line in file:
        entry = line.strip().split(";")
        data.append((entry[0], int(entry[3]), (float(entry[1]), float(entry[2]))))

best = -1;
best_route = []
i = 1;
for perm in itertools.permutations(data):
    score, route = evaluate_permutation(perm)
    if (score < best or best == -1): 
        print("NEW BEST ROUTE FOUND ", str(i), best)
        i = i + 1
        best = score
        best_route = route
        print_route(best_route, '/best_route.csv')

print('----------- BEGIN BEST ROUTE ----------')
print_route(best_route)
print('----------- END BEST ROUTE ------------')

