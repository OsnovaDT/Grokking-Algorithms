'''Some data for chapter 7, task 7.1 (B)'''


INFINITY = float('inf')

graph = {
    # Start point
    'Start': {
        'A': 10,
    },

    # Point A
    'A': {
        'C': 20,
    },

    # Point B
    'B': {
        'A': 1,
    },

    'C': {
        'B': 1,
        'Finish': 30
    },

    # Finish point
    'Finish': {},
}

costs = {
    'A': 10,
    'B': INFINITY,
    'C': INFINITY,
    'Finish': INFINITY,
}

parents = {
    'A': 'Start',
    'B': None,
    'C': None,
    'D': None,
    'Finish': None,
}
