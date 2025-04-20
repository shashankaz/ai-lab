import heapq

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    pq = [(heuristics[start], start, [start])]

    while pq:
        _, current, path = heapq.heappop(pq)
        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [neighbor]))

    return None


#######################################################################################

def a_star(graph, heuristics, start, goal):
    visited = set()
    pq = [(heuristics[start], 0, start, [start])]  # (f = g + h, g, current, path)

    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None
