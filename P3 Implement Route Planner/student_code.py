def shortest_path(M,start,goal):

    # Map info
    intersections = M.intersections
    roads = M.roads

    def dist_between(node1,node2):
        node1 = intersections[node1]
        node2 = intersections[node2]
        return math.sqrt((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)



    def heuristic_cost_estimate(node1,node2):
        node1 = intersections[node1]
        node2 = intersections[node2]
        return math.sqrt((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)
    
    def reconstruct_path(cameFrom, current):
        if not cameFrom:
            return [current]
        
        path = []
        while cameFrom[current] in cameFrom.keys():
            path.append(current)
            current = cameFrom[current]
        path.append(current)
        path.append(cameFrom[current])
        path.reverse()
        return path


    closedSet = set()

    openSet = {start}

    cameFrom = dict()


    gScore = {i:math.inf for i in intersections.keys()}

    gScore[start] = 0


    fScore = {i:math.inf for i in intersections.keys()}

    fScore[start] = heuristic_cost_estimate(start, goal)


    while openSet:
        fScore_openSet = { i:fScore[i] for i in openSet }
        current = min(fScore_openSet , key=fScore_openSet.get)
        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        closedSet.add(current)

        for neighbor in roads[current]:
            if neighbor in closedSet:
                continue
            else:
                openSet.add(neighbor)
            tentative_gScore = gScore[current] + dist_between(current,neighbor)

            if tentative_gScore >= gScore[neighbor]:
                continue

            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(neighbor,goal)

    return "Goal can not be reached."