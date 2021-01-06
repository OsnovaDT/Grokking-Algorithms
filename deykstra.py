# from data_for_exercise_7_1_A import graph, costs, parents
# from data_for_exercise_7_1_B import graph, costs, parents
from data_for_exercise_7_1_C import graph, costs, parents

INFINITY = float('inf')


def get_node_nearest_to_start_node(costs, processed_nodes):
    # Sort costs by values
    sorted_costs = sorted(
        list(costs.items()),
        key=lambda item: item[1]
    )
    sorted_costs = iter(sorted_costs)

    node_nearest_to_start_node = next(sorted_costs)

    # If the node was processed take next node
    try:
        while node_nearest_to_start_node in processed_nodes:
            node_nearest_to_start_node = next(sorted_costs)

        # Add the node to processed nodes
        processed_nodes.append(node_nearest_to_start_node)
    # If there are all nodes in processed_nodes
    except StopIteration:
        node_nearest_to_start_node = None

    return node_nearest_to_start_node


def run_deykstra_algorithm(graph, costs, parents, processed_nodes):
    # While not all nodes are processed yet
    while len(processed_nodes) != len(graph) - 1:
        # Get name and weight for node, nearest to start node
        node_nearest_to_start_node, weight_for_node_nearest_to_start_node \
            = get_node_nearest_to_start_node(costs, processed_nodes)

        # Neighbors for current node
        neighbors = graph[node_nearest_to_start_node].items()

        # Update the cost of neighbours node_nearest_to_start_node
        for neighbour_node, neighbour_weight in neighbors:
            neighbour_node_cost_by_new_way = neighbour_weight + \
                weight_for_node_nearest_to_start_node

            # If new cost for neighbour node less then old
            if neighbour_node_cost_by_new_way < costs[neighbour_node]:
                costs[neighbour_node] = neighbour_node_cost_by_new_way

                # Change parent for neighbour node
                parents[neighbour_node] = node_nearest_to_start_node


def main():
    # The main task for chapter 7

    # graph = {
    #     # Start point
    #     'Start': {
    #         'A': 6,
    #         'B': 2
    #     },

    #     # Point A
    #     'A': {'Finish': 1},

    #     # Point B
    #     'B': {
    #         'A': 3,
    #         'Finish': 5
    #     },

    #     # Finish point
    #     'Finish': {},
    # }

    # costs = {
    #     'A': 6,
    #     'B': 2,
    #     'Finish': INFINITY,
    # }

    # parents = {
    #     'A': 'Start',
    #     'B': 'Start',
    #     'Finish': None,
    # }

    processed_nodes = []

    run_deykstra_algorithm(graph, costs, parents, processed_nodes)
    print(costs['Finish'])
    print(parents)


if __name__ == '__main__':
    main()
