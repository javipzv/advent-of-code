import re
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

with open('input.txt', 'r') as file:
    input_data = [line.strip() for line in file]

distances = {}
cities = set()
for travel in input_data:
    origin, destination, distance = re.findall("(\w*) to (\w*) = (\d*)", travel)[0]
    distances[(origin, destination)] = int(distance)
    cities.add(origin)
    cities.add(destination)
