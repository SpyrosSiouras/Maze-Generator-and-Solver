from maze import * 


def make_graph(V: list[int],E: list[tuple]) -> dict:
    """
    function that converts the edges from a list of tuples to a dictionary
    """
    graph = {}
    for elem in V:
        tempList = []
        for item in E:
            if elem in item:
                if elem == item[0]:
                    tempList.append(item[1])
                else:
                    tempList.append(item[0])
        graph[elem] = tempList
        tempList = []
    
    return graph


