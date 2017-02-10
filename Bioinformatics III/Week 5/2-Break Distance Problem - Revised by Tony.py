import sys
import math
import numpy as np


def blocks(line, max_val=None):
    """
    Transfer the string genome into integers.
    """

    chromosome = [i.split(' ') for i in line.split(')(')]
    chromosome[0][0] = chromosome[0][0][1:]            # Remove unnecessary parts of the genome.
    chromosome[-1][-1] = chromosome[-1][-1][:-1]

    chromosome = np.array(chromosome).astype('int')

    if not max_val:
        max_val = max(abs(chromosome))

    return chromosome, max_val


def get_edges(chromosome):
    """
    Get edges from chromosomes.
    """
    edges = []
    for i in range(len(chromosome)):
        for j in range(len(chromosome[i]) - 1):
            m = 2 * chromosome[i][j]
            if chromosome[i][j] <= 0:
                m = -m -1

            n = 2 * -chromosome[i][j+1]
            if chromosome[i][j+1] > 0:
                n = -n -1

            edges.append((m, n))

        m = 2 * chromosome[i][j + 1]   
        if chromosome[i][j + 1] <= 0:
            m = -m - 1

        n = 2 * -chromosome[i][0]   
        if chromosome[i][j + 1] <= 0:
            n = -n - 1

        edges.append((m, n))
        
    return edges


def get_next_node(edges, n):
    """
    Find a next node of an edge and delete the used edge.
    """
    for i in range(len(edges)):
        for j in range(2):
            if edges[i][j] == n:
                n = edges[i][1] if j == 0 else edges[i][0]
                edges.remove(edges[i])
                return
    return


"""
Input
"""
line = sys.stdin.read().splitlines()

"""
Get chromosome1, 2 and the max number of blocks.
"""
max_val = 0
chromosome1 = blocks(line[0], max_val)
chromosome2 = blocks(line[1], max_val)

"""
Get edges of chromosome1 and 2.
"""
edges1 = get_edges(chromosome1)
edges2 = get_edges(chromosome2)

"""
Find how many circles there are.
"""
circles = 0
while edges1 != []:                                     # If we find all circles with no edge left, stop the while loop.
    first = edges1[0][0]                                # first as the first node of the circle.
    n = edges1[0][1]                                    # n as the end of the edge, the next node.
    edges1.remove(edges1[0])                            # remove used edges.
    while n != first:                                   # Go through a circle.
        get_next_node(edges2, n)
        if n != first:                                  # Cause circles consist of alternative edges...
            get_next_node(edges1, n)
    circles += 1

"""
2-Break Distance = Blocks - Circles and print it out.
"""
print(max_val - circles)