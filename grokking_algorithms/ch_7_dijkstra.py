# ------------------my solution-----------------------------------

from typing import Union
from copy import deepcopy
from math import inf


def dijkstra(
        graph, cost: dict,
        parents: dict, start: str = 'start',
        end: str = 'end') -> Union[float, int]:
    visited = []
    graph = deepcopy(graph)
    parents = deepcopy(parents)
    cost = deepcopy(cost)
    node_value = float(inf)
    while set(cost.keys()) != set(visited):
        for k, v in cost.items():
            if k not in visited and v < node_value:
                node_value = v
                node_name = k
        visited += [node_name]
        for child_name, child_value in graph[node_name].items():
            if cost[child_name] > child_value + cost[node_name]:
                cost[child_name] = child_value + cost[node_name]
                parents[child_name] = node_name
        node_value = float(inf)
    res = f'Distance to {end} = {cost[end]}'
    rout = f'Rout to {end}'
    rout_point = end
    while rout_point != start:
        rout += ' -->'
        for k, v in parents.items():
            if k == rout_point:
                rout += f' {v}'
                rout_point = v
                break
    return res, rout


if __name__ == "__main__":
    graph = {}
    graph["start"] = {}
    graph["start"]["A"] = 6
    graph["start"]["B"] = 2
    graph["B"] = {}
    graph["B"]["A"] = 3
    graph["A"] = {}
    graph["A"]["end"] = 1
    graph["B"]["end"] = 5
    graph["end"] = {}

    cost = {}
    cost["start"] = 0
    cost["A"] = float(inf)
    cost["B"] = float(inf)
    cost["end"] = float(inf)

    parents = {}
    parents["A"] = None
    parents["B"] = None
    parents["end"] = None

    res = dijkstra(graph, cost, parents)
    print(res[0], res[1], sep='\n')

# ------------------2 exercice-----------------------------------
    graph = {}
    graph["Reykjavik"] = {}
    graph["Reykjavik"]["Oslo"] = 5
    graph["Reykjavik"]["London"] = 4
    graph["London"] = {}
    graph["London"]["Berlin"] = 3
    graph["Oslo"] = {}
    graph["Oslo"]["Berlin"] = 1
    graph["Oslo"]["Moscow"] = 3
    graph["Berlin"] = {}
    graph["Berlin"]["Rome"] = 2
    graph["Berlin"]["Belgrade"] = 9
    graph["Rome"] = {}
    graph["Rome"]["Athens"] = 2
    graph["Belgrade"] = {}
    graph["Belgrade"]["Athens"] = 1
    graph["Belgrade"]["Moscow"] = 5
    graph["Athens"] = {}
    graph["Athens"]["Rome"] = 2
    graph["Athens"]["Belgrade"] = 1
    graph["Athens"]["Moscow"] = 4
    graph["Moscow"] = {}
    graph["Moscow"]["Belgrade"] = 5
    graph["Moscow"]["Athens"] = 4

    costs = {}
    costs["Reykjavik"] = 0
    costs["London"] = float("inf")
    costs["Oslo"] = float("inf")
    costs["Berlin"] = float("inf")
    costs["Rome"] = float("inf")
    costs["Belgrade"] = float("inf")
    costs["Athens"] = float("inf")
    costs["Moscow"] = float("inf")

    parents = {}
    parents["Reykjavik"] = None
    parents["London"] = None
    parents["Oslo"] = None
    parents["Berlin"] = None
    parents["Rome"] = None
    parents["Belgrade"] = None
    parents["Athens"] = None
    parents["Moscow"] = None

    res = dijkstra(graph, costs, parents, "Reykjavik", "Athens")
    print(res[0], res[1], sep='\n')

# ------------------2 exercice-----------------------------------
    graph = {}
    graph["start"] = {}
    graph["start"]["A"] = 5
    graph["start"]["B"] = 2
    graph["A"] = {}
    graph["A"]["D"] = 2
    graph["A"]["C"] = 4
    graph["B"] = {}
    graph["B"]["A"] = 8
    graph["B"]["D"] = 7
    graph["C"] = {}
    graph["C"]["D"] = 6
    graph["C"]["end"] = 3
    graph["D"] = {}
    graph["D"]["end"] = 1
    graph["end"] = {}

    cost = {}
    cost["start"] = 0
    cost["A"] = float(inf)
    cost["B"] = float(inf)
    cost["C"] = float(inf)
    cost["D"] = float(inf)
    cost["end"] = float(inf)

    parents = {}
    parents["A"] = None
    parents["B"] = None
    parents["end"] = None

    res = dijkstra(graph, cost, parents)
    print(res[0], res[1], sep='\n')
