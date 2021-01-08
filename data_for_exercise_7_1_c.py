'''Some data for chapter 7, task 7.1 (C)'''


INFINITY = float('inf')

graph = {
    # Start point
    'Start': {
        'A': 2,
        'B': 2,
    },

    # Point A
    'A': {
        'B': 2,
    },

    # Point B
    'B': {
        'C': 2,
        'Finish': 2,
    },

    'C': {
        'A': -1,
        'Finish': 2
    },

    # Finish point
    'Finish': {},
}

costs = {
    'A': 2,
    'B': 2,
    'C': INFINITY,
    'Finish': INFINITY,
}

parents = {
    'A': 'Start',
    'B': 'Start',
    'C': None,
    'Finish': None,
}
