INFINITY = float('inf')

graph = {
    # Start point
    'Start': {
        'A': 5,
        'B': 2
    },

    # Point A
    'A': {
        'C': 4,
        'D': 2
    },

    # Point B
    'B': {
        'A': 8,
        'D': 7
    },

    'C': {
        'D': 6,
        'Finish': 3
    },

    'D': {
        'Finish': 1
    },

    # Finish point
    'Finish': {},
}

costs = {
    'A': 5,
    'B': 2,
    'C': INFINITY,
    'D': INFINITY,
    'Finish': INFINITY,
}

parents = {
    'A': 'Start',
    'B': 'Start',
    'C': None,
    'D': None,
    'Finish': None,
}
