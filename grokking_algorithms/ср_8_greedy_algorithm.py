from copy import deepcopy


states_needed = {
    "mt", "wa", "or", "id", "nv", "ut", "са", "az",
    "co", "al", "ar", "fl", "ct", "ga", "tn", "tx"
}
states_needed_1 = {"wa", "or", "ct", "ga", "tn", "tx"}

stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "са"},
    "kfour": {"nv", "ut"},
    "kfive": {"co", "ca", "az"},
    "ksix": {"co", "al", "fl"},
    "kseven": {"ar", "fl", "ct", "ut"},
    "keight": {"ct", "ga", "tn"},
    "knine": {"id", "nv", "al", "tx"}
}


def find_cover(
        stations: dict = stations,
        states_needed: set = states_needed) -> list:
    res = []
    stations = deepcopy(stations)
    states_needed = states_needed.copy()
    station = ''
    station_states = {}
    while states_needed:
        for k, v in stations.items():
            if k not in res and len(station_states) < len(v & states_needed):
                station = k
                station_states = v
        res.append(station)
        states_needed.difference_update(station_states)
        station_states = {}
    return res


def find_cover_1(
        stations: dict = stations,
        states_needed: set = states_needed) -> list:
    final_list = {}
    stations = deepcopy(stations)
    states_needed = states_needed.copy()
    while states_needed:
        current_station = 0
        for station in stations:
            if current_station < len(states_needed & stations[station]):
                current_station = len((states_needed & stations[station]))
                name_station = station
        final_list[name_station] = stations[name_station]
        states_needed = states_needed - stations[name_station]
        del stations[name_station]
    return list(final_list.keys())


if __name__ == "__main__":
    assert find_cover(stations, states_needed) == [
        'kseven', 'knine', 'ktwo', 'kthree', 'kfive', 'keight'
    ]
    assert find_cover_1(stations, states_needed) == [
        'kseven', 'knine', 'ktwo', 'kthree', 'kfive', 'keight'
    ]
    assert find_cover(stations, states_needed_1) == [
        'ktwo', 'kthree', 'kseven', 'keight', 'knine'
    ]
    assert find_cover_1(stations, states_needed_1) == [
        'keight', 'ktwo', 'kthree', 'knine'
    ]
    print("all test passed")
