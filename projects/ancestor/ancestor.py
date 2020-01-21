
current_earliest_parents=[]
def earliest_ancestor(ancestors, starting_node, distance=0):
    parents = parent_finder(ancestors, starting_node)
    if distance == 0 and parents == None:
        clear_list()
        return -1
    
    # if starting node has a parent

    if parents != None:
        distance += 1
        for parent in parents:
            earliest_ancestor(ancestors, parent, distance)
    else:
        current_earliest_parents.append([starting_node, distance])
    
    earliest_parents = current_earliest_parents.copy()
    # if len(current_earliest_parents) > 0:
    #     current_earliest_parents = []

    earliest_parent = (0,0)
    earliest_parent_2 = None
    for parent in earliest_parents:
        if parent[1] > earliest_parent[1]:
            earliest_parent = parent
        elif parent[1] == earliest_parent[1]:
            earliest_parent_2 = parent
    # print('lists', earliest_parents, current_earliest_parents)
    if earliest_parent_2:
        if earliest_parent_2[0] > earliest_parent[0]:

            return earliest_parent[0]
        else:

            return earliest_parent_2[0]
    else:

        return earliest_parent[0]

def clear_list():
    current_earliest_parents.clear()


def parent_finder(ancestors, node):
    parents = []
    for connection in ancestors:
        if connection[1] == node:
            parents.append(connection[0])

    if len(parents) < 1:
        return None
    else:
        return parents



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(parent_finder(test_ancestors, 3))

print(earliest_ancestor(test_ancestors, 1))
clear_list()
print(earliest_ancestor(test_ancestors, 2))
clear_list()
print(earliest_ancestor(test_ancestors, 3))
clear_list()
print(earliest_ancestor(test_ancestors, 4))
clear_list()
print(earliest_ancestor(test_ancestors, 5))
clear_list()
print(earliest_ancestor(test_ancestors, 6))
clear_list()
print(earliest_ancestor(test_ancestors, 7))
clear_list()
print(earliest_ancestor(test_ancestors, 8))
clear_list()
print(earliest_ancestor(test_ancestors, 9))
clear_list()
print(earliest_ancestor(test_ancestors, 10))
clear_list()
print(earliest_ancestor(test_ancestors, 11))





