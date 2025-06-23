#######################  DEEP CLONE GRAPH #######################

# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution_shallow(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        # edge cases:
        #   - graph with 0 nodes: OK

        if not node:
            return node

        # create dictionary because graph size is unknown
        copy = {}
        visited = set()
        stack = [node]

        while stack:
            #take the latest added node
            dot = stack.pop()
            if dot not in visited:
                #Add to visited
                visited.add(dot)

                #Add to graph and remove from stack
                copy[dot] = Node(dot.val, dot.neighbors)

                for subdot in dot.neighbors:
                    stack.append(subdot)

        # for orig_node, cloned_node in copy.items():
        #     print("Original node {} -> Cloned node {}".format(orig_node.val, cloned_node.val))
        #     print("  Neighbors: {}".format([n.val for n in cloned_node.neighbors]))


        return copy[node]



class Solution_deep(object):
    def cloneGraph(self, node ):
        """
        :type node: Node
        :rtype: Node
        """

        # edge cases:
        #   - graph with 0 nodes: OK

        if not node:
            return node

        # create dictionary, keys will be the original node, and
        # value the independent node copy
        copy = {}
        neighbors_seen = {}

        # start stack with new node
        stack = [node]

        while stack:
            #take the latest added node
            dot = stack.pop()

            # check if node was already created not enough
            # because we create it when it is visited as a neighbor
            # needs to be condition around having neigbors

            if dot not in neighbors_seen:

                # create copy object
                if dot not in copy:
                    copy[dot] = Node(dot.val)

                neighbors_seen[dot] = 1

                # now go through neigbours
                for subdot in dot.neighbors:

                    if subdot not in copy:
                        copy[subdot] = Node(subdot.val)

                    if subdot not in neighbors_seen:
                        stack.append(subdot)

                    # Append cloned neighbor to cloned node
                    copy[dot].neighbors.append(copy[subdot])

        return copy[node]

        #return copy.deepcopy(node)

class Solution_simplet(object):
    def cloneGraph(self, node):
        if not node:
            return None

        copy = {}  # Original node → cloned node
        stack = [node]
        copy[node] = Node(node.val)

        while stack:
            curr = stack.pop()

            for neighbor in curr.neighbors:
                if neighbor not in copy:
                    # Clone the neighbor node
                    copy[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                # Link the clone of neighbor to the clone of current
                copy[curr].neighbors.append(copy[neighbor])

        return copy[node]
