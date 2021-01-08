'''Code for chapter 8'''


def get_required_stations(states, all_stations):
    '''Get required stations for cover all states'''

    required_stations = []

    station_with_max_state_coverage = None

    # While not all states were covered
    while states:
        # Find station with max states cover
        min_states_amount_after_station_add = len(states)

        for station, states_for_station in all_stations.items():
            if len(states - states_for_station) < min_states_amount_after_station_add:
                min_states_amount_after_station_add = len(
                    states - states_for_station
                )
                station_with_max_state_coverage = station

        # Amount of states that need to cover will reduce
        states -= all_stations[station_with_max_state_coverage]

        # Move station from all_stations to required_stations
        all_stations.pop(station_with_max_state_coverage)
        required_stations.append(station_with_max_state_coverage)

    return required_stations


def main():
    '''Run get_required_stations function'''

    states = {
        'mt', 'wa', 'or', 'id',
        'nv', 'ut', 'ca', 'az'
    }

    all_stations = {
        # For each station there are states
        'station_1': {'id', 'nv', 'ut'},
        'station_2': {'wa', 'id', 'mt'},
        'station_3': {'or', 'nv', 'ca'},
        'station_4': {'nv', 'ut'},
        'station_5': {'ca', 'az'},
    }

    print(get_required_stations(states, all_stations))


if __name__ == '__main__':
    main()
